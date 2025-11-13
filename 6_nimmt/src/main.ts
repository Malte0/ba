import { Game } from "./game";
import { Player } from "./player";
import * as strategies from "./strategies";

const results: { [key: string]: number } = {};
const NUMBER_OF_GAMES = 10000;

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

function main() {
  const players: Player[] = [
    new Player("Emilia", strategies.RANDOM),
    new Player("Leo", strategies.HIGHEST_CARD),
    new Player("Clara", strategies.RANDOM),
    new Player("Donavan", strategies.LOWEST_CARD),
  ];
  for (let i = 0; i < NUMBER_OF_GAMES; i++) {
    playGame(players);
  }
  const lowestScore = Math.min(...Object.keys(results).map((key) => results[key]));
  for (const result in results) {
    results[result] = Math.round((results[result] / lowestScore) * 100) / 100;
  }
  console.table(results);
}

main();
