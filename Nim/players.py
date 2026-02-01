import random
from solver import LookUpTable

class Player:
    def __init__(self, thinking_steps=0):
        self.thinking_steps = thinking_steps
        self.lut = LookUpTable()
    
    def think_ahead(self, N, T):
        self.lut.populate(N, T, self.thinking_steps)
        # self.lut.print()

    def random_move(self, Ti):
        return random.choice(Ti)

    def lut_move(self, s, ns, Ti):
        Ti0_result = self.lut.get(s, ns, Ti[0])
        Ti1_result = self.lut.get(s, ns, Ti[1])
        if Ti0_result == 1:
            return Ti[0]
        elif Ti1_result == 1:
            return Ti[1]
        return None
    
    def make_move(self, s, ns, T):
        Ti = T[s]
        if self.lut.get(s, ns, Ti[0]):
            return self.lut_move(s, ns, Ti)
        return self.random_move(Ti)


# TODO: Does it make sense to consider looking ahead, so that if we have no guaranteed win, we can still make a move where it's possible for the opponent to make a mistake for us to end up in a guaranteed winning scenario