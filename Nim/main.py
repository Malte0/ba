from game import create_T, play_tournament
from players import Player, create_players
import matplotlib.pyplot as plt

N = 100
K = 8
NUMBER_OF_GAMES = 100
NUMBER_OF_PLAYERS = 2
def player_thinking_steps(player_index):
    return 75+player_index*25
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

def plot_results(results, games_played, thinking_times: dict[int, list[int]]):
    plt.xlabel('Thinking steps')
    plt.ylabel('Winrate %')
    thinking_times = get_planning_steps()
    plot_x = [key for key, value in results.items()]
    plot_z_normed, plot_z_scaled  = thinking_norm(thinking_times)
    print("plot_z_normed")
    print(plot_z_normed)
    # considering computational costs
    plot_y = [round((value / games_played[key]) * 100, 2) / plot_z_normed[key] for key, value in results.items()]
    # ignoring all costs
    # plot_y = [round((value / games_played[key]) * 100, 2) for key, value in results.items()]
    for key, value in results.items():
        player_win_percentage = round((value / games_played[key]) * 100, 2)
        print(f"Player {key} won {player_win_percentage}% games, thinking {plot_z_scaled[key]}")

    # print(plot_z_normed)
    plot_x_sorted = sorted(plot_x)
    plot_y_sorted = [plot_y[plot_x.index(x)] for x in plot_x_sorted]
    plot_z_scaled_sorted = [plot_z_scaled[x] for x in plot_x_sorted]
    plt.plot(plot_x_sorted, plot_y_sorted, plot_x_sorted, plot_z_scaled_sorted)
    plt.show()

def main():
    players: list[Player] = create_players(NUMBER_OF_PLAYERS, player_thinking_steps)
    results, games_played, thinking_times = play_tournament(players, N, K, NUMBER_OF_GAMES)
    plot_results(results, games_played, thinking_times)

if __name__ == "__main__":
    main()