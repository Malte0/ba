
from math import ceil
import random
import matplotlib.pyplot as plt

from player import Player

NUMBER_OF_PLAYERS = 100
NUMBER_OF_ROUNDS = 10_000
CHOICE_RANGE = [1, 100]
MEAN_PLAYER_INTELLIGENCE = 0.8 # 1 is most inttelligent, 0 is least intelligent
SIGMA_SCALE = 0.3

# creates a gaussian distribution of intelligence levels with mean at AVG_PLAYER_INTELLIGENCE and a standard deviation of SIGMA_SCALE
def create_opponents(mean_intelligence=MEAN_PLAYER_INTELLIGENCE):
    opponents = []
    for id in range(NUMBER_OF_PLAYERS):
        intelligence = random.gauss(mean_intelligence, SIGMA_SCALE)
        intelligence = max(0, min(1, intelligence)) # Ensure intelligence is between 0 and 1
        opponents.append(Player(id=id, intelligence=intelligence))
    return opponents

intelligence_epsilon = 0.01 # A small value to prevent infinite loops for very intelligent players
# A more intelligent player will do more induction steps getting closer to 1

def get_winning_number(answers):
    average = sum(answers) / len(answers)
    return ceil(average * 2 / 3)

def determine_winners(opponents, winning_number):
    winners = []
    for opponent in opponents:
        if opponent.give_answer(opponent.intelligence) == winning_number:
            winners.append(opponent)
    return winners

def plot_results(winning_numbers_per_mean):
    plt.figure(figsize=(10, 6))
    means = sorted(winning_numbers_per_mean.keys())
    cmap = plt.get_cmap('tab10')

    for idx, mean in enumerate(means):
        winning_numbers = winning_numbers_per_mean[mean]
        x_values = sorted(winning_numbers.keys())
        y_values = [winning_numbers[number] for number in x_values]
        color = cmap(idx % cmap.N)
        plt.plot(x_values, y_values, color=color, alpha=0.9, linewidth=2, label=f'mean={mean}')

    plt.xlabel('Number')
    plt.ylabel('Number of wins')
    plt.title('Winning numbers by mean intelligence')
    plt.legend()
    plt.grid(alpha=0.2)
    plt.tight_layout()
    plt.show()

def main():
    means = [0.25, 0.5, 0.75, 1]

    winning_numbers_per_mean = {}
    for mean_intelligence in means:
        opponents = create_opponents(mean_intelligence=mean_intelligence)
        winning_numbers = {}
        for round in range(NUMBER_OF_ROUNDS):
            answers = [opponent.give_answer(opponent.intelligence) for opponent in opponents]
            winning_number = get_winning_number(answers)
            winning_numbers[winning_number] = winning_numbers.get(winning_number, 0) + 1
            winners = determine_winners(opponents, winning_number)
            for winner in winners:
                winner.add_win()
        opponents.sort(key=lambda x: x.score, reverse=True)
        for opponent in opponents:
            print(f"Player {opponent.id}, int: {opponent.intelligence:.2f}, score {opponent.score}")

        winning_numbers_per_mean[mean_intelligence] = winning_numbers
    
    plot_results(winning_numbers_per_mean)

if __name__ == "__main__":
    main()