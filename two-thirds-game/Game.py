
from math import ceil
import random
from player import Player

# creates a gaussian distribution of intelligence levels with mean at AVG_PLAYER_INTELLIGENCE and a standard deviation of SIGMA_SCALE
def create_opponents(number_of_players, mean_reasoning_cost=0.1, sigma_scale=0.2):
    opponents = []
    for id in range(number_of_players):
        sampled_cost = random.gauss(mean_reasoning_cost, sigma_scale)
        reasoning_cost = max(0, sampled_cost)
        opponents.append(Player(id=id, reasoning_cost=reasoning_cost))
    return opponents

def get_winning_number(answers):
    average = sum(answers) / len(answers)
    return max(1, round(average * (2 / 3)))

def determine_winners(opponents: list[Player], winning_number):
    winners = []
    for opponent in opponents:
        if opponent.answer == winning_number:
            winners.append(opponent)
    return winners