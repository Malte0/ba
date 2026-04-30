# Task:
# Send an agent into a tournament of Nim
# depending on the price and the computation cost, what is the best agent to send?

import matplotlib.pyplot as plt
from game import play_tournament
import random
from players import Player

N = 100
K = 8
NUMBER_OF_GAMES_PER_MATCH = 10
NUMBER_OF_ITERATIONS = 1
NUMBER_OF_PLAYERS_IN_TOURNAMENT = 10
EXPTECTED_ROUNDS = N // (K // 2)
SIGMA_SCALE = 0.5 # gaussian spread for opponent thinking steps

COST_FACTOR = 0.05
# ALPHA = 0.5 # weight for win rate vs cost in reward calculation

def cost_of_thinking(computation_steps):
    x = (computation_steps // N) ** 2
    return x * COST_FACTOR

def reward_for_winning(thinking_steps):
    # Example reward function: linear reward for winning with fewer thinking steps
    return max(0, N - thinking_steps)

# craetes players with thinking steps gaussian distributed around a mean that is linearly shifted by the average opponent strength
def create_opponents(avg_opponent_strength=0.5):
    # Baseline is the "minimum strong" level; strength=1 pushes mean close to N.
    baseline_thinking_steps = N - EXPTECTED_ROUNDS
    strength = max(0.0, min(1.0, avg_opponent_strength))
    mean_thinking_steps = baseline_thinking_steps + strength * (N - baseline_thinking_steps)
    sigma = max(1, int((N - baseline_thinking_steps) * SIGMA_SCALE))
    thinking_steps = [
        max(0, min(N, int(round(random.gauss(mean_thinking_steps, sigma)))))
        for _ in range(NUMBER_OF_PLAYERS_IN_TOURNAMENT)
    ]
    return [Player(steps) for steps in thinking_steps]  

def plot_results(best_players, opponent_strengths):
    plt.figure(figsize=(10, 6))
    plt.plot(opponent_strengths, best_players, marker='o')
    plt.title('Best Player Thinking Steps vs Average Opponent Strength')
    plt.xlabel('Average opponent strength')
    plt.ylabel('Best Player Thinking Steps')
    plt.grid()
    plt.show()
    
def main():
    best_players = []
    avg_opponent_strengths = [i / 100.0 for i in range(0, 101, 25)] # from 0.0 to 1.0 in steps of 0.25
    for avg_opponent_strength in avg_opponent_strengths: # from 0 to 1 in steps of 0.1
        print(f"Testing with average opponent strength: {avg_opponent_strength}")
        opponents = create_opponents(avg_opponent_strength)
        win_rates = {}
        win_rates_per_thinking_time = {}
        print("Opponents' thinking steps:", [player.thinking_steps for player in opponents])
        # Player with thinking steps from N-EXPECTED_ROUNDS to N, excluding existing opponent steps
        test_thinking_steps_list = [i for i in range(N - EXPTECTED_ROUNDS, N + 1) if not any(player.thinking_steps == i for player in opponents)]
        for test_player_thinking_steps in test_thinking_steps_list:
            total_results = 0
            total_games = 0
            total_thinking_time = 0.0
            for it in range(NUMBER_OF_ITERATIONS):
                print(f"Iteration {it+1}/{NUMBER_OF_ITERATIONS}: Testing player with {test_player_thinking_steps} thinking steps")
                test_player = Player(test_player_thinking_steps)
                players = opponents + [test_player]
                results, games_played, thinking_times, _, _ = play_tournament(players, N, K, NUMBER_OF_GAMES_PER_MATCH)
                total_results += results.get(test_player_thinking_steps, 0)
                total_games += games_played.get(test_player_thinking_steps, 0)
                total_thinking_time += sum(thinking_times.get(test_player_thinking_steps, [0]))

            avg_win_rate = (total_results / total_games) if total_games > 0 else 0
            avg_thinking_time_per_game = (total_thinking_time / total_games) if total_games > 0 else 0
            win_rates[test_player_thinking_steps] = avg_win_rate
            win_rates_per_thinking_time[test_player_thinking_steps] = avg_win_rate / (avg_thinking_time_per_game if avg_thinking_time_per_game > 0 else 1)
        
        best_player = max(win_rates_per_thinking_time, key=win_rates_per_thinking_time.get)
        best_players.append(best_player)
    print(best_players)
    plot_results(best_players, [N - EXPTECTED_ROUNDS + strength * EXPTECTED_ROUNDS for strength in avg_opponent_strengths])

if __name__ == "__main__":
    main()
