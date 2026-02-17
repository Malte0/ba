
class Card:
    def __init__(self, card_value):
        self.value = card_value
        self.open = False
    
    def open_up(self):
        self.open = True
    
    def is_open(self):
        return self.open