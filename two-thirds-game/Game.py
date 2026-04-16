
from math import ceil
import random
from player import Player

# creates a gaussian distribution of intelligence levels with mean at AVG_PLAYER_INTELLIGENCE and a standard deviation of SIGMA_SCALE
def create_opponents(number_of_players, mean_intelligence=0.5, sigma_scale=0.3):
    opponents = []
    for id in range(number_of_players):
        intelligence = random.gauss(mean_intelligence, sigma_scale)
        intelligence = max(0, min(1, intelligence)) # Ensure intelligence is between 0 and 1
        opponents.append(Player(id=id, thinking_depth=intelligence))
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