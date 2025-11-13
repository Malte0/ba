import { Board } from "./board";
import { Deck } from "./deck";
import { Player } from "./player";
import { Card } from "./types";

const some_random_names = [
  "Emilia",
  "Leo",
  "Clara",
  "Noah",
  "Mia",
  "Donavan",
  "Sophia",
  "Barbara",
  "Olivia",
  "Pascal",
];

export class Game {
  private players: Player[];
  private board: Board;
  private deck: Deck;
  private numberOfPlayers: number;

  constructor(numberOfPlayers: number) {
    this.numberOfPlayers = numberOfPlayers;
    this.resetGame();
  }

  public playersHaveCardsInHand(): boolean {
    return this.players.some((player) => player.hand.length > 0);
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

  public resetGame(): void {
    this.deck = new Deck();
    this.board = new Board(this.deck);
    this.players = [];
    for (let i = 0; i < this.numberOfPlayers; i++) {
      const playerName = some_random_names[i % some_random_names.length];
      this.players.push(new Player(playerName, this.deck));
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
    const playedCards = this.players.map((player) => ({
      player,
      card: player.playCard(),
    }));
    playedCards.sort((a, b) => a.card.value - b.card.value);
    for (const { player, card } of playedCards) {
      this.putCardOnBoard(card, player);
    }
  }
}
