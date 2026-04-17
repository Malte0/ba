
from math import ceil
import random

CHOICE_RANGE = [1, 100]

class Player:
    id = -1
    score = 0
    reasoning_depth = 0 # how many times the player will do 2/3 multiplications to get to the answer
    answer = 0
    noise_range = 5 # random number from range is added or subtracted from answer

    def __init__(self, id, reasoning_depth=0):
        self.id = id
        self.reasoning_depth = round(max(0, reasoning_depth))
    
    def guess_number(self):
        guessed_number = 50
        for _ in range(self.reasoning_depth):
            guessed_number = guessed_number * 2 / 3
        noise = random.uniform(-self.noise_range, self.noise_range)
        if random.random() < 0.5:
            guessed_number += noise
        self.answer = max(CHOICE_RANGE[0], min(CHOICE_RANGE[1], guessed_number))
        return self.answer
        