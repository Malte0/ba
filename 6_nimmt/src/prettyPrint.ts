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
    devider += middleCorner + "".padStart(STANDARD_COLUMN_WIDTH+2, "─");
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
  // Sort scores descending
  let sortedScores: [string, number][] = [];
  for (const playerName in results) {
    sortedScores.push([playerName, results[playerName]]);
  }
  sortedScores.sort((a, b) => {
    return a[1] - b[1];
  });
  // print results
  console.log("Game Results:");
  const COLUMN_COUNT = 2;
  const LONGEST_NAME_LENGTH = sortedScores
    .map((pair) => pair[0].length)
    .reduce((prev, curr) => Math.max(prev, curr), 0);
  const LONGEST_RESULT_LENGTH = sortedScores
    .map((pair) => pair[1].toString().length)
    .reduce((prev, curr) => Math.max(prev, curr), 0);

  // +2 because of spaces left and right of name
  drawDevider(LONGEST_NAME_LENGTH + 2, COLUMN_COUNT, "┌", "┬", "┐");
  for (let i = 0; i < sortedScores.length; i++) {
    const playerName = sortedScores[i][0];
    const nameFormatted = playerName.padStart(LONGEST_NAME_LENGTH, " ");
    const scoreFormatted = results[playerName]
      .toString()
      .padEnd(Math.max(LONGEST_RESULT_LENGTH, STANDARD_COLUMN_WIDTH), " ");
    console.log(`│ ${nameFormatted} │ ${scoreFormatted} │`);

    // if playerName is the last name in the list
    if (i === sortedScores.length - 1) {
      drawDevider(LONGEST_NAME_LENGTH + 2, COLUMN_COUNT, "└", "┴", "┘");
      return;
    }
    drawDevider(LONGEST_NAME_LENGTH + 2, COLUMN_COUNT, "├", "┼", "┤");
  }
}
