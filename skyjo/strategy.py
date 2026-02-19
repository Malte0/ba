
import random

def open_random_card(player):
    closed_cards = []
    for row_index in range(3):
        for column_index in range(4):
            if not player.card_grid[row_index][column_index].is_open:
                closed_cards.append([row_index, column_index])
    
    if len(closed_cards) == 0:
        player.print_grid()
        return

    random_card = random.choice(closed_cards)
    player.open_card(random_card[0],random_card[1])

def start_random(player):
    open_random_card(player)
    open_random_card(player)
