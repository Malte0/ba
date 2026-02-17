from random import randrange

class Card_Deck:
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
        for key, value in self.cards.items():
            current_count += value
            if random_card_index <= current_count:
                self.cards[key] = self.cards[key]-1
                return key

    def print_deck(self):
        for key, value in self.cards.items():
            print(f"{key}: {value}")