
import matplotlib.pyplot as plt

from Game import create_opponents, determine_winners, get_winning_number

NUMBER_OF_PLAYERS = 20
NUMBER_OF_ROUNDS = 1_000
MEAN_PLAYER_REASONING_COST = 0.4 # 1 is most inttelligent, 0 is least intelligent
SIGMA_SCALE = 0.2

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
    plt.title('Winning numbers by mean reasoning cost')
    plt.legend()
    plt.grid(alpha=0.2)
    plt.tight_layout()
    plt.show()

def main():
    means = [0.25, 0.5, 0.75, 1]

    winning_numbers_per_mean = {}
    for mean_reasoning_cost in means:
        opponents = create_opponents(NUMBER_OF_PLAYERS, mean_reasoning_cost, SIGMA_SCALE)
        winning_numbers = {}
        for _ in range(NUMBER_OF_ROUNDS):
            answers = [opponent.guess_number() for opponent in opponents]
            winning_number = get_winning_number(answers)
            winning_numbers[winning_number] = winning_numbers.get(winning_number, 0) + 1
            winners = determine_winners(opponents)
            for winner in winners:
                winner.score += 1

        winning_numbers_per_mean[mean_reasoning_cost] = winning_numbers
    
    plot_results(winning_numbers_per_mean)

if __name__ == "__main__":
    main()