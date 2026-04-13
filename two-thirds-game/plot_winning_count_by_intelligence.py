
from math import ceil
import random
import matplotlib.pyplot as plt

from Game import create_opponents, determine_winners, get_winning_number
from player import Player

NUMBER_OF_PLAYERS = 1000
NUMBER_OF_ROUNDS = 10_00
CHOICE_RANGE = [1, 100]
MEAN_PLAYER_INTELLIGENCE = 0.78 # 1 is most inttelligent, 0 is least intelligent
SIGMA_SCALE = 0.3

def plot_results(wins_by_intelligence):
    intelligences = list(wins_by_intelligence.keys())
    win_counts = [sum(wins) for wins in wins_by_intelligence.values()]
    
    plt.scatter(intelligences, win_counts)
    plt.xlabel('Intelligence')
    plt.ylabel('Win Count')
    plt.title('Win Count by Intelligence')
    plt.grid()
    plt.show()

def main():
    opponents: list[Player] = create_opponents(NUMBER_OF_PLAYERS, MEAN_PLAYER_INTELLIGENCE, SIGMA_SCALE)
    for round in range(NUMBER_OF_ROUNDS):
        answers = [opponent.give_answer(opponent.intelligence) for opponent in opponents]
        winning_number = get_winning_number(answers)
        winners = determine_winners(opponents, winning_number)
        for winner in winners:
            winner.add_win()
    wins_by_intelligence = {}
    for opponent in opponents:
        if opponent.intelligence not in wins_by_intelligence:
            wins_by_intelligence[opponent.intelligence] = []
        wins_by_intelligence[opponent.intelligence].append(opponent.score)
    plot_results(wins_by_intelligence)    
    



if __name__ == "__main__":
    main()