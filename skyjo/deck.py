from random import randrange

class Card_Deck:
    # [card_value: amount_of_cards]
    cards = {}

    def __init__(self):
        self.cards[-2] = 5
        self.cards[-1] = 10
        self.cards[0] = 15
        for card_value in range(1, 13):
            self.cards[card_value] = 10

    def cards_left(self):
        return sum([value for key, value in self.cards.items()])
    
    def draw_card(self):
        random_card_index = randrange(self.cards_left())+1
        current_count = 0
        for card_value, card_count in self.cards.items():
            current_count += card_count
            if random_card_index <= current_count:
                self.cards[card_value] = self.cards[card_value]-1
                return card_value

    def print_deck(self):
        for key, value in self.cards.items():
            print(f"{key}: {value}")