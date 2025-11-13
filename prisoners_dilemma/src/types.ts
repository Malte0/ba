
export type Strategy = {
    name: string;
    description: string;
    costMatrix: number[][];
    cooperates: (opponentHistory: boolean[]) => boolean;
}

export type Player = {
  id: number;
  strategy: Strategy;
  history: boolean[];
  totalCost: number;
};