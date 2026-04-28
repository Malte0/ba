
import matplotlib.pyplot as plt

from Game import determine_winners, create_players
from player import Player

NUMBER_OF_PLAYERS = 1000
NUMBER_OF_ROUNDS = 1_000
MEAN_REASONING_COST = 0.5
SIGMA_SCALE = 0.2

def plot_results(avg_answers_by_reasoning_cost: dict[float, float]):
    reasoning_costs = list(avg_answers_by_reasoning_cost.keys())
    average_answers = list(avg_answers_by_reasoning_cost.values())
    
    plt.scatter(reasoning_costs, average_answers)
    plt.xlabel('Reasoning Cost')
    plt.ylabel('Average Answer')
    plt.title('Average Answer by Reasoning Cost')
    plt.grid()
    plt.show()

def main():
    opponents: list[Player] = create_players(NUMBER_OF_PLAYERS, MEAN_REASONING_COST, SIGMA_SCALE)
    answers_by_reasoning_cost = {}
    for _ in range(NUMBER_OF_ROUNDS):
        [opponent.guess_number() for opponent in opponents]
        for opponent in opponents:
            rounded_reasoning_cost = round(opponent.reasoning_cost, 2)
            if rounded_reasoning_cost not in answers_by_reasoning_cost:
                answers_by_reasoning_cost[rounded_reasoning_cost] = []
            answers_by_reasoning_cost[rounded_reasoning_cost].append(opponent.answer)
    
    avg_answers_by_reasoning_cost = {cost: sum(answers) / len(answers) for cost, answers in answers_by_reasoning_cost.items()}
    plot_results(avg_answers_by_reasoning_cost)

if __name__ == "__main__":
    main()
