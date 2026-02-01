from game import create_T
from players import Player

N = 23
K = 4
NUMBER_OF_GAMES = 100
NUMBER_OF_PLAYERS = 2
VERBOSE = False

def create_players():
    players = []
    for i in range(NUMBER_OF_PLAYERS):
        players.append(Player(thinking_steps=i*30))
    return players

def play_tournament():
    players = create_players()
    results = {}
    for i in range(len(players)):
        for j in range(i+1, len(players)):
            for _ in range(NUMBER_OF_GAMES):
                T = create_T(N, K)
                players[i].think_ahead(N, T)
                players[j].think_ahead(N, T)
                winner_steps = play_game(N, T, players[i], players[j])
                results[winner_steps] = results.get(winner_steps, 0) + 1
    return results

def play_game(N, T, player1: Player, player2: Player):
    ns = 0
    s = 0
    turnSwitch = True
    while True:
        if VERBOSE: print(f"Position: {ns}")
        if VERBOSE: print(f"Options: {T[s]}")
        choice = player1.make_move(s, ns, T) if turnSwitch else player2.make_move(s, ns, T)
        if VERBOSE: print(f"Player {player1.thinking_steps if turnSwitch else player2.thinking_steps} chose: {choice}")
        ns += choice
        if ns >= N:
            if VERBOSE: print(f"Game over! Winner: {'Player 1' if not turnSwitch else 'Player 2'}")
            return player1.thinking_steps if not turnSwitch else player2.thinking_steps
        s += 1
        turnSwitch = not turnSwitch

def normalize_results(results):
    total_games = sum(results.values())
    normalized = {key: f"{round(value / total_games * 100)}%" for key, value in results.items()}
    return normalized

if __name__ == "__main__":
    results = play_tournament()
    results = normalize_results(results)
    for key, value in results.items():
        print(f"Player with {key} thinking steps won {value} games")