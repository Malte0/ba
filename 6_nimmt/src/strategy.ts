import { Card } from "./types"

export type Strategy = {
    name: string,
    cardToPlay: (handCards: Card[]) => number
}

export const RANDOM: Strategy = {
    name: "Play random Card",
    cardToPlay: (handCards: Card[]) => {
        const randomIndex = Math.floor(Math.random() * handCards.length);
        return randomIndex;
    }
}

export const LOWEST_CARD: Strategy = {
    name: "Play lowest Card",
    cardToPlay: (handCards: Card[]) => {
        let lowesValue = Infinity
        let lowestIndex: number = 0;
        for (let i = 0; i < handCards.length; i++) {
            const card = handCards[i];
            if (card.value < lowesValue) {
                lowesValue = card.value;
                lowestIndex = i;
            }
        }
        return lowestIndex;
    },
}