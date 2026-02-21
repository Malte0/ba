
from card import Card
from deck import Card_Deck
from game import Game
from player import Player
from strategy import simple_strategy, start_random

# def firstStrategy(open_card: Card, otherPlayersOpenCards: list[Card], playerToTheLeft: Player, ):

def main():
    print("start")
    deck = Card_Deck()
    player1 = Player(deck, "Justin")
    player2 = Player(deck, "Good Player", startingMove=start_random, moveStrategy=simple_strategy)
    player3 = Player(deck, "Taylor")
    game = Game([player1, player2, player3], deck)
    game.start_game()

if __name__ == "__main__":
    main()