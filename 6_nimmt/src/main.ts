import { Game } from "./game";
import { Player } from "./player";
import { playManually } from "./manualPlay";
import * as strategies from "./strategies";
import config from "./config";
import { prettyPrintResults } from "./prettyPrint";

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

function main() {
  if (config.Manual_Play) {
    playManually();
    return;
  }
  const players: Player[] = [
    new Player("Random", strategies.RANDOM),
    new Player("Highest first", strategies.HIGHEST_CARD),
    new Player("Lowest first", strategies.LOWEST_CARD),
    new Player("Middle", strategies.KEEP_MIDDLE),
    new Player("Safe Memory", strategies.SAFE_WITH_MEMORY),
  ];
  for (let i = 0; i < config.Number_of_Games; i++) {
    playGame(players);
  }
  const lowestScore = Math.min(...Object.keys(results).map((key) => results[key]));
  for (const result in results) {
    results[result] = Math.round((results[result] / lowestScore) * 100) / 100;
  }
  prettyPrintResults(results);
}

main();
