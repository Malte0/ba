from game import create_T
from players import Player, create_players
import random
import matplotlib.pyplot as plt

N = 100
K = 8
NUMBER_OF_GAMES = 1000
NUMBER_OF_PLAYERS = 8
def player_thinking_steps(player_index): 
    return 79+player_index*3
VERBOSE = False

def play_round(player1: Player, player2: Player, results):
    T = create_T(N, K)
    player1.plan_ahead(N, T)
    player2.plan_ahead(N, T)
    winner_steps = play_game(N, T, player1, player2)
    results[winner_steps] = results.get(winner_steps, 0) + 1
    return results

def play_tournament():
    players = create_players(NUMBER_OF_PLAYERS, player_thinking_steps)
    results = {} # dict of how may games players have won
    games_played = {} # dict of how many games players have played
    for i in range(len(players)):
        for j in range(i+1, len(players)):
            for _ in range(NUMBER_OF_GAMES):
                games_played[players[i].thinking_steps] = games_played.get(players[i].thinking_steps, 0)+1
                games_played[players[j].thinking_steps] = games_played.get(players[j].thinking_steps, 0)+1
                results = play_round(players[i], players[j], results)
    return results, games_played

def play_game(N, T, player1: Player, player2: Player):
    ns = 0
    s = 0
    turnSwitch = random.choice([True, False])
    while True:
        choice = player1.make_move(N, s, ns, T) if turnSwitch else player2.make_move(N, s, ns, T)
        if VERBOSE: print(f"Ns: {ns} - Ts: {T[s]} - Step: {s}")
        if VERBOSE: print(f"Player {player1.thinking_steps if turnSwitch else player2.thinking_steps} chose: {choice}")
        ns += choice
        if ns >= N:
            if VERBOSE: print(f"Game over! Winner: {player1.thinking_steps if turnSwitch else player2.thinking_steps}")
            return player1.thinking_steps if turnSwitch else player2.thinking_steps
        s += 1
        turnSwitch = not turnSwitch

if __name__ == "__main__":
    X = range(10)
    results, games_played = play_tournament()
    plot_x = [key for key, value in results.items()]
    plot_y = [round((value / games_played[key]) * 100, 2) for key, value in results.items()]
    for key, value in results.items():
        player_win_percentage = round((value / games_played[key]) * 100, 2)
        print(f"Player with {key} thinking steps won {player_win_percentage}% games")

    plt.plot(plot_x, plot_y)
    plt.show()