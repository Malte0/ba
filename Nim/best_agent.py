# Task:
# Send an agent into a tournament of Nim
# depending on the price and the computation cost, what is the best agent to send?

import matplotlib.pyplot as plt
from game import create_T, play_tournament
import random

from players import Player

N = 100
K = 8
EXPTECTED_ROUNDS = N // (K // 2)
NUMBER_OF_GAMES_PER_MATCH = 1000
NUMBER_OF_PLAYERS_IN_TOURNAMENT = 10
AVG_OPPONENT_STRENGTH = 0.5 # linear mean shift from baseline to N in [0, 1]
SIGMA_SCALE = 0.5 # gaussian spread for opponent thinking steps

# craetes players with thinking steps gaussian distributed around a mean that is linearly shifted by the average opponent strength
def create_tournament_players():
    # Baseline is the "minimum strong" level; strength=1 pushes mean close to N.
    baseline_thinking_steps = N - EXPTECTED_ROUNDS
    strength = max(0.0, min(1.0, AVG_OPPONENT_STRENGTH))
    mean_thinking_steps = baseline_thinking_steps + strength * (N - baseline_thinking_steps)
    sigma = max(1, int((N - baseline_thinking_steps) * SIGMA_SCALE))
    thinking_steps = [
        max(0, min(N, int(round(random.gauss(mean_thinking_steps, sigma)))))
        for _ in range(NUMBER_OF_PLAYERS_IN_TOURNAMENT)
    ]
    return [Player(steps) for steps in thinking_steps]  

def main():
    opponents = create_tournament_players()
    

if __name__ == "__main__":
    main()


# run convergence nim with non perfect player