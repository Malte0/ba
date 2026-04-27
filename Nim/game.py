import random
from time import time
from players import Player


# Calculates the bounds of the bucket given its index
def bucket_bounds(index, total_buckets, K):
    if total_buckets > K:
        raise ValueError("Cannot create disjoint buckets when total_buckets > K.")
    lower = 1 + (index * K) // total_buckets
    upper = ((index + 1) * K) // total_buckets
    return lower, upper

def create_T(numberOfOptions=2, isKDevided=False):
    numberOfOptions = max(1, numberOfOptions) 
    def create_table(N, K):
        T = []
        for _ in range(N):
            options = []
            for i in range(numberOfOptions):
                if isKDevided:
                    lower, upper = bucket_bounds(i, numberOfOptions, K)
                    options.append(random.randint(lower, upper))
                else:
                    options.append(random.randint(1, K))
            T.append(tuple(options))
        return T
    return create_table

DEFAULT_T = create_T()

# test for what T looks like
# for i in range(2,9):
#     print(create_T(numberOfOptions=i, isKDevided=True)(1, 8))

# allows to fix some values in T, while randomizing the rest (UNUSED)
def partially_fixed_T(fixed_values, numberOfOptions=2, isKDevided=False):
    options_with_fixed_value = numberOfOptions - len(fixed_values)
    def create_table(N, K):
        T = []
        for i in range(N):
            options = list(fixed_values)
            for j in range(options_with_fixed_value):
                if isKDevided:
                    lower, upper = bucket_bounds(j, options_with_fixed_value, K)
                    options.append(random.randint(lower, upper))
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
    if verbose: print(f"Player {player1.thinking_steps if turnSwitch else player2.thinking_steps} starts first.")
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
    for player in [player1, player2]:
        if player.thinking_steps == winner_steps:
            player.wins += 1
    results[winner_steps] = results.get(winner_steps, 0) + 1
    return results


def play_tournament(players, N, K, NUMBER_OF_GAMES, create_T=DEFAULT_T, verbose=False):
    results = { player.thinking_steps: 0 for player in players } # dict of how may games players have won
    games_played = { player.thinking_steps: 0 for player in players } # dict of how many games players have played
    computation_steps = { player.thinking_steps: 0 for player in players } # dict of how much memory players have used
    number_of_guaranteed_wins = { player.thinking_steps: 0 for player in players } # dict of how many guaranteed wins players have
    for i in range(len(players)):
        for j in range(i+1, len(players)):
            for _ in range(NUMBER_OF_GAMES):
                games_played[players[i].thinking_steps] = games_played.get(players[i].thinking_steps, 0)+1
                games_played[players[j].thinking_steps] = games_played.get(players[j].thinking_steps, 0)+1
                results: dict[int, int] = play_round(N, K, players[i], players[j], results, create_T=create_T, verbose=verbose)
                computation_steps[players[i].thinking_steps] += players[i].computation_steps[-1]
                computation_steps[players[j].thinking_steps] += players[j].computation_steps[-1]
                # check if a player only made guaranteed winning moves
                if players[i].played_only_winning_moves:
                    number_of_guaranteed_wins[players[i].thinking_steps] += 1
                if players[j].played_only_winning_moves:
                    number_of_guaranteed_wins[players[j].thinking_steps] += 1
    thinking_times = {player.thinking_steps: player.thinking_times for player in players}
    computation_steps = {player.thinking_steps: player.computation_steps for player in players}
    return results, games_played, thinking_times, computation_steps, number_of_guaranteed_wins