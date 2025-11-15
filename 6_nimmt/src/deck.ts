import { Card } from "./types";
import config from "./config";

const CARDS: (totalCards: number) => Card[] = (totalCards: number) => {
    const cards: Card[] = [];
    for (let i = 1; i <= totalCards; i++) {
        let points = 1;
        if (i % 5 === 0) points += 1;
        if (i % 10 === 0) points += 1;
        if (i % 11 === 0) points += 4;
        if (i === 55) points += 1;
        cards.push({ value: i, points });
    }
    return cards;
};

export class Deck {
    private cards: Card[];

    constructor(numberOfPlayers: number) {
        this.cards = [...CARDS(config.Profi_Variante ? numberOfPlayers * 10 + 4 : config.Total_Cards_Default)];
        this.shuffle();
    }

    private shuffle(): void {
        for (let i = this.cards.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [this.cards[i], this.cards[j]] = [this.cards[j], this.cards[i]];
        }
    }

    public drawCard(): Card {
        if (this.cards.length === 0) {
            throw new Error("No cards left in the deck");
        }
        return this.cards.pop();
    }

    public remainingCards(): number {
        return this.cards.length;
    }
}