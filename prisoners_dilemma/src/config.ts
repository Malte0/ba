import * as strategies from "./strategies";
import { Strategy } from "./types";

export const ROUNDS_PER_GAME = 1000;
export const NUMBER_OF_TOURNAMENTS = 10;
export const PLAYERS_PER_STRATEGY = 10;
export const NOISE = 0.02;
export const STRATEGIES: Strategy[] = [
  strategies.ALWAYS_COOPERATE,
  strategies.TIT_FOR_TAT,
  strategies.TIT_FOR_TAT_FORGIVING,
];
