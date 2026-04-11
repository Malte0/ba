# Task:
# Send an agent into a tournament of Nim
# depending on the price and the computation cost, what is the best agent to send?

import matplotlib.pyplot as plt
from game import create_T, play_tournament
import random
from players import Player
import time

N = 100
K = 8
EXPTECTED_ROUNDS = N // (K // 2)
NUMBER_OF_GAMES_PER_MATCH = 20
NUMBER_OF_PLAYERS_IN_TOURNAMENT = 10
AVG_OPPONENT_STRENGTH = 0.5 # linear mean shift from baseline to N in [0, 1]
SIGMA_SCALE = 0.5 # gaussian spread for opponent thinking steps

WINNING_PRICE = 1_000 # Euro
COST_FACTOR = 0.05
# ALPHA = 0.5 # weight for win rate vs cost in reward calculation

def cost_of_thinking(computation_steps):
    x = (computation_steps // N) ** 2
    return x * COST_FACTOR

def reward_for_winning(thinking_steps):
    # Example reward function: linear reward for winning with fewer thinking steps
    return max(0, N - thinking_steps)

# craetes players with thinking steps gaussian distributed around a mean that is linearly shifted by the average opponent strength
def create_opponents():
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

# x-axis: thinking steps, y-axis: reward
def plot_results(thinking_steps, rewards):
    plt.figure(figsize=(10, 6))
    plt.plot(thinking_steps, rewards, marker='o')
    plt.title('Reward vs Thinking Steps')
    plt.xlabel('Thinking Steps')
    plt.ylabel('Reward')
    plt.grid()
    plt.show()
    

def main():
    win_rates = {}
    cost_results = {}
    opponents = create_opponents()
    test_thinking_steps = [i for i in range(N - EXPTECTED_ROUNDS, N + 1) if not any(player.thinking_steps == i for player in opponents)]
    iteration_count = len(test_thinking_steps)
    start_time = time.perf_counter()
    for iteration_index, test_player_thinking_steps in enumerate(test_thinking_steps, start=1):
        iteration_start = time.perf_counter()
        test_player = Player(test_player_thinking_steps)
        players = opponents + [test_player]
        results, games_played, thinking_times, computation_steps = play_tournament(players, N, K, NUMBER_OF_GAMES_PER_MATCH)
        avg_computation_steps = {player.thinking_steps: computation_steps.get(player.thinking_steps, 0) / games_played.get(player.thinking_steps, 1) for player in players}
        win_rates[test_player_thinking_steps] = results.get(test_player_thinking_steps, 0) / games_played.get(test_player_thinking_steps, 1)
        cost_results[test_player_thinking_steps] = cost_of_thinking(avg_computation_steps[test_player_thinking_steps])
        iteration_duration = time.perf_counter() - iteration_start
        elapsed_time = time.perf_counter() - start_time
        estimated_total_time = elapsed_time / iteration_index * iteration_count
        remaining_time = estimated_total_time - elapsed_time
        print(
            f"Iteration {iteration_index}/{iteration_count} took {iteration_duration:.2f}s; "
            f"elapsed {elapsed_time:.2f}s; estimated total {estimated_total_time:.2f}s; "
            f"remaining {max(0.0, remaining_time):.2f}s"
        )
    rewards = [win_rates.get(steps, 0) * WINNING_PRICE - cost_results.get(steps, 0) for steps in test_thinking_steps]
    # but with winrates?
    print(win_rates)
    print(cost_results)
    plot_results(test_thinking_steps, rewards)

if __name__ == "__main__":
    main()


# run convergence nim with non perfect player