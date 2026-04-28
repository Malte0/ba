
import matplotlib.pyplot as plt

from Game import CHOICE_RANGE, create_players
from player import Player

NUMBER_OF_PLAYERS = 10_000
NUMBER_OF_ROUNDS = 1
MEAN_REASONING_COST = 0.5
SIGMA_SCALE= 0.2

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
    opponents: list[Player] = create_players(NUMBER_OF_PLAYERS, MEAN_REASONING_COST, SIGMA_SCALE)
    answer_frequency = {number: 0 for number in range(CHOICE_RANGE[0], CHOICE_RANGE[1] + 1)}
    for _ in range(NUMBER_OF_ROUNDS):
        answers = [opponent.guess_number() for opponent in opponents]
        for answer in answers:
            answer_frequency[answer] += 1

    plot_results(answer_frequency)

if __name__ == "__main__":
    main()
