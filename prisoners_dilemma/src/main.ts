import { NUMBER_OF_TOURNAMENTS, PLAYERS_PER_STRATEGY, ROUNDS_PER_GAME, STRATEGIES } from "./config";
import { Player } from "./types";

function instantiatePlayers() {
  const players: Player[] = [];
  let playerId = 0;

  // Create players
  for (const strategy of STRATEGIES) {
    for (let i = 0; i < PLAYERS_PER_STRATEGY; i++) {
      players.push({
        id: playerId++,
        strategy: strategy,
        history: [],
        totalCost: 0,
      });
    }
  }
  return players;
}

function playRound(playerA: Player, playerB: Player) {
  const aCooperates = playerA.strategy.cooperates(playerB.history);
  const bCooperates = playerB.strategy.cooperates(playerA.history);
  // Update histories
  playerA.history.push(aCooperates);
  playerB.history.push(bCooperates);
  // Update costs based on cost matrix
  const costMatrixA = playerA.strategy.costMatrix;
  const costMatrixB = playerB.strategy.costMatrix;
  const aCost = costMatrixA[aCooperates ? 0 : 1][bCooperates ? 0 : 1];
  const bCost = costMatrixB[bCooperates ? 0 : 1][aCooperates ? 0 : 1];
  playerA.totalCost += aCost;
  playerB.totalCost += bCost;
}

function runTournament() {
  const players = instantiatePlayers();
  // Each player plays against every other player
  for (let i = 0; i < players.length; i++) {
    for (let j = i + 1; j < players.length; j++) {
      const playerA = players[i];
      const playerB = players[j];
      // Reset histories for new match
      playerA.history = [];
      playerB.history = [];
      for (let round = 0; round < ROUNDS_PER_GAME; round++) {
        playRound(playerA, playerB);
      }
    }
  }

  const strategyCosts: { [key: string]: number } = {};
  // Aggregate costs by strategy
  for (const player of players) {
    if (!strategyCosts[player.strategy.name]) {
      strategyCosts[player.strategy.name] = 0;
    }
    strategyCosts[player.strategy.name] += player.totalCost;
  }
  // Divide by cost of best strategy
  // @ts-ignore
  const leastCost = Math.min(...Object.values(strategyCosts));
  for (const strategyName in strategyCosts) {
    strategyCosts[strategyName] =
      Math.round((strategyCosts[strategyName] / leastCost) * 100) / 100;
  }
  return strategyCosts;
}

function main() {
  const strategyCosts: { [key: string]: number[] } = {};
  for (let t = 0; t < NUMBER_OF_TOURNAMENTS; t++) {
    const results = runTournament();
    for (const strategyName in results) {
      if (!strategyCosts[strategyName]) {
        strategyCosts[strategyName] = [];
      }
      strategyCosts[strategyName].push(results[strategyName]);
    }
  }
  const finalCosts: { [key: string]: number } = {};
  // Calculate average costs
  for (const strategyName in strategyCosts) {
    const costs = strategyCosts[strategyName];
    const avgCost =
      Math.round((costs.reduce((a, b) => a + b, 0) / costs.length) * 100) / 100;
    finalCosts[strategyName] = avgCost;
  }
  console.table(finalCosts);
}

main();
