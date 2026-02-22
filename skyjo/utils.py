
from card import Card
from deck import Card_Deck

def allCardsLowerThan(card_grid: list[list[Card]], max_value):
    for row in card_grid:
        for card in row:
            if card.value >= max_value and card.is_open:
                return False
    return True

def findHighestCardInGrid(card_grid: list[list[Card]]):
    highest_value = -2
    card_cords = []
    for row_index in range(3):
        for column_index in range(4):
            card = card_grid[row_index][column_index]
            if card.value > highest_value and card.is_open:
                highest_value = card.value
                card_cords = [row_index, column_index]
    return card_cords

def find_closed_cards(card_grid: list[list[Card]]) -> list[list[int]]:
    closed_cards = []
    for row_index in range(3):
        for column_index in range(4):
            card = card_grid[row_index][column_index]
            if not card.is_open:
                closed_cards.append([row_index, column_index])
    return closed_cards


def average_starting_points():
    from player import Player
    SAMPLE_SIZE = 1000
    points = []
    for _ in range(SAMPLE_SIZE):
        deck = Card_Deck()
        player = Player(deck, "Justin")
        player.open_all_cards()
        starting_points = player.open_points()
        points.append(starting_points)
    
    print("Average starting points:")
    print(round(sum(points) / len(points)))

def average_card_value():
    value_total = 0
    deck = Card_Deck()
    for card_value, card_count in deck.cards.items():
        value_total += card_value * card_count
    
    return round(value_total / deck.cards_left())

AVG_CARD_VALUE = average_card_value()