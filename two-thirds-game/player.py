
from math import ceil
import random

CHOICE_RANGE = [1, 100]
NOISE_CHANCE = 0.75
MIN_REASONING_COST = 0.05

class Player:
    id = -1
    score = 0
    reasoning_cost = 0.5
    reasoning_budget = 1
    answer = 0
    noise_range = 10

    def __init__(self, id, reasoning_cost=0.5):
        self.id = id
        self.reasoning_cost = reasoning_cost
    
    def guess_number(self):
        guessed_number = 50

        if (self.reasoning_cost < MIN_REASONING_COST):
            self.answer = 1
            return 1

        while self.reasoning_budget - self.reasoning_cost >= 0 and guessed_number > 1:
            guessed_number = round(guessed_number * (2 / 3))
            self.reasoning_budget -= self.reasoning_cost
        
        if random.random() < NOISE_CHANCE:
            noise = random.randint(-self.noise_range, self.noise_range)
            guessed_number += noise
        self.answer = max(CHOICE_RANGE[0], min(CHOICE_RANGE[1], guessed_number))
        return self.answer
        