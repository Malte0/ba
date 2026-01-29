import random
from solver import create_lookup_table

# chooses a random t from Ti
def random_move(Ti, s):
    return random.choice(Ti[s])

class Player:
    def __init__(self, thinking_steps=0):
        self.thinking_steps = thinking_steps
        self.lookup_table = create_lookup_table(thinking_steps)

    def make_move(self, ns, s, Ti):
        if s in self.lookup_table:
            return self.lookup_table[s]
        return random_move(Ti, s)