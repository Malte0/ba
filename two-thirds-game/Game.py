
from math import ceil
import random
from player import Player

# creates a gaussian distribution of intelligence levels with mean at AVG_PLAYER_INTELLIGENCE and a standard deviation of SIGMA_SCALE
def create_opponents(number_of_players):
    opponents = []
    for id in range(number_of_players):
        opponents.append(Player(id=id))
    return opponents

def get_winning_number(answers):
    average = sum(answers) / len(answers)
    return ceil(average * 2 / 3)

def determine_winners(opponents: list[Player], winning_number):
    winners = []
    for opponent in opponents:
        if opponent.answer == winning_number:
            winners.append(opponent)
    return winners