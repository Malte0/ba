import { Game } from "./game";
import { Strategy } from "./strategy";

const NUMBER_OF_PLAYERS = 4;

function main() {
    const game: Game = new Game(NUMBER_OF_PLAYERS);
    while (game.playersHaveCardsInHand()) {
        game.playRound();
        game.printBoardState();
    }
    game.printScore();
}

main();