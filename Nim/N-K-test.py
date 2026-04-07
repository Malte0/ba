from game import partially_fixed_T, play_tournament
from players import Player, create_players
import matplotlib.pyplot as plt

NUMBER_OF_GAMES = 200
NUMBER_OF_PLAYERS = 2
PLOT_EFFICIENCY_BY_TIME = True
VERBOSE = False


def player_thinking_steps(n, k):
    # Keep a consistent gap between players while avoiding division-by-zero for small k.
    step_span = max(1, n // max(1, k // 2))
    base_steps = max(0, n - step_span)
    return lambda player_index: base_steps + player_index * step_span

def plot_results(
    win_rate_by_k: dict[int, dict[int, float]],
    efficiency_by_k: dict[int, dict[int, float]],
    avg_time_ms_by_k: dict[int, dict[int, float]],
    plot_efficiency_by_time: bool,
):
    if plot_efficiency_by_time:
        fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    else:
        fig, ax = plt.subplots(1, 1, figsize=(10, 6))
        axes = [ax]

    for k in sorted(win_rate_by_k.keys()):
        n_values = sorted(win_rate_by_k[k].keys())
        win_percentages = [win_rate_by_k[k][n] for n in n_values]
        axes[0].plot(n_values, win_percentages, marker='o', label=f'K={k}')

    if plot_efficiency_by_time:
        for k in sorted(efficiency_by_k.keys()):
            n_values = sorted(efficiency_by_k[k].keys())
            efficiency_values = [efficiency_by_k[k][n] for n in n_values]
            axes[1].plot(n_values, efficiency_values, marker='o', label=f'K={k}')

    axes[0].set_xlabel('N')
    axes[0].set_ylabel('Highest-Thinking Player Win Rate (%)')
    axes[0].set_title('Raw Win Rate')
    axes[0].grid(True)
    axes[0].legend()

    if plot_efficiency_by_time:
        axes[1].set_xlabel('N')
        axes[1].set_ylabel('Efficiency (win-rate percentage points per second planning)')
        axes[1].set_title('Cost-Aware Efficiency')
        axes[1].grid(True)
        axes[1].legend()

    fig.suptitle('Impact of N and K on Highest-Thinking Player')
    plt.tight_layout()
    plt.show()

def main():
    N_VALUES = [50, 75, 100, 125, 150]
    K_VALUES = [5, 6, 7, 8, 9]
    ITERATIONS_PER_SETTING = 20

    win_rate_by_k: dict[int, dict[int, float]] = {k: {} for k in K_VALUES}
    efficiency_by_k: dict[int, dict[int, float]] = {k: {} for k in K_VALUES}
    avg_time_ms_by_k: dict[int, dict[int, float]] = {k: {} for k in K_VALUES}

    for k in K_VALUES:
        for n in N_VALUES:
            total_win_rate = 0.0
            total_avg_time_ms = 0.0

            for _ in range(ITERATIONS_PER_SETTING):
                players: list[Player] = create_players(NUMBER_OF_PLAYERS, player_thinking_steps(n, k))
                results, games_played, thinking_times = play_tournament(players, n, k, NUMBER_OF_GAMES)

                highest_player = max(games_played.keys())
                wins = results.get(highest_player, 0)
                games = games_played.get(highest_player, 1)
                total_win_rate += (wins / games) * 100

                times = thinking_times.get(highest_player, [])
                avg_time_ms_this_iteration = (sum(times) / len(times)) * 1000 if times else 0.0
                total_avg_time_ms += avg_time_ms_this_iteration

            avg_win_rate = round(total_win_rate / ITERATIONS_PER_SETTING, 2)
            avg_time_ms = round(total_avg_time_ms / ITERATIONS_PER_SETTING, 3)
            # Efficiency unit: win-rate percentage points per second of planning.
            efficiency = round(avg_win_rate / max(avg_time_ms / 1000, 1e-9), 2)

            win_rate_by_k[k][n] = avg_win_rate
            avg_time_ms_by_k[k][n] = avg_time_ms
            efficiency_by_k[k][n] = efficiency

            print(
                f"K={k}, N={n}: win rate={avg_win_rate}%, "
                f"avg planning time={avg_time_ms}ms, "
                f"efficiency={efficiency} win-rate points/s"
            )

    plot_results(
        win_rate_by_k,
        efficiency_by_k,
        avg_time_ms_by_k,
        plot_efficiency_by_time=PLOT_EFFICIENCY_BY_TIME,
    )


if __name__ == "__main__":
    main()