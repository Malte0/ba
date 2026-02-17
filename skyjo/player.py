
from card import Card
from deck import Card_Deck

class Player:
    card_grid: list[list[Card]] = []

    def __init__(self, deck: Card_Deck):
        for row_index in range(3):
            self.card_grid.append([])
            for column_index in range(4):
                card = Card(deck.draw_card())
                self.card_grid[row_index].append(card)
        
    def print_grid(self):
        for row in self.card_grid:
            row_string = ""
            for card in row:
                row_string += f" {card.value}".rjust(3, " ") if card.is_open() else "[ ]"
            print(row_string)

    def open_card(self, row, column):
        self.card_grid[row][column].open_up()