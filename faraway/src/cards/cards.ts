import type { COLOR, CARD, SYMBOL } from "../types";

export class CardDeck {
  cardsLeft = Array.from({ length: 68 }, (_e, i) => i + 1);

  drawRegion() {
    const indexChoice = Math.floor(Math.random() * this.cardsLeft.length); // 0-cardsLeft.length
    const chosenCard = this.cardsLeft[indexChoice];
    this.cardsLeft = this.cardsLeft.filter((card) => card != this.cardsLeft[indexChoice]);
    return chosenCard;
  }
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
    colorCount[openCard.color] += 1;
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
    symbolsInCondition[symbol] = symbolsInCondition[symbol] ? symbolsInCondition[symbol]+1 : 1;
  }
  // check if it occurs fewer times
  for (const symbol of Object.keys(symbolsInCondition)) {
    const symbolCount = countSymbol(symbol as SYMBOL, openRegions);
    if (symbolCount < symbolsInCondition[symbol]) {
      return false
    }
  }
  return true;
}

export function getCardPoints(openRegions: CARD[], regionToGetPointsOf: CARD) {
  //, openSanctuaries
  if (!regionToGetPointsOf.points) {
    return 0;
  }
  if (regionToGetPointsOf.condition && !isConditionFullfilled(openRegions, regionToGetPointsOf.condition)) {
    return 0;
  }
  const basePoints = regionToGetPointsOf.points;
  const pointsMultiplier = regionToGetPointsOf.multiplier;
  if (!pointsMultiplier) {
    return basePoints;
  }
  switch (pointsMultiplier) {
    case "map":
      let numberOfMaps = 0;
      for (const openRegion of openRegions) {
        numberOfMaps += openRegion.map ? 1 : 0;
      }
      return numberOfMaps * basePoints;
    case "night":
      let numberOfNights = 0;
      for (const openRegion of openRegions) {
        numberOfNights += openRegion.night ? 1 : 0;
      }
      return numberOfNights * basePoints;
    case "Stein":
      return countSymbol("Stein", openRegions) * basePoints;
    case "Schimaere":
      return countSymbol("Schimaere", openRegions) * basePoints;
    case "Distel":
      return countSymbol("Distel", openRegions) * basePoints;
    case "color-set":
      return countColorSets(openRegions) * basePoints;
    default:
      // in this case it's always a color counter
      const colorsToCount = regionToGetPointsOf.multiplier;
      return countColors(colorsToCount as COLOR[], openRegions) * basePoints;
  }
}
