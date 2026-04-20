
from math import ceil
import random
import matplotlib.pyplot as plt

from Game import create_opponents, determine_winners, get_winning_number
from player import Player

NUMBER_OF_PLAYERS = 100000
NUMBER_OF_ROUNDS = 10_000
CHOICE_RANGE = [1, 100]
MEAN_REASONING_COST = 0.5

def plot_results(player_count_by_intelligence):
    intelligences = list(player_count_by_intelligence.keys())
    player_counts = list(player_count_by_intelligence.values())

    plt.scatter(intelligences, player_counts)
    plt.xlabel('Intelligence')
    plt.ylabel('Player Count')
    plt.title('Player Count by Intelligence')
    plt.grid()
    plt.show()

def main():
    opponents: list[Player] = create_opponents(NUMBER_OF_PLAYERS, MEAN_REASONING_COST)
    player_count_by_intelligence = {}
    for opponent in opponents:
        rounded_intelligence = round(opponent.reasoning_cost, 2)
        if rounded_intelligence not in player_count_by_intelligence:
            player_count_by_intelligence[rounded_intelligence] = 0
        player_count_by_intelligence[rounded_intelligence] += 1
    plot_results(player_count_by_intelligence)    
    

if __name__ == "__main__":
    main()