import { Deck } from "./deck";
import { Card } from "./types";

const NUMBER_OF_ROWS = 4;

export class Board {
    public rows: Card[][];

    constructor(deck: Deck) {
        this.rows = Array.from({ length: NUMBER_OF_ROWS }, () => [] as Card[]);
        for (let i = 0; i < NUMBER_OF_ROWS; i++) {
            this.rows[i].push(deck.drawCard());
        }
    }
}
