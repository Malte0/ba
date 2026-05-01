
import matplotlib.pyplot as plt
from game import create_T, play_tournament
from players import create_players

N = 100
K = 8
NUMBER_OF_GAMES = 100
NUMBER_OF_ITERATIONS = 100
OTHER_PLAYER_THINKING_STEPS = 0
NUMBER_OF_PLAYERS = 2
def player_thinking_steps(player_index):
    return min(N, OTHER_PLAYER_THINKING_STEPS+player_index*N)
VERBOSE = False

def plot_results(results, games_played, thinking_times: dict[int, list[int]], guaranteed_wins):
    player_indices = sorted(thinking_times.keys())
    highest_thinking_player = player_indices[-1]
    win_rates = [(results[k][highest_thinking_player] / (NUMBER_OF_GAMES * NUMBER_OF_ITERATIONS)) * 100 for k in sorted(results.keys())]
    guaranteed_win_percentages = [(guaranteed_wins[k][highest_thinking_player] / (NUMBER_OF_GAMES * NUMBER_OF_ITERATIONS)) * 100 for k in sorted(results.keys())]
    ks = sorted(results.keys())

    fig, ax1 = plt.subplots(figsize=(10, 6))
    
    # Plot win rate on primary y-axis
    ax1.plot(ks, win_rates, marker='o', color='blue', label='Win Rate %')
    ax1.set_xlabel('M')
    ax1.set_ylabel('Win Rate in %', color='blue')
    ax1.set_ylim(bottom=0, top=100)
    ax1.tick_params(axis='y', labelcolor='blue')
    ax1.grid(True)
    
    # Create secondary y-axis for guaranteed wins percentage
    ax2 = ax1.twinx()
    ax2.plot(ks, guaranteed_win_percentages, marker='s', color='red', label='Guaranteed Wins %')
    ax2.set_ylabel('Guaranteed Wins in %', color='red')
    ax2.set_ylim(bottom=0, top=100)
    ax2.tick_params(axis='y', labelcolor='red')
    
    fig.suptitle(f'Win Rate and Guaranteed Wins of Player {highest_thinking_player}')
    fig.tight_layout()
    plt.show()

def main():
    players = create_players(NUMBER_OF_PLAYERS, player_thinking_steps)
    k_results = {}
    k_guaranteed_wins = {}
    for options in range(2, K+1):
        for _ in range(NUMBER_OF_ITERATIONS):
            print(f"Running with {options} options")
            MODIFIED_T = create_T(numberOfOptions=options, isKDevided=True)
            results, games_played, thinking_times, computation_steps, number_of_guaranteed_wins = play_tournament(players, N, K, NUMBER_OF_GAMES, create_T=MODIFIED_T, verbose=VERBOSE)
            if options not in k_results:
                k_results[options] = results
                k_guaranteed_wins[options] = number_of_guaranteed_wins
            else:
                k_results[options] = {player: k_results[options][player] + results[player] for player in results}
                k_guaranteed_wins[options] = {player: k_guaranteed_wins[options][player] + number_of_guaranteed_wins[player] for player in number_of_guaranteed_wins}
    print(f"Percentage of guaranteed wins: { {k: {player: (wins / (NUMBER_OF_GAMES * NUMBER_OF_ITERATIONS)) * 100 for player, wins in k_guaranteed_wins[k].items()} for k in k_guaranteed_wins} }")
    k_results = {k: {player: wins for player, wins in k_results[k].items()} for k in k_results} 
    plot_results(k_results, games_played, thinking_times, k_guaranteed_wins)

if __name__ == "__main__":
    main()

# run convergence nim with non perfect player