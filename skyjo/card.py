
class Card:
    is_open = False

    def __init__(self, card_value):
        self.value = card_value
    
    def open_up(self):
        self.is_open = True
    