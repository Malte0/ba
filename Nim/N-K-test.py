from game import create_T, play_tournament
from players import Player, create_players
import matplotlib.pyplot as plt

N = 100
K = 10
NUMBER_OF_GAMES = 100
NUMBER_OF_PLAYERS = 2
def player_thinking_steps(n, k):
    return lambda player_index: n-(n//(k//2))+player_index*(n//(k//2))
VERBOSE = False

def get_planning_steps():
    # (N//(K//2)) is the expected number of rounds, so N - (N//(K//2)) is the expected number of rounds where planning ahead makes sense
    players: list[Player] = create_players((N//(K//2))+1, lambda a : N-(N//(K//2))+a)
    T = create_T(N, K)
    planning_steps: dict[int, list[int]] = {}
    for player in players:
        planning_steps[player.thinking_steps] = [player.plan_ahead(N, T)]
    return planning_steps

def readable(thinking_time):
    return round(thinking_time * 1000, 2)

def thinking_norm(thinking_times: dict[int, list[int]]):
    vals = {key: readable(sum(t_times) / len(t_times)) for key, t_times in thinking_times.items()}
    lowest = max(1, min(vals.values()))
    normed_vals = {key: max(1, (thinking_time / lowest)) for key, thinking_time in vals.items()}
    scaled_vals = {key: round(thinking_time * 20, 1) for key, thinking_time in normed_vals.items()}
    return normed_vals, scaled_vals

def plot_results(iteration_average):
    plt.figure(figsize=(10, 6))
    max_player = max(iteration_average[list(iteration_average.keys())[0]].keys())
    n_values = sorted(iteration_average.keys())
    win_percentages = [iteration_average[n][max_player] for n in n_values]
    plt.plot(n_values, win_percentages, marker='o')
    plt.xlabel('N')
    plt.ylabel('Win Percentage (%)')
    plt.title(f'Win Percentage vs N (Player {max_player})')
    plt.grid(True)
    plt.show()
    

def main():
    global N
    N_ITERATIONS = 10
    ITERATION_STEP = 10
    iteration_average = {}
    for i in range(N_ITERATIONS):
        NEW_N = N + i*ITERATION_STEP
        print(f"Iteration {NEW_N} of {N_ITERATIONS}")
        players: list[Player] = create_players(NUMBER_OF_PLAYERS, player_thinking_steps(NEW_N, K))
        results, games_played, thinking_times = play_tournament(players, NEW_N, K, NUMBER_OF_GAMES)
        winpercentages = {key: round((value / games_played[key]) * 100, 2) for key, value in results.items()}
        print(f"Results for N={NEW_N}: {winpercentages}")
        iteration_average[NEW_N] = winpercentages if NEW_N not in iteration_average else {player: iteration_average[NEW_N][player] + winpercentages[player] for player in winpercentages}
    iteration_average = {N: {player: round(winpercentage / N_ITERATIONS, 2) for player, winpercentage in iteration_average[N].items()} for N in iteration_average}
    print("Average win percentages over iterations:")
    for N, winpercentages in iteration_average.items():
        print(f"N={N}: {winpercentages}")
    plot_results(iteration_average)
    

if __name__ == "__main__":
    main()