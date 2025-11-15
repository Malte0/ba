import { Game } from "./game";
import { Player } from "./player";
import * as strategies from "./strategies";
import { Card, Strategy } from "./types";
const prompt = require("prompt-sync")({ sigint: true });

const results: { [key: string]: number } = {};

function playGame(players: Player[]) {
  for (const player of players) {
    player.reset();
  }
  const game: Game = new Game(players);
  while (game.playersHaveCardsInHand()) {
    game.playRound();
    // game.printBoardState();
  }
  const scores = game.getScores();
  for (const player in scores) {
    if (results[player]) {
      results[player] += scores[player];
    } else {
      results[player] = scores[player];
    }
  }
}

export function playManually() {
  const players: Player[] = [
    new Player("You", REAL_PLAYER),
    new Player("Safe Memory 2", strategies.SAFE_WITH_MEMORY),
    new Player("Middle", strategies.KEEP_MIDDLE),
    new Player("Safe Memory", strategies.SAFE_WITH_MEMORY),
  ];
  playGame(players); 
  console.table(results);
}

const REAL_PLAYER: Strategy = {
  name: "Real Player",
  description: "Play yourself",
  cardToPlay: (handCards: Card[], cardsOnBoard: Card[][]) => {
    if (handCards.length == 1) {
      return 0;
    }
    console.log("Cards on Board:");
    console.table(cardsOnBoard.map(row => row.map(card => card.value)));
    console.log("These are the Cards you can Play:");
    console.table(handCards.map(card => card.value));
    let indexToPlay = Number(prompt("Index to play: "));
    return indexToPlay;
  },
};