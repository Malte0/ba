import { Game } from "./game";
import { Player } from "./player";
import * as strategies from "./strategies";
import * as fs from "fs";

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

function writeResultToFile(
  results: {
    [key: string]: number;
  },
  testValue: number
) {
  const file = "./results.txt";
  let content = fs.readFileSync(file, "utf-8");
  const testValues = content.split("\n");
  let outPerforms = 0;
  for (const result in results) {
    if (result !== "Middle") {
      outPerforms += results[result] - 1;
    }
  }
  if (testValues.length > 99) {
    const currentValue = Number(testValues[testValue-1]);
    testValues[testValue-1] = `${Math.round(((currentValue + outPerforms) / 2) * 100) / 100}`;
    fs.writeFileSync(file, testValues.join("\n"), "utf-8");
  } else {
    fs.writeFileSync(file, content+`${Math.round(outPerforms * 100) / 100}\n`, "utf-8")
  }

}

function main(testValue: number) {
  const players: Player[] = [
    new Player("Random", strategies.RANDOM),
    new Player("Highest", strategies.HIGHEST_CARD),
    new Player("Middle", strategies.KEEP_MIDDLE(testValue)),
    new Player("Lowest", strategies.LOWEST_CARD),
  ];
  for (let i = 0; i < NUMBER_OF_GAMES; i++) {
    playGame(players);
  }
  const lowestScore = Math.min(...Object.keys(results).map((key) => results[key]));
  for (const result in results) {
    results[result] = Math.round((results[result] / lowestScore) * 100) / 100;
  }
  // console.table(results);
  writeResultToFile(results, testValue);
}


const numberOfTestRuns = 20;
for (let j = 0; j < numberOfTestRuns; j++) {
  for (let i = 1; i < 101; i++) {
    main(i);
  }
}
