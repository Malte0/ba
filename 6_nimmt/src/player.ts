import { Deck } from "./deck";
import { Card } from "./types";

const NUMBER_OF_CARDS_IN_HAND = 10;

export class Player {
    public name: string;
    public hand: Card[];
    public points: number;

    constructor(name: string, deck: Deck) {
        this.name = name;
        this.hand = [];
        for (let i = 0; i < NUMBER_OF_CARDS_IN_HAND; i++) {
            this.hand.push(deck.drawCard());
        }
        this.points = 0;
    }

    public addPoints(points: number): void {
        this.points += points;
    }

    // momentarily plays random card from hand
    public playCard(): Card {
        return this.hand.splice(Math.floor(Math.random() * this.hand.length), 1)[0];
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