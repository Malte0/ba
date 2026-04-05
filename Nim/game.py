import random
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
    results = {} # dict of how may games players have won
    games_played = {} # dict of how many games players have played
    for i in range(len(players)):
        print(f"Running at step {i} of {len(players)}")
        for j in range(i+1, len(players)):
            for _ in range(NUMBER_OF_GAMES):
                games_played[players[i].thinking_steps] = games_played.get(players[i].thinking_steps, 0)+1
                games_played[players[j].thinking_steps] = games_played.get(players[j].thinking_steps, 0)+1
                results = play_round(N, K, players[i], players[j], results, create_T=create_T)
    # thinking_times = {player.thinking_steps: player.thinking_times for player in players}
    thinking_times = {player.thinking_steps: player.thinking_times for player in players}
    return results, games_played, thinking_times