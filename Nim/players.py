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
        planning_steps = self.lut.populate(N, T, self.thinking_steps)
        self.time_end = time.time()
        self.thinking_times.append(self.time_end - self.time_start)
        return planning_steps

    def random_move(self, Ti):
        return random.choice(Ti)

    def lut_move(self, N, s, ns, Ts):
        for tsi in Ts:
            if ns + tsi >= N:
                return tsi
        for tsi in Ts:
            if self.lut.get(s+1, ns+tsi, False) == 1:
                return tsi
        return self.random_move(Ts) # fallback option if there is no winning move
    
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