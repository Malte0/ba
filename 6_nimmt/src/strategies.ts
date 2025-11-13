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

export const KEEP_MIDDLE_CARDS: Strategy = {
  name: "Keep middle cards",
  description: "Plays high and low cards first",
  cardToPlay: (handCards: Card[]) => {
    return 0;
  },
};
