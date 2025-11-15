import { Deck } from "./deck";
import { Player } from "./player";
import { Card } from "./types";

const NUMBER_OF_ROWS = 4;

export class Board {
  public rows: Card[][];
  // Array with only 0 and 1. If a card is yet to be played, the value at index in the array of the corresponding card value is 1 otherwise it's 0.
  public cardsLeft: number[];

  constructor(deck: Deck) {
    this.cardsLeft = new Array(105).fill(1);
    this.rows = Array.from({ length: NUMBER_OF_ROWS }, () => [] as Card[]);
    for (let i = 0; i < NUMBER_OF_ROWS; i++) {
      const drawnCard = deck.drawCard()
      this.rows[i].push(drawnCard);
      this.cardsLeft[drawnCard.value] = 0;
    }
  }

  public putCardOnBoard(card: Card, player: Player): void {
    let lowestDiff = Infinity;
    let targetRowIndex = -1;
    for (let row of this.rows) {
      const lastCardInRow = row[row.length - 1];
      const diff = card.value - lastCardInRow.value;
      if (diff > 0 && diff < lowestDiff) {
        lowestDiff = diff;
        targetRowIndex = this.rows.indexOf(row);
      }
    }
    // In case the card value is lower than any last card on the board
    if (targetRowIndex === -1) {
      // Player must pick a row
      const chosenRowIndex = player.pickRow(this.rows);
      const chosenRow = this.rows[chosenRowIndex];
      const pointsToAdd = chosenRow.reduce((sum, card) => sum + card.points, 0);
      player.addPoints(pointsToAdd);
      this.rows[chosenRowIndex] = [card];
      return;
    }
    const targetRow = this.rows[targetRowIndex];
    if (targetRow.length < 5) {
      targetRow.push(card);
    } else {
      // Row is full, player must take this row
      const pointsToAdd = targetRow.reduce((sum, card) => sum + card.points, 0);
      player.addPoints(pointsToAdd);
      this.rows[targetRowIndex] = [card];
    }
    this.cardsLeft[card.value] = 0;
  }
}
