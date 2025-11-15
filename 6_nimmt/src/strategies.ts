import { Card, Strategy } from "./types";

export const RANDOM: Strategy = {
  name: "Random",
  description: "Plays cards in order they were dealt",
  cardToPlay: (handCards: Card[]) => {
    return 0;
  },
};

export const LOWEST_CARD: Strategy = {
  name: "Lowest Card",
  description: "Always plays the card with the lowest value",
  cardToPlay: (handCards: Card[]) => {
    let lowestValue = Infinity;
    let lowestIndex: number = 0;
    for (let i = 0; i < handCards.length; i++) {
      const card = handCards[i];
      if (card.value < lowestValue) {
        lowestValue = card.value;
        lowestIndex = i;
      }
    }
    return lowestIndex;
  },
};

export const HIGHEST_CARD: Strategy = {
  name: "Highest Card",
  description: "Always plays the card with the highest value",
  cardToPlay: (handCards: Card[]) => {
    let highestValue = 0;
    let highestIndex: number = 0;
    for (let i = 0; i < handCards.length; i++) {
      const card = handCards[i];
      if (card.value > highestValue) {
        highestValue = card.value;
        highestIndex = i;
      }
    }
    return highestIndex;
  },
};

function mostDistantFrom60(handCards: Card[]) {
  const MIDDLE = 60;
  let highestDistance = 0;
  let indexOfHighestDistance = 0;
  for (let i = 0; i < handCards.length; i++) {
    const card = handCards[i];
    const distance = Math.abs(card.value - MIDDLE);
    if (distance > highestDistance) {
      highestDistance = distance;
      indexOfHighestDistance = i;
    }
  }
  return indexOfHighestDistance;
}

// Finds cards that are most distant from a center point
export const KEEP_MIDDLE: Strategy = {
  name: "Keep middle cards",
  description: "Plays high and low cards first",
  cardToPlay: (handCards: Card[]) => {
    return mostDistantFrom60(handCards);
  },
};

// a card is safe to play, if it is at most spacesLeftInRow higher than a card on the board
function isSafeToPlay(card: Card, cardsOnBoard: Card[][], numberOfPlayers: number) {
  const rowProperties = cardsOnBoard.map((row) => {
    return { lastCard: row[row.length - 1], cardsLeftInRow: 5 - row.length };
  });
  // console.table(cardsOnBoard)
  // console.log(rowProperties);
  const isSafe = rowProperties.some((property) => {
    const cardIsHigher = property.lastCard.value < card.value;
    const maxDistance = Math.min(numberOfPlayers - 1, property.cardsLeftInRow);
    const cardIsSafe = card.value <= property.lastCard.value + maxDistance;
    return cardIsHigher && cardIsSafe;
  });
  // console.log(isSafe);
  // console.log(card)
  return isSafe;
}

export const MIDDLE_AND_SAFE: Strategy = {
  name: "Middle and safe",
  description:
    "Plays high and low cards first, unless he has a card, that has a value at most n-1 higher than a card in a non full row",
  cardToPlay: (handCards: Card[], cardsOnBoard: Card[][], cardsLeft: number[], numberOfPlayers: number) => {
    const mostDistant = mostDistantFrom60(handCards);

    for (const handCard of handCards) {
      if (isSafeToPlay(handCard, cardsOnBoard, numberOfPlayers)) {
        return handCards.indexOf(handCard);
      }
    }

    return mostDistant;
  },
};

function rowIndexCardWouldBePlacedAt(card: Card, cardsOnBoard: Card[][]) {
  let lowestDiff = Infinity;
  let targetRowIndex = -1;
  for (let row of cardsOnBoard) {
    const lastCardInRow = row[row.length - 1];
    const diff = card.value - lastCardInRow.value;
    if (diff > 0 && diff < lowestDiff) {
      lowestDiff = diff;
      targetRowIndex = cardsOnBoard.indexOf(row);
    }
  }
  return targetRowIndex;
}

function isSafeToPlayMemory(
  card: Card, // card to be played
  cardsOnBoard: Card[][],
  cardsLeft: number[]
) {
  const targetRowIndex = rowIndexCardWouldBePlacedAt(card, cardsOnBoard);
  if (targetRowIndex == -1) return false; // card cannot be placed at all
  const targetRow = cardsOnBoard[targetRowIndex];
  const lastCard = targetRow[targetRow.length - 1];
  const spacesLeftInRow = 5 - targetRow.length;

  let highestPossibleDistance = spacesLeftInRow;
  for (let highestPossibleValue = lastCard.value; highestPossibleValue < cardsLeft.length; highestPossibleValue++) {
    const cardYetToPlay = cardsLeft[highestPossibleValue];
    highestPossibleDistance -= cardYetToPlay;
    if (highestPossibleDistance == 0) {
      return card.value > lastCard.value && card.value <= highestPossibleValue;
    }
  }

  return false;
}

export const SAFE_WITH_MEMORY: Strategy = {
  name: "Safe with Memory",
  description:
    "Plays high and low cards first, unless he has a card, that has a value at most n+k-1 higher than a card in a non full row, n is number of players, k is how many cards in the range have been played allready",
  cardToPlay: (handCards: Card[], cardsOnBoard: Card[][], cardsLeft: number[], numberOfPlayers: number) => {
    const mostDistant = mostDistantFrom60(handCards);

    const totalCardsOnBoard = cardsOnBoard.map((row) => row.length).reduce((prev, curr) => prev + curr, 0);
    if (totalCardsOnBoard < 9) return mostDistant;

    for (const handCard of handCards) {
      if (isSafeToPlayMemory(handCard, cardsOnBoard, cardsLeft)) {
        // console.log(cardsOnBoard);
        // console.log(handCards);
        // console.log(handCard);
        // console.log(handCards.indexOf(handCard));
        // throw new Error();
        return handCards.indexOf(handCard);
      }
    }
    return mostDistant;
  },
};

// Additional ideas:
// using a card to take a low amount of points on purpose
// vorhersehen, welchen stapel man beim Spielen einer zb. sehr hohen karte nehmen muesste und dann ne andere spielen
// Only other good sources for strategies
// https://math.rptu.de/komms/archiv/berichte-modellierungswochen/03/2019-spiele-spielstrategien
// https://pub.tik.ee.ethz.ch/students/2021-HS/GA-2021-02.pdf
// https://boardgamegeek.com/thread/436792/6-nimmt-strategy-tips