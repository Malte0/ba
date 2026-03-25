
import matplotlib.pyplot as plt
from game import create_T, play_tournament
from players import create_players

N = 100
K = 8
NUMBER_OF_GAMES = 100
NUMBER_OF_PLAYERS = 2
def player_thinking_steps(player_index):
    return 0+player_index*N
VERBOSE = False

def plot_results(results, games_played, thinking_times: dict[int, list[int]]):
    player_indices = sorted(thinking_times.keys())
    highest_thinking_player = player_indices[-1]
    win_rates = [results[k][highest_thinking_player] / NUMBER_OF_GAMES for k in sorted(results.keys())]
    ks = sorted(results.keys())

    plt.figure(figsize=(10, 6))
    plt.plot(ks, win_rates, marker='o')
    plt.xlabel('K')
    plt.ylabel('Win Rate')
    plt.title(f'Win Rate of Player {highest_thinking_player}')
    plt.grid(True)
    plt.show()

def main():
    players = create_players(NUMBER_OF_PLAYERS, player_thinking_steps)
    k_results = {}
    ITERATIONS_PER_K = 20
    for k in range(2, K+1):
        for _ in range(ITERATIONS_PER_K):
            print(f"Running with K={k}")
            MODIFIED_T = create_T(numberOfOptions=k, isKDevided=True)
            results, games_played, thinking_times = play_tournament(players, N, K, NUMBER_OF_GAMES, create_T=MODIFIED_T)
            k_results[k] = results if k not in k_results else {player: k_results[k][player] + results[player] for player in results}
    k_results = {k: {player: wins / ITERATIONS_PER_K for player, wins in k_results[k].items()} for k in k_results} 
    plot_results(k_results, games_played, thinking_times)

if __name__ == "__main__":
    main()