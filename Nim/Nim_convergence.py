
import matplotlib.pyplot as plt
from game import create_T, play_tournament
from players import create_players

N = 100
K = 8
NUMBER_OF_GAMES = 100
NUMBER_OF_ITERATIONS = 100
NUMBER_OF_PLAYERS = 2
def player_thinking_steps(player_index):
    return min(100, 90+player_index*N)
VERBOSE = False

def plot_results(results, games_played, thinking_times: dict[int, list[int]]):
    player_indices = sorted(thinking_times.keys())
    highest_thinking_player = player_indices[-1]
    win_rates = [(results[k][highest_thinking_player] / (NUMBER_OF_GAMES * NUMBER_OF_ITERATIONS)) * 10000 for k in sorted(results.keys())]
    ks = sorted(results.keys())

    plt.figure(figsize=(10, 6))
    plt.plot(ks, win_rates, marker='o')
    plt.xlabel('K')
    plt.ylabel('Win Rate in %')
    plt.title(f'Win Rate of Player {highest_thinking_player}')
    plt.grid(True)
    plt.show()

def main():
    players = create_players(NUMBER_OF_PLAYERS, player_thinking_steps)
    k_results = {}
    for options in range(2, K+1):
        for _ in range(NUMBER_OF_ITERATIONS):
            print(f"Running with {options} options")
            MODIFIED_T = create_T(numberOfOptions=options, isKDevided=True)
            results, games_played, thinking_times, computation_steps = play_tournament(players, N, K, NUMBER_OF_GAMES, create_T=MODIFIED_T)
            k_results[options] = results if options not in k_results else {player: k_results[options][player] + results[player] for player in results}
    k_results = {k: {player: wins / NUMBER_OF_ITERATIONS for player, wins in k_results[k].items()} for k in k_results} 
    plot_results(k_results, games_played, thinking_times)

if __name__ == "__main__":
    main()

# run convergence nim with non perfect player