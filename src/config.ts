import * as strategies from "./strategies";
import { Strategy } from "./types";

export const ROUNDS_PER_GAME = 100;
export const NUMBER_OF_TOURNAMENTS = 10;
export const PLAYERS_PER_STRATEGY = 10;
export const NOISE = 0.02;
export const STRATEGIES: Strategy[] = [
  strategies.ALWAYS_COOPERATE,
  strategies.ALWAYS_DEFECT,
  strategies.TIT_FOR_TAT,
  strategies.TIT_FOR_TAT_FORGIVING,
  strategies.RANDOM_CHOICE,
];
