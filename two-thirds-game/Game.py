
import random
from player import Player

CHOICE_RANGE = [1, 100]

def create_opponents(number_of_players, mean_reasoning_cost=0.1, sigma_scale=0.2):
    opponents = []
    for id in range(number_of_players):
        sampled_cost = random.gauss(mean_reasoning_cost, sigma_scale)
        reasoning_cost = max(0, sampled_cost)
        opponents.append(Player(id=id, reasoning_cost=reasoning_cost))
    return opponents

def get_winning_number(answers):
    average = sum(answers) / len(answers)
    rounded = round(average * (2 / 3))
    return rounded

def closest_to_winning_number(opponents: list[Player], winning_number: int):
    closest_opponents = []
    closest_distance: int = 100
    for opponent in opponents:
        distance = abs(opponent.answer - winning_number)
        if distance < closest_distance:
            closest_distance = distance
            closest_opponents = [opponent]
        elif distance == closest_distance:
            closest_opponents.append(opponent)
    return closest_opponents

def determine_winners(opponents: list[Player]):
    winning_number = get_winning_number([opponent.guess_number() for opponent in opponents])
    winners = closest_to_winning_number(opponents, winning_number)
    return winners