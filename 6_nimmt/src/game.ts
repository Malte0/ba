import { Board } from "./board";
import { Deck } from "./deck";
import { Player } from "./player";
import { Card } from "./types";

export class Game {
  private players: Player[];
  private board: Board;
  private deck: Deck;

  constructor(players: Player[]) {
    this.players = players;
    this.resetGame();
  }

  public playersHaveCardsInHand(): boolean {
    return this.players.some((player) => player.hasCards());
  }

  public printBoardState(): void {
    const valuesFormatted = this.board.rows.map(row => row.map(card => card.value));
    console.table(valuesFormatted);
  }

  public printScore(): void {
    console.log("Current Scores:");
    this.players.forEach(player => {
      console.log(`${player.name}: ${player.points} points`);
    });
  }

  public getScores(): {[key: string]: number} {
    const scores: {[key: string]: number} = {}
    this.players.forEach(player => {
      scores[player.name] = player.points;
    });
    return scores
  }

  public resetGame(): void {
    this.deck = new Deck()
    this.board = new Board(this.deck);
    for(const player of this.players) {
      player.drawCards(this.deck);
    }
  }

  private putCardOnBoard(card: Card, player: Player): void {
    let lowestDiff = Infinity;
    let targetRowIndex = -1;
    for (let row of this.board.rows) {
        const lastCardInRow = row[row.length - 1];
        const diff = card.value - lastCardInRow.value;
        if (diff > 0 && diff < lowestDiff) {
            lowestDiff = diff;
            targetRowIndex = this.board.rows.indexOf(row);
        }
    }
    // In case the card value is lower than any last card on the board
    if (targetRowIndex === -1) {
        // Player must pick a row
        const chosenRowIndex = player.pickRow(this.board.rows);
        const chosenRow = this.board.rows[chosenRowIndex];
        const pointsToAdd = chosenRow.reduce((sum, card) => sum + card.points, 0);
        player.addPoints(pointsToAdd);
        this.board.rows[chosenRowIndex] = [card];
        return;
    }
    const targetRow = this.board.rows[targetRowIndex];
    if (targetRow.length < 5) {
        targetRow.push(card);
    } else {
        // Row is full, player must take this row
        const pointsToAdd = targetRow.reduce((sum, card) => sum + card.points, 0);
        player.addPoints(pointsToAdd);
        this.board.rows[targetRowIndex] = [card];
    }
  }

  public playRound(): void {
    const playedCards = this.players.map((player: Player) => ({
      player,
      card: player.playCard(),
    }));
    playedCards.sort((a, b) => a.card.value - b.card.value);
    for (const { player, card } of playedCards) {
      this.putCardOnBoard(card, player);
    }
  }
}
