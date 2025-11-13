import { Card } from "./types";

const TOTAL_CARDS = 104;
const CARDS: Card[] = (() => {
    const cards: Card[] = [];
    for (let i = 1; i <= TOTAL_CARDS; i++) {
        let points = 1;
        if (i % 5 === 0) points += 1;
        if (i % 10 === 0) points += 1;
        if (i % 11 === 0) points += 4;
        if (i === 55) points += 1;
        cards.push({ value: i, points });
    }
    return cards;
})();

export class Deck {
    private cards: Card[];

    constructor() {
        this.cards = [...CARDS];
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