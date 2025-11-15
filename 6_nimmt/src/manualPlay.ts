import { Game } from "./game";
import { Player } from "./player";
import * as strategies from "./strategies";

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
    new Player("You", strategies.REAL_PLAYER),
    new Player("Safe Memory 2", strategies.SAFE_WITH_MEMORY),
    new Player("Middle", strategies.KEEP_MIDDLE),
    new Player("Safe Memory", strategies.SAFE_WITH_MEMORY),
  ];
  playGame(players); 
  console.table(results);
}
