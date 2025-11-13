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

const mostDistantCardFrom = (middleCardValue: number) => {
  return (handCards: Card[]) => {
    const MIDDLE = middleCardValue;
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
  };
};

// Finds cards that are most distant from a center point
export const KEEP_MIDDLE = (middleValue: number) => {
  const distFunction = mostDistantCardFrom(middleValue);
  return {
    name: "Keep middle cards",
    description: "Plays high and low cards first",
    cardToPlay: (handCards: Card[]) => {
      return distFunction(handCards);
    },
  };
};

export const MIDDLE_AND_SAFE: Strategy = {
  name: "Middle and safe",
  description:
    "Plays high and low cards first, unless he has a card, that has a value at most n-1 higher than a card in a non full row",
  cardToPlay: (handCards: Card[]) => {
    const MIDDLE = 55;
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
  },
};
