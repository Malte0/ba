
from deck import Card_Deck
from player import Player

def average_starting_points():
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