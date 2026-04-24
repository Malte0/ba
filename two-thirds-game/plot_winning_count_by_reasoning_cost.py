
from math import ceil
import random
import matplotlib.pyplot as plt

from Game import create_opponents, determine_winners, get_winning_number
from player import Player

NUMBER_OF_PLAYERS = 1000
NUMBER_OF_ROUNDS = 1_000
MEAN_PLAYER_INTELLIGENCE = 0.5 # 1 is most inttelligent, 0 is least intelligent
SIGMA_SCALE = 0.2

def plot_results(wins_by_reasoning_cost):
    reasoning_costs = list(wins_by_reasoning_cost.keys())
    win_counts = [sum(wins) for wins in wins_by_reasoning_cost.values()]
    
    plt.scatter(reasoning_costs, win_counts)
    plt.xlabel('Reasoning Cost')
    plt.ylabel('Win Count')
    plt.title('Win Count by Reasoning Cost')
    plt.grid()
    plt.show()

def main():
    opponents: list[Player] = create_opponents(NUMBER_OF_PLAYERS, MEAN_PLAYER_INTELLIGENCE, SIGMA_SCALE)
    for _ in range(NUMBER_OF_ROUNDS):
        [opponent.guess_number() for opponent in opponents]
        winners = determine_winners(opponents)
        for winner in winners:
            winner.score += 1
    wins_by_reasoning_cost = {}
    for opponent in opponents:
        if opponent.reasoning_cost not in wins_by_reasoning_cost:
            wins_by_reasoning_cost[opponent.reasoning_cost] = []
        wins_by_reasoning_cost[opponent.reasoning_cost].append(opponent.score)
    plot_results(wins_by_reasoning_cost)    
    



if __name__ == "__main__":
    main()