import { Game } from "./game";
import { Player } from "./player";
import { prettyPrintBoard, prettyPrintHandCards, prettyPrintResults } from "./prettyPrint";
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
  prettyPrintResults(results);
}

const REAL_PLAYER: Strategy = {
  name: "Real Player",
  description: "Play yourself",
  cardToPlay: (handCards: Card[], cardsOnBoard: Card[][]) => {
    if (handCards.length == 1) {
      return 0;
    }
    prettyPrintBoard(cardsOnBoard);
    prettyPrintHandCards(handCards);
    let indexToPlay = -1;
    while (indexToPlay === -1) {
      let cardToPlay = Number(prompt("Card to play: "));
      indexToPlay = handCards.map((card) => card.value).indexOf(cardToPlay);
    }
    return indexToPlay;
  },
};
