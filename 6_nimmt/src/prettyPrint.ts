import { Card } from "./types";

const MAX_ROW_LENGTH = 5;
const STANDARD_COLUMN_WIDTH = 4;

function drawDevider(
  firstColumnWidth: number, // width of the first column
  deviderCount: number,
  startCorner: string,
  middleCorner: string,
  endCorner: string
) {
  let devider = startCorner + "".padStart(firstColumnWidth, "─");
  for (let i = 1; i <= deviderCount; i++) {
    if (i === deviderCount) {
      devider += endCorner;
      break;
    }
    devider += middleCorner + "────";
  }
  console.log(devider);
}

export function prettyPrintBoard(cardsOnBoard: Card[][]) {
  console.log("Cards on Table:");
  drawDevider(STANDARD_COLUMN_WIDTH, MAX_ROW_LENGTH, "┌", "┬", "┐");
  for (const row of cardsOnBoard) {
    let rowContent = "│";
    for (let i = 0; i < MAX_ROW_LENGTH; i++) {
      if (i < row.length) {
        rowContent += " " + `${row[i].value}`.padStart(2, "0") + " │";
      } else {
        rowContent += "    │";
      }
    }
    console.log(rowContent);
    if (cardsOnBoard.indexOf(row) === cardsOnBoard.length - 1) break;
    drawDevider(STANDARD_COLUMN_WIDTH, MAX_ROW_LENGTH, "├", "┼", "┤");
  }
  drawDevider(STANDARD_COLUMN_WIDTH, MAX_ROW_LENGTH, "└", "┴", "┘");
}

export function prettyPrintHandCards(handCards: Card[]) {
  console.log("Cards in hand:");
  drawDevider(STANDARD_COLUMN_WIDTH, handCards.length, "┌", "┬", "┐");
  let cardString = "│";
  for (let i = 0; i < handCards.length; i++) {
    if (i < handCards.length) {
      cardString += " " + `${handCards[i].value}`.padStart(2, " ") + " │";
    } else {
      cardString += "    │";
    }
  }
  console.log(cardString);
  drawDevider(STANDARD_COLUMN_WIDTH, handCards.length, "└", "┴", "┘");
}

export function prettyPrintResults(results: { [key: string]: number }) {
    
  console.log("Game Results:");
  const COLUMN_COUNT = 2;
  const LONGEST_NAME_LENGTH = Object.keys(results)
  .map((key) => key.length)
  .reduce((prev, curr) => Math.max(prev, curr), 0);
  const LONGEST_RESULT_LENGTH = Object.values(results).map(val => val.toString().length).reduce((prev, curr) => Math.max(prev, curr), 0);
  
  // +2 because of spaces left and right of name
  drawDevider(LONGEST_NAME_LENGTH+2, COLUMN_COUNT, "┌", "┬", "┐");
  for ( let i = 0; i < Object.keys(results).length; i++) {
    const playerName = Object.keys(results)[i];
    console.log(
      `│ ${playerName.padStart(LONGEST_NAME_LENGTH, " ")} │ ${results[
        playerName
      ]
        .toString()
        .padEnd(LONGEST_RESULT_LENGTH, " ")} │`
    );

    // if playerName is the last name in the list
    if (
      i === Object.keys(results).length-1
    ) {
      drawDevider(LONGEST_NAME_LENGTH+2, COLUMN_COUNT, "└", "┴", "┘");
      return;
    }
    drawDevider(LONGEST_NAME_LENGTH+2, COLUMN_COUNT, "├", "┼", "┤");
  }
}
