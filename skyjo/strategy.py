
import random

from card import Card
from deck import Card_Deck
from utils import allCardsLowerThan, find_closed_cards, findHighestCardInGrid

# only take low cards and replace high cards
def simple_strategy(player, middle_card: Card, card_deck: Card_Deck):
    my_grid = player.card_grid
    new_middle_card = middle_card
    if middle_card.value in [-2, -1, 0, 1, 2]:
        if allCardsLowerThan(my_grid, 4):
            # replaces a random closed card
            closed_cards = find_closed_cards(my_grid)
            card_to_replace = random.choice(closed_cards)
            new_middle_card = my_grid[card_to_replace[0]][card_to_replace[1]]
            my_grid[card_to_replace[0]][card_to_replace[1]] = middle_card
        else:
            highest_card_cords = findHighestCardInGrid(my_grid)
            new_middle_card = my_grid[highest_card_cords[0]][highest_card_cords[1]]
            my_grid[highest_card_cords[0]][highest_card_cords[1]] = middle_card
    else: 
        drawn_card = Card(card_deck.draw_card())
        if drawn_card.value < 4:
            if allCardsLowerThan(my_grid, 4):
                # replaces a random closed card
                closed_cards = find_closed_cards(my_grid)
                card_to_replace = random.choice(closed_cards)
                new_middle_card = my_grid[card_to_replace[0]][card_to_replace[1]]
                my_grid[card_to_replace[0]][card_to_replace[1]] = drawn_card
            else:
                highest_card_cords = findHighestCardInGrid(my_grid)
                new_middle_card = my_grid[highest_card_cords[0]][highest_card_cords[1]]
                my_grid[highest_card_cords[0]][highest_card_cords[1]] = drawn_card
        else:
            new_middle_card = drawn_card
            closed_cards = find_closed_cards(my_grid)
            choice = random.choice(closed_cards)
            random_closed_card = my_grid[choice[0]][choice[1]]
            random_closed_card.open_up()
    new_middle_card.open_up()
    return new_middle_card

def open_random_card(player, middle_card: Card, card_deck: Card_Deck):
    if card_deck:
        new_middle_card = Card(card_deck.draw_card())
    closed_cards = []
    for row_index in range(3):
        for column_index in range(4):
            if not player.card_grid[row_index][column_index].is_open:
                closed_cards.append([row_index, column_index])
    
    random_card = random.choice(closed_cards)
    player.open_card(random_card[0],random_card[1])
    if card_deck:
        return new_middle_card

def start_random(player):
    open_random_card(player, None, None)
    open_random_card(player, None, None)
