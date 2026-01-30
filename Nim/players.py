import random
from solver import create_lookup_table

# chooses a random t from Ti
def random_move(Ti, s):
    return random.choice(Ti[s])

def get_lut_move(lut, ns, s, Ti):
    Ti0 = lut[(s, ns, Ti[0])]
    Ti1 = lut[(s, ns, Ti[1])]
    if Ti0 and Ti0 == 1:
        return Ti[0]
    elif Ti1 and Ti1 == 1:
        return Ti[1]
    return None

class Player:
    def __init__(self, thinking_steps=0):
        self.thinking_steps = thinking_steps
        self.lookup_table = create_lookup_table(thinking_steps)

    def make_move(self, ns, s, Ti):
        # if we are in the explored range
        if thinking_steps >= N-s:
            # find best move, otherwise move random
            # TODO: Does it make sense to consider looking ahead, so that if we have no guaranteed win, we can still make a move where it's possible for the opponent to make a mistake for us to end up in a guaranteed winning scenario
            lut_move = get_lut_move(self.lookup_table, ns, s, Ti)
            if lut_move is not None:
                return lut_move
        return random_move(Ti, s)