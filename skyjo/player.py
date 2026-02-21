
from card import Card
from deck import Card_Deck
from strategy import open_random_card, start_random

class Player:
    card_grid: list[list[Card]] = []

    def __init__(self, deck: Card_Deck, name, startingMove=start_random, moveStrategy=open_random_card):
        self.name = name
        self.card_grid = []
        self.makeStartingMove=startingMove
        self.makeMove=moveStrategy
        for row_index in range(3):
            self.card_grid.append([])
            for column_index in range(4):
                card = Card(deck.draw_card())
                self.card_grid[row_index].append(card)
        
    def print_grid(self):
        for row in self.card_grid:
            row_string = ""
            for card in row:
                row_string += f" {card.value}".rjust(3, " ") if card.is_open else "[ ]"
            print(row_string)
    
    def has_finished(self):
        for row in self.card_grid:
            for card in row:
                if not card.is_open:
                    return False
        return True

    def open_card(self, row, column):
        self.card_grid[row][column].open_up()

    def open_all_cards(self):
        for row in self.card_grid:
            for card in row:
                card.open_up()
    
    def open_points(self):
        points = sum([card.value for row in self.card_grid for card in row if card.is_open])
        return points
    
    def makeStartingMove(self, player):
        start_random(player)

    def makeMove(self, player, middle_card, card_deck):
        open_random_card(player, middle_card, card_deck)
    