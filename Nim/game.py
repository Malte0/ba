import random
from time import time
from players import Player

def create_T(numberOfOptions=2, isKDevided=False):
    def create_table(N, K):
        T = []
        for _ in range(N):
            options = []
            for i in range(numberOfOptions):
                if isKDevided:
                    lower = 1 + i * (K // numberOfOptions)
                    upper = (i + 1) * (K // numberOfOptions)
                    options.append(random.randint(lower, max(lower, upper)))
                else:
                    options.append(random.randint(1, K))
            T.append(tuple(options))
        return T
    return create_table

DEFAULT_T = create_T()

# example of creating a T with 2 options, where the first option is between 1 and 4, and the second option is between 5 and 8
# print(create_T(numberOfOptions=2, isKDevided=True)(1, 8)) 

# allows to fix some values in T, while randomizing the rest
def partially_fixed_T(fixed_values, numberOfOptions=2, isKDevided=False):
    options_with_fixed_value = numberOfOptions - len(fixed_values)
    def create_table(N, K):
        T = []
        for i in range(N):
            options = list(fixed_values)
            for j in range(options_with_fixed_value):
                if isKDevided:
                    lower = 1 + j * (K // options_with_fixed_value)
                    upper = (j + 1) * (K // options_with_fixed_value)
                    options.append(random.randint(lower, max(lower, upper)))
                else:
                    options.append(random.randint(1, K))
            T.append(tuple(options))
        return T
    return create_table

# winners thinking steps are returned
def play_game(N, T, player1: Player, player2: Player, verbose=False):
    ns = 0
    s = 0
    turnSwitch = random.choice([True, False])
    while True:
        choice = player1.make_move(N, s, ns, T) if turnSwitch else player2.make_move(N, s, ns, T)
        if verbose: print(f"Ns: {ns} - Ts: {T[s]} - Step: {s}")
        if verbose: print(f"Player {player1.thinking_steps if turnSwitch else player2.thinking_steps} chose: {choice}")
        ns += choice
        if ns >= N:
            if verbose: print(f"Game over! Winner: {player1.thinking_steps if turnSwitch else player2.thinking_steps}")
            return player1.thinking_steps if turnSwitch else player2.thinking_steps
        s += 1
        turnSwitch = not turnSwitch

def play_round(N, K, player1: Player, player2: Player, results, verbose=False, create_T=DEFAULT_T):
    T = create_T(N, K)
    player1.plan_ahead(N, T)
    player2.plan_ahead(N, T)
    winner_steps = play_game(N, T, player1, player2, verbose)
    results[winner_steps] = results.get(winner_steps, 0) + 1
    return results


def play_tournament(players, N, K, NUMBER_OF_GAMES, create_T=DEFAULT_T):
    results = { player.thinking_steps: 0 for player in players } # dict of how may games players have won
    games_played = { player.thinking_steps: 0 for player in players } # dict of how many games players have played
    computation_steps = { player.thinking_steps: 0 for player in players } # dict of how much memory players have used
    for i in range(len(players)):
        for j in range(i+1, len(players)):
            for _ in range(NUMBER_OF_GAMES):
                games_played[players[i].thinking_steps] = games_played.get(players[i].thinking_steps, 0)+1
                games_played[players[j].thinking_steps] = games_played.get(players[j].thinking_steps, 0)+1
                results: dict[int, int] = play_round(N, K, players[i], players[j], results, create_T=create_T)
    thinking_times = {player.thinking_steps: player.thinking_times for player in players}
    computation_steps = {player.thinking_steps: player.computation_steps for player in players}
    return results, games_played, thinking_times, computation_steps