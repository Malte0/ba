
from deck import Card_Deck

class Game:
    def __init__(self, number_of_players, card_deck: Card_Deck):
        self.number_of_players = number_of_players
        print(card_deck.cards_left())
        self.deal_cards()
    
    def deal_cards(self):
        pass