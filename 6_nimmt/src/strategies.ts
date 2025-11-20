import { Card, Strategy } from "./types";
import config from "./config";

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

function centerCard(numberOfPlayers: number) {
  const DIVISOR_FOR_MIDDLE = 60 / 104;
  const TOTAL_CARDS = config.Profi_Variante
    ? numberOfPlayers * 10 + 4
    : config.Total_Cards_Default;
  const MIDDLE = DIVISOR_FOR_MIDDLE * TOTAL_CARDS;
  return MIDDLE;
}

function mostDistantFromCenter(handCards: Card[], numberOfPlayers: number) {
  const middle = centerCard(numberOfPlayers);
  let highestDistance = 0;
  let indexOfHighestDistance = 0;
  for (let i = 0; i < handCards.length; i++) {
    const card = handCards[i];
    const distance = Math.abs(card.value - middle);
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
  cardToPlay: (handCards: Card[], cardsOnBoard, cardsLeft, numberOfPlayers) => {
    return mostDistantFromCenter(handCards, numberOfPlayers);
  },
};

// a card is safe to play, if it is at most spacesLeftInRow higher than a card on the board
function isSafeToPlay(
  card: Card,
  cardsOnBoard: Card[][],
  numberOfPlayers: number
) {
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
  cardToPlay: (
    handCards: Card[],
    cardsOnBoard: Card[][],
    cardsLeft: number[],
    numberOfPlayers: number
  ) => {
    const mostDistant = mostDistantFromCenter(handCards, numberOfPlayers);

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
  cardsLeft: number[],
  unreliability: number
) {
  const targetRowIndex = rowIndexCardWouldBePlacedAt(card, cardsOnBoard);
  if (targetRowIndex == -1) return false; // card cannot be placed at all
  const targetRow = cardsOnBoard[targetRowIndex];
  const lastCard = targetRow[targetRow.length - 1];
  const spacesLeftInRow = 5 - targetRow.length;

  let highestPossibleDistance = spacesLeftInRow;
  for (
    let highestPossibleValue = lastCard.value;
    highestPossibleValue < cardsLeft.length;
    highestPossibleValue++
  ) {
    // if memory is unrealiable takes a guess, whether card has been played
    const falseMemory: boolean = Math.random() < unreliability;
    const cardYetToPlay = falseMemory
      ? Math.round(Math.random())
      : cardsLeft[highestPossibleValue];
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
  cardToPlay: (
    handCards: Card[],
    cardsOnBoard: Card[][],
    cardsLeft: number[],
    numberOfPlayers: number
  ) => {
    const mostDistant = mostDistantFromCenter(handCards, numberOfPlayers);

    const totalCardsOnBoard = cardsOnBoard
      .map((row) => row.length)
      .reduce((prev, curr) => prev + curr, 0);
    if (totalCardsOnBoard < 9) return mostDistant;

    for (const handCard of handCards) {
      if (isSafeToPlayMemory(handCard, cardsOnBoard, cardsLeft, 0)) {
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

// sorts cards by distance from center, descending
function sortByDistance(cards: Card[], numberOfPlayers: number) {
  const center = centerCard(numberOfPlayers);
  const cardsWithDistance: [Card, number][] = cards.map((card) => {
    return [card, Math.abs(card.value - center)];
  });
  // sort descending
  cardsWithDistance.sort((a, b) => a[1] - b[1]).reverse();
  const cardsByDistance = cardsWithDistance.map((pair) => pair[0]);
  return cardsByDistance;
}

// The risk of a card is calculated by
// - Checking which row a card would likely go into (rows with closest card in case row with closest gets taken by another player)
// - The number of points in that row
// - The distance from center of that card (not playing it now might make one stuck with that card)
function riskOfCard(
  card: Card,
  cardsOnBoard: Card[][],
  numberOfPlayers: number, // not used yet, but could be used to adjust probabilities based on players
  cardsLeft: number[]
) {
  const rowStats: {
    lastCard: Card;
    cardsLeftInRow: number;
    pointsInRow: number;
    highestSafeValue: number;
  }[] = cardsOnBoard.map((row) => {
    return {
      lastCard: row[row.length - 1],
      cardsLeftInRow: 5 - row.length,
      pointsInRow: row.map((card) => card.points).reduce((a, b) => a + b, 0),
      highestSafeValue: 1,
    };
  });

  for (const row of rowStats) {
    let highestPossibleDistance = row.cardsLeftInRow;
    for (
      let highestPossibleValue = row.lastCard.value;
      highestPossibleValue < cardsLeft.length;
      highestPossibleValue++
    ) {
      const cardYetToPlay = cardsLeft[highestPossibleValue];
      highestPossibleDistance -= cardYetToPlay;
      if (highestPossibleDistance == 0) {
        row.highestSafeValue = highestPossibleValue;
        break;
      }
    }
  }

  // determine order of rows where card would go to

  return 0;
}

export const SELECTIVE_DISTANCE: Strategy = {
  name: "Selective Distance",
  description:
    "Checks whether high or low cards are safer to play, plays the card with the least risk. The least risk is a probability of having to take a row multiplied by the number of points present in the rows.",
  cardToPlay: (
    handCards: Card[],
    cardsOnBoard: Card[][],
    cardsLeft: number[],
    numberOfPlayers: number
  ) => {
    const cardsByDistance: Card[] = sortByDistance(handCards, numberOfPlayers);

    return 0;
  },
};

export const UNRELIABLE: (unreliability: number) => Strategy = (
  unreliability: number
) => {
  return {
    name: "Unreliable",
    description: "Same as safe with memory, but has unreliable memory",
    cardToPlay: (
      handCards: Card[],
      cardsOnBoard: Card[][],
      cardsLeft: number[],
      numberOfPlayers: number
    ) => {
      const mostDistant = mostDistantFromCenter(handCards, numberOfPlayers);

      const totalCardsOnBoard = cardsOnBoard
        .map((row) => row.length)
        .reduce((prev, curr) => prev + curr, 0);
      if (totalCardsOnBoard < 9) return mostDistant;

      for (const handCard of handCards) {
        if (
          isSafeToPlayMemory(handCard, cardsOnBoard, cardsLeft, unreliability)
        ) {
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
};

// Additional ideas:
// vorhersehen, welchen stapel man beim Spielen einer zb. sehr hohen karte nehmen muesste und dann ne andere spielen
// Only other good sources for strategies
// https://math.rptu.de/komms/archiv/berichte-modellierungswochen/03/2019-spiele-spielstrategien
// https://pub.tik.ee.ethz.ch/students/2021-HS/GA-2021-02.pdf
// https://boardgamegeek.com/thread/436792/6-nimmt-strategy-tips
