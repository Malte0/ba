
import matplotlib.pyplot as plt

from Game import get_winning_number, create_opponents
from player import Player
from plot_winning_numbers_per_mean import determine_winners

NUMBER_OF_PLAYERS = 1000
NUMBER_OF_ROUNDS = 1
CHOICE_RANGE = [1, 100]
MEAN_PLAYER_INTELLIGENCE = 0.25 # 1 is most inttelligent, 0 is least intelligent
SIGMA_SCALE = 0.08 # value with the nicest curve

def plot_results(answer_frequency: dict[int, int]):
    numbers = list(answer_frequency.keys())
    frequencies = list(answer_frequency.values())
    total_answers = sum(frequencies)
    frequency_percentages = [
        (frequency / total_answers) * 100 if total_answers > 0 else 0
        for frequency in frequencies
    ]

    plt.figure(figsize=(8.5, 4.8))
    plt.bar(numbers, frequency_percentages)
    plt.xlabel('Number Chosen')
    plt.ylabel('Answer Frequency (%)')
    plt.title('Answer Frequency Percentage by Number Chosen')
    plt.grid()
    plt.show()

def main():
    opponents: list[Player] = create_opponents(NUMBER_OF_PLAYERS)
    answer_frequency = {number: 0 for number in range(CHOICE_RANGE[0], CHOICE_RANGE[1] + 1)}
    for round in range(NUMBER_OF_ROUNDS):
        answers = [opponent.give_answer() for opponent in opponents]
        winning_number = get_winning_number(answers)
        winners = determine_winners(opponents, winning_number)
        for answer in answers:
            chosen_number = max(CHOICE_RANGE[0], min(CHOICE_RANGE[1], int(answer + 0.5)))
            answer_frequency[chosen_number] += 1
        for winner in winners:
            winner.add_win()

    opponents.sort(key=lambda x: x.score, reverse=False)
    plot_results(answer_frequency)

if __name__ == "__main__":
    main()
