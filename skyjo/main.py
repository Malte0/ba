
from deck import Card_Deck
from game import Game
from player import Player
import random

def open_random_card(player: Player):
    closed_cards = []
    for row_index in range(3):
        for column_index in range(4):
            if not player.card_grid[row_index][column_index].is_open():
                closed_cards.append([row_index, column_index])

    random_card = random.choice(closed_cards)
    player.open_card(random_card[0],random_card[1])

if __name__ == "__main__":
    print("start")
    deck = Card_Deck()
    player = Player(deck)
    open_random_card(player)
    open_random_card(player)
    player.print_grid()