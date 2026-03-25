import type { COLOR, CARD, SYMBOL } from "../types";

const NUMBER_OF_REGIONS = 68;
const NUMBER_OF_SANCTUARIES = 45;

export class CardDeck {
  cardsLeft = Array.from({ length: NUMBER_OF_REGIONS }, (_e, i) => i + 1);
  sanctuaryPile: number[] = shuffle(Array.from({ length: NUMBER_OF_SANCTUARIES }, (_e, i) => i + 1));

  drawSanctuaries(amountToDraw: number) {
    // take the top amountToDraw cards
    const drawnSanctuaries = this.sanctuaryPile.splice(0, amountToDraw);
    // unused sanctuaries are put back under the pile
    // remove the chosen card later
    this.sanctuaryPile.concat(drawnSanctuaries);
    return drawnSanctuaries;
  }

  takeSanctuary(sanctuaryIndex: number) {
    this.sanctuaryPile = this.sanctuaryPile.filter((cardIndex) => cardIndex != sanctuaryIndex);
  }

  drawRegion() {
    const indexChoice = Math.floor(Math.random() * this.cardsLeft.length); // 0-cardsLeft.length
    const chosenCard = this.cardsLeft[indexChoice];
    // unused regions are removed from the game
    this.cardsLeft = this.cardsLeft.filter((card) => card != this.cardsLeft[indexChoice]);
    return chosenCard;
  }
}

// in-place shuffle function
function shuffle(array: any[]) {
  let currentIndex = array.length;
  while (currentIndex != 0) {
    let randomIndex = Math.floor(Math.random() * currentIndex);
    currentIndex--;
    [array[currentIndex], array[randomIndex]] = [array[randomIndex], array[currentIndex]];
  }
  return array;
}

function countSymbol(symbolToCount: SYMBOL, openRegions: CARD[]) {
  let numberOfStein = 0;
  for (const openRegion of openRegions) {
    numberOfStein += openRegion.symbols ? openRegion.symbols.filter((symbol) => symbol === symbolToCount).length : 0;
  }
  return numberOfStein;
}

function countColorSets(openCards: CARD[]) {
  const colorCount: { [key: string]: number } = {
    red: 0,
    blue: 0,
    yellow: 0,
    green: 0,
  };

  for (const openCard of openCards) {
    if (openCard.color !== "none") {
      colorCount[openCard.color] += 1;
    }
  }

  return Math.min(...Object.values(colorCount));
}

function countColors(colorsToCount: COLOR[], openRegions: CARD[]) {
  let colorCount = 0;
  for (const openRegion of openRegions) {
    colorCount += colorsToCount.includes(openRegion.color) ? 1 : 0;
  }
  return colorCount;
}

function isConditionFullfilled(openRegions: CARD[], condition: SYMBOL[]) {
  // count how many times a SYMBOL has to occur
  const symbolsInCondition: { [key: string]: number } = {};
  for (const symbol of condition) {
    symbolsInCondition[symbol] = symbolsInCondition[symbol] ? symbolsInCondition[symbol] + 1 : 1;
  }
  // check if it occurs fewer times
  for (const symbol of Object.keys(symbolsInCondition)) {
    const symbolCount = countSymbol(symbol as SYMBOL, openRegions);
    if (symbolCount < symbolsInCondition[symbol]) {
      return false;
    }
  }
  return true;
}

function countNights(openCards: CARD[]) {
  let numberOfNights = 0;
  for (const openRegion of openCards) {
    numberOfNights += openRegion.night ? 1 : 0;
  }
  return numberOfNights;
}

export function countMaps(openCards: CARD[]) {
  let numberOfMaps = 0;
  for (const openCard of openCards) {
    numberOfMaps += openCard.map ? 1 : 0;
  }
  return numberOfMaps;
}

export function getCardPoints(openCards: CARD[], regionToGetPointsOf: CARD) {
  //, openSanctuaries
  if (!regionToGetPointsOf.points) {
    return 0;
  }
  if (regionToGetPointsOf.condition && !isConditionFullfilled(openCards, regionToGetPointsOf.condition)) {
    return 0;
  }
  const basePoints = regionToGetPointsOf.points;
  const pointsMultiplier = regionToGetPointsOf.multiplier;
  if (!pointsMultiplier) {
    return basePoints;
  }
  switch (pointsMultiplier) {
    case "map":
      return countMaps(openCards) * basePoints;
    case "night":
      return countNights(openCards) * basePoints;
    case "Stein":
      return countSymbol("Stein", openCards) * basePoints;
    case "Schimaere":
      return countSymbol("Schimaere", openCards) * basePoints;
    case "Distel":
      return countSymbol("Distel", openCards) * basePoints;
    case "color-set":
      return countColorSets(openCards) * basePoints;
    default:
      // in this case it's always a color counter
      const colorsToCount = regionToGetPointsOf.multiplier;
      return countColors(colorsToCount as COLOR[], openCards) * basePoints;
  }
}
