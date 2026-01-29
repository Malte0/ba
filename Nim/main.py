from game import create_T
from players import Player

N = 23
K = 5

def construct_game():
    T = create_T(N, K)
    player1 = Player(0)
    player2 = Player(0)
    print(play_game(N, T, player1, player2))

def play_game(N,T, player1: Player, player2: Player):
    ns = 0
    s = 0
    turnSwitch = True
    while ns < N:
        print(f"Position: {ns}")
        print(f"Options: {T[s]}")
        if turnSwitch:
            choice = player1.make_move(ns, s, T)
            print(f"Player 1 chose: {choice}")
            ns += choice
        else:
            choice = player2.make_move(ns, s, T)
            print(f"Player 2 chose: {choice}")
            ns += choice
        turnSwitch = not turnSwitch
        s += 1
        if ns >= N:
            return "Player 1 wins" if not turnSwitch else "Player 2 wins"


if __name__ == "__main__":
    construct_game()