
from math import ceil
import random
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

from Game import create_opponents, determine_winners, get_winning_number
from player import Player

NUMBER_OF_PLAYERS = 100000
NUMBER_OF_ROUNDS = 1000
MEAN_REASONING_COST = 0.11

def plot_results(player_count_by_reasoning_cost):
    reasoning_costs = list(player_count_by_reasoning_cost.keys())
    player_counts = list(player_count_by_reasoning_cost.values())
    total_players = sum(player_counts)
    player_percentages = [count / total_players * 100 for count in player_counts]

    plt.scatter(reasoning_costs, player_percentages)
    plt.xlabel('Reasoning Cost')
    plt.ylabel('Player Percentage')
    plt.title('Player Percentage by Reasoning Cost')
    plt.gca().yaxis.set_major_formatter(PercentFormatter())
    plt.grid()
    plt.show()

def main():
    opponents: list[Player] = create_opponents(NUMBER_OF_PLAYERS, MEAN_REASONING_COST)
    player_count_by_reasoning_cost = {}
    for opponent in opponents:
        rounded_reasoning_cost = round(opponent.reasoning_cost, 2)
        if rounded_reasoning_cost not in player_count_by_reasoning_cost:
            player_count_by_reasoning_cost[rounded_reasoning_cost] = 0
        player_count_by_reasoning_cost[rounded_reasoning_cost] += 1
    plot_results(player_count_by_reasoning_cost)    
    

if __name__ == "__main__":
    main()