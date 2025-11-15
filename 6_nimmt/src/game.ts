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
    const valuesFormatted = this.board.rows.map((row) => row.map((card) => card.value));
    console.table(valuesFormatted);
  }

  public printScore(): void {
    console.log("Current Scores:");
    this.players.forEach((player) => {
      console.log(`${player.name}: ${player.points} points`);
    });
  }

  public getScores(): { [key: string]: number } {
    const scores: { [key: string]: number } = {};
    this.players.forEach((player) => {
      scores[player.name] = player.points;
    });
    return scores;
  }

  public resetGame(): void {
    this.deck = new Deck();
    this.board = new Board(this.deck);
    for (const player of this.players) {
      player.drawCards(this.deck);
    }
  }

  public playRound(): void {
    const playedCards = this.players.map((player: Player) => ({
      player,
      card: player.playCard(this.board.rows, this.board.cardsLeft, this.players.length),
    }));
    playedCards.sort((a, b) => a.card.value - b.card.value);
    for (const { player, card } of playedCards) {
      this.board.putCardOnBoard(card, player);
    }
  }
}
