
import matplotlib.pyplot as plt

from Game import determine_winners, create_players
from player import Player

NUMBER_OF_PLAYERS = 1000
NUMBER_OF_ROUNDS = 1000

def plot_results(winning_costs_by_reasoning_cost: dict[float, list[float]]):
    reasoning_costs = list(winning_costs_by_reasoning_cost.keys())
    average_winning_costs = [
        sum(costs) / len(costs) if costs else 0
        for costs in winning_costs_by_reasoning_cost.values()
    ]

    plt.figure(figsize=(8.5, 4.8))
    plt.plot(reasoning_costs, average_winning_costs, marker='o')
    plt.xlabel('Mean Player Reasoning Cost')
    plt.ylabel('Average Winning Player Reasoning Cost')
    plt.title('Average Winning Player Reasoning Cost by Mean Player Reasoning Cost')
    plt.grid()
    plt.show()

def main():
    MAX_I = 100
    winning_costs_by_reasoning_cost = {i / MAX_I: [] for i in range(1, MAX_I)}
    for i in range(1, MAX_I):
        mean_reasoning_cost = i / MAX_I
        opponents: list[Player] = create_players(NUMBER_OF_PLAYERS, mean_reasoning_cost)
        for _ in range(NUMBER_OF_ROUNDS):
            [opponent.guess_number() for opponent in opponents]
            winners = determine_winners(opponents)
            avg_winning_reasoning_cost = sum([winner.reasoning_cost for winner in winners]) / len(winners)
            winning_costs_by_reasoning_cost[mean_reasoning_cost].append(avg_winning_reasoning_cost)
    plot_results(winning_costs_by_reasoning_cost)

if __name__ == "__main__":
    main()
