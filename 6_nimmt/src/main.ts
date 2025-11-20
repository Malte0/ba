import { Game } from "./game";
import { Player } from "./player";
import { playManually } from "./manualPlay";
import * as strategies from "./strategies";
import config from "./config";
import { prettyPrintResults } from "./prettyPrint";
import { writeResultToFile } from "./writeToFile";

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

function main(unreliability: number, i: number) {
  if (config.Manual_Play) {
    playManually();
    return;
  }
  const players: Player[] = [
    new Player("Random", strategies.RANDOM),
    new Player("Highest first", strategies.HIGHEST_CARD),
    // new Player("Unreliable", strategies.UNRELIABLE(unreliability)),
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
  writeResultToFile(results, unreliability, i, "Unreliable", "results.txt");
  prettyPrintResults(results);
}

// for (let i = 0; i <= 10; i++) {
//   const unreliability = i / 100;
//   console.log(`Iteration ${i}`);
//   for (let j = 0; j < 10; j++) {
//     main(unreliability, i);
//   }
// }
// console.log("DONE");

main(1,1)