import random
from solver import LookUpTable
import time

class Player:
    thinking_steps: int
    lut: LookUpTable
    thinking_times: list[int] = []

    def __init__(self, thinking_steps=0):
        self.thinking_steps = thinking_steps
        self.thinking_times = []
        self.lut = LookUpTable()
    
    def plan_ahead(self, N, T):
        self.time_start = time.time()
        self.lut.populate(N, T, self.thinking_steps)
        self.time_end = time.time()
        self.thinking_times.append(self.time_end - self.time_start)

    def random_move(self, Ti):
        return random.choice(Ti)

    def lut_move(self, N, s, ns, Ts):
        if ns+Ts[0] >= N:
            return Ts[0]
        elif ns+Ts[1] >= N:
            return Ts[1]
        return Ts[0] if self.lut.get(s+1, ns+Ts[0], False) == 1 else Ts[1]
    
    def make_move(self, N, s, ns, T):
        Ts = T[s]
        if self.lut.get(s, ns, True) == 1:
            return self.lut_move(N, s, ns, Ts)
        return self.random_move(Ts)

def create_players(number_of_players, player_thinking_steps):
    players = []
    for i in range(number_of_players):
        players.append(Player(player_thinking_steps(i)))
    return players