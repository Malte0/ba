
from math import ceil
import random
CHOICE_RANGE = [1, 100]

def clamp_choice(choice):
    return ceil(max(CHOICE_RANGE[0], min(CHOICE_RANGE[1], choice)))

class Player:
    intelligence_epsilon = 0.01 # A small value to prevent infinite loops for very intelligent players

    def __init__(self, id, intelligence):
        self.id = id
        self.intelligence = intelligence
        self.score = 0

    def add_win(self):
        self.score += 1
    
    def give_answer(self, player_intelligence):
        if player_intelligence > 1-self.intelligence_epsilon:
            return 1
        two_thirds = (2 / 3) * CHOICE_RANGE[1]
        random_number = random.uniform(0,1)
        while random_number < player_intelligence:
            two_thirds *= (2 / 3)
            random_number = random.uniform(0,1)
        return clamp_choice(two_thirds)