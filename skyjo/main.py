
from deck import Card_Deck
from game import Game
from player import Player

if __name__ == "__main__":
    print("start")
    deck = Card_Deck()
    player = Player(deck)
    player.open_card(0,0)
    player.open_card(2,3)
    player.open_card(1,2)
    player.print_grid()