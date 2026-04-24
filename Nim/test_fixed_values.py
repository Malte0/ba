from game import create_T, partially_fixed_T, play_tournament
from players import Player, create_players
import matplotlib.pyplot as plt

N = 100
K = 8
V_VALUES = list(range(1, K + 1))
NUMBER_OF_GAMES = 1000
NUMBER_OF_PLAYERS = 2
def player_thinking_steps(player_index):
    return N-(N//(K//2))+player_index*(N//(K//2))
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

def plot_results(results_by_v, games_played_by_v):
    plt.xlabel('v (fixed value)')
    plt.ylabel('Winrate %')
    plt.title('Winrate by fixed v')

    plot_x = sorted(results_by_v.keys())
    player_steps = sorted({
        step
        for v in plot_x
        for step in games_played_by_v[v].keys()
    })

    for step in player_steps:
        winrates = []
        for v in plot_x:
            wins = results_by_v[v].get(step, 0)
            games = games_played_by_v[v].get(step, 0)
            winrates.append(round((wins / games) * 100, 2) if games else 0)
        plt.plot(plot_x, winrates, marker='o', label=f'Player steps={step}')

    plt.legend()
    plt.show()

def main():
    results_by_v = {}
    games_played_by_v = {}

    for v in V_VALUES:
        T_function = partially_fixed_T(fixed_values=[v], numberOfOptions=4, isKDevided=True)
        players: list[Player] = create_players(NUMBER_OF_PLAYERS, player_thinking_steps)
        results, games_played, _, _ = play_tournament(players, N, K, NUMBER_OF_GAMES, create_T=T_function)
        results_by_v[v] = results
        games_played_by_v[v] = games_played

    plot_results(results_by_v, games_played_by_v)

if __name__ == "__main__":
    main()