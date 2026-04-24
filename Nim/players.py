import random
from solver import LookUpTable
import time

class Player:
    thinking_steps: int
    lut: LookUpTable
    thinking_times: list[int] = []
    computation_steps: list[int] = []

    def __init__(self, thinking_steps=0):
        self.thinking_steps = thinking_steps
        self.thinking_times = []
        self.lut = LookUpTable()
    
    def plan_ahead(self, N, T):
        self.time_start = time.time()
        computation_steps = self.lut.populate(N, T, self.thinking_steps)
        self.time_end = time.time()
        self.thinking_times.append(self.time_end - self.time_start)
        self.computation_steps.append(computation_steps)
        return computation_steps

    def random_move(self, Ti):
        return random.choice(Ti)

    def lut_move(self, N, s, ns, Ts):
        # if there is a move that wins immediately, take it
        for tsi in Ts:
            if ns + tsi >= N:
                return tsi
        # otherwise, take a move that leads to a winning position in the next step
        for tsi in Ts:
            if self.lut.get(s+1, ns+tsi, False) == 1:
                return tsi
        return self.random_move(Ts) # fallback option if there is no good move
    
    def make_move(self, N, s, ns, T):
        Ts = T[s]
        return self.lut_move(N, s, ns, Ts)

def create_players(number_of_players, player_thinking_steps):
    players = []
    for i in range(number_of_players):
        players.append(Player(player_thinking_steps(i)))
    return players