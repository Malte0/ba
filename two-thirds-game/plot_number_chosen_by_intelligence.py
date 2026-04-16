
from math import ceil
import matplotlib.pyplot as plt

from Game import get_winning_number, create_opponents
from player import Player
from plot_winning_numbers_per_mean import determine_winners

NUMBER_OF_PLAYERS = 1000
NUMBER_OF_ROUNDS = 10_000
CHOICE_RANGE = [1, 100]
MEAN_PLAYER_INTELLIGENCE = 0.5 # 1 is most inttelligent, 0 is least intelligent
SIGMA_SCALE = 0.3 # value with the nicest curve

def plot_results(avg_answers_by_intelligence: dict[float, float]):
    intelligences = list(avg_answers_by_intelligence.keys())
    average_answers = list(avg_answers_by_intelligence.values())
    
    plt.scatter(intelligences, average_answers)
    plt.xlabel('Intelligence')
    plt.ylabel('Average Answer')
    plt.title('Average Answer by Intelligence')
    plt.grid()
    plt.show()

def main():
    opponents: list[Player] = create_opponents(NUMBER_OF_PLAYERS, MEAN_PLAYER_INTELLIGENCE, SIGMA_SCALE)
    answers_by_intelligence = {}
    for round in range(NUMBER_OF_ROUNDS):
        answers = [opponent.give_answer() for opponent in opponents]
        winning_number = get_winning_number(answers)
        winners = determine_winners(opponents, winning_number)
        for opponent in opponents:
            if opponent.reasoning_depth not in answers_by_intelligence:
                answers_by_intelligence[opponent.reasoning_depth] = []
            answers_by_intelligence[opponent.reasoning_depth].append(opponent.answer)
        for winner in winners:
            winner.add_win()
    
    avg_answers_by_intelligence = {}
    for intelligence, answers in answers_by_intelligence.items():
        average_answer = sum(answers) / len(answers)
        avg_answers_by_intelligence[intelligence] = average_answer

    opponents.sort(key=lambda x: x.score, reverse=False)
    plot_results(avg_answers_by_intelligence)

if __name__ == "__main__":
    main()
