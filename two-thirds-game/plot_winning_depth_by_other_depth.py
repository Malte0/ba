
import matplotlib.pyplot as plt

from Game import get_winning_number, create_opponents
from player import Player
from plot_winning_numbers_per_mean import determine_winners

NUMBER_OF_PLAYERS = 1000
NUMBER_OF_ROUNDS = 1000
CHOICE_RANGE = [1, 100]

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
        opponents: list[Player] = create_opponents(NUMBER_OF_PLAYERS, mean_reasoning_cost)
        for round in range(NUMBER_OF_ROUNDS):
            answers = [opponent.guess_number() for opponent in opponents]
            winning_number = get_winning_number(answers)
            winners = determine_winners(opponents, winning_number)
            avg_winning_cost = sum(winner.reasoning_cost for winner in winners) / len(winners) if winners else 0
            winning_costs_by_reasoning_cost[mean_reasoning_cost].append(avg_winning_cost)
    plot_results(winning_costs_by_reasoning_cost)

if __name__ == "__main__":
    main()
