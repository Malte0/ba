import random
from solver import LookUpTable

class Player:
    def __init__(self, thinking_steps=0):
        self.thinking_steps = thinking_steps
        self.lut = LookUpTable()
    
    def plan_ahead(self, N, T):
        self.lut.populate(N, T, self.thinking_steps)
        # self.lut.print()

    def random_move(self, Ti):
        return random.choice(Ti)

    def lut_move(self, s, ns, Ts):
        return Ts[0] if self.lut.get(s+1, ns+Ts[0], False) == 1 else Ts[1]
    
    def make_move(self, s, ns, T):
        Ts = T[s]
        if self.lut.get(s, ns, True) == 1:
            return self.lut_move(s, ns, Ts)
        return self.random_move(Ts)


# TODO: Does it make sense to consider looking ahead, so that if we have no guaranteed win, we can still make a move where it's possible for the opponent to make a mistake for us to end up in a guaranteed winning scenario