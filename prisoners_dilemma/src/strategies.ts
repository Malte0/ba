import { NOISE } from "./config";
import { DEFAULT_COST_MATRIX } from "./costMatrix";
import { Strategy } from "./types";

export const RANDOM_CHOICE: Strategy = {
    name: "Random Choice",
    description: "This strategy randomly cooperates or defects.",
    costMatrix: DEFAULT_COST_MATRIX,
    cooperates: (opponentHistory: boolean[]) => {
        return Math.random() < 0.5 ? true : false;
    },
};

export const ALWAYS_COOPERATE: Strategy = {
  name: "Always Cooperate",
  description: "This strategy always cooperates.",
  costMatrix: DEFAULT_COST_MATRIX,
  cooperates: (opponentHistory: boolean[]) => {
    return Math.random() < NOISE ? false : true;
  },
};

export const ALWAYS_DEFECT: Strategy = {
  name: "Always Defect",
  description: "This strategy always defects.",
  costMatrix: DEFAULT_COST_MATRIX,
  cooperates: (opponentHistory: boolean[]) => {
    return Math.random() < NOISE ? true : false;
  },
};

export const TIT_FOR_TAT: Strategy = {
  name: "Tit for Tat",
  description:
    "First round cooperate, afterwards do what opponent did last turn",
  costMatrix: DEFAULT_COST_MATRIX,
  cooperates: (OpponentHistory: boolean[]) => {
    const result = OpponentHistory.length > 0 ? OpponentHistory[0] : true
    return Math.random() < NOISE ? !result : result;
  },
};

export const TIT_FOR_TAT_FORGIVING: Strategy = {
  name: "Tit for Tat Forgiving",
  description:
    "Same as Tit for Tat, but sometimes still cooperates when opponent defects",
  costMatrix: DEFAULT_COST_MATRIX,
  cooperates: (opponentHistory: boolean[]) => {
    const PROB_TO_FORGIVE = 0.2;
    let result = true
    if (opponentHistory.length > 0) {
      result = Math.random() < PROB_TO_FORGIVE ? true : opponentHistory[0];
    }
    return Math.random() < NOISE ? !result : result;
  },
};
