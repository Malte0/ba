import { Deck } from "./deck";
import { Strategy } from "./strategy";
import { Card } from "./types";

const NUMBER_OF_CARDS_IN_HAND = 10;

export class Player {
  public name: string;
  private hand: Card[];
  public points: number;
  private strategy: Strategy;

  constructor(name: string, strategy: Strategy) {
    this.name = name;
    this.strategy = strategy;
    this.reset();
  }

  public drawCards(deck: Deck): void {
    this.hand = [];
    for (let i = 0; i < NUMBER_OF_CARDS_IN_HAND; i++) {
      this.hand.push(deck.drawCard());
    }
  }

  public reset(): void {
    this.hand = [];
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
    const cardToPlay = this.hand.splice(cardIndexToPlay, 1)[0];
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
