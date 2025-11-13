import { Deck } from "./deck";
import { Strategy } from "./strategy";
import { Card } from "./types";

const NUMBER_OF_CARDS_IN_HAND = 10;

export class Player {
    public name: string;
    private hand: Card[];
    public points: number;
    private strategy: Strategy

    constructor(name: string, strategy: Strategy, deck: Deck) {
        this.name = name;
        this.hand = [];
        this.strategy = strategy;
        for (let i = 0; i < NUMBER_OF_CARDS_IN_HAND; i++) {
            this.hand.push(deck.drawCard());
        }
        this.points = 0;
    }

    public hasCards(): boolean {
        return this.hand.length > 0;
    }

    public addPoints(points: number): void {
        this.points += points;
    }

    // momentarily plays random card from hand
    public playCard(): Card {
        const cardIndexToPlay: number = this.strategy.cardToPlay([...this.hand]);
        const cardToPlay: Card = this.hand.slice(cardIndexToPlay, 0)[0];
        return cardToPlay;
    }

    // Picks the row with the least points
    public pickRow(boardRows: Card[][]): number {
        let minPoints = Infinity;
        let chosenRowIndex = -1;
        for (let i = 0; i < boardRows.length; i++) {
            const row = boardRows[i];
            const rowPoints = row.reduce((sum, card) => sum + card.points, 0);
            if (rowPoints < minPoints) {
                minPoints = rowPoints;
                chosenRowIndex = i;
            }
        }
        return chosenRowIndex;
    }
}