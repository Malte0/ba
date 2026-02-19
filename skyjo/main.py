
from card import Card
from deck import Card_Deck
from game import Game
from player import Player

# def firstStrategy(open_card: Card, otherPlayersOpenCards: list[Card], playerToTheLeft: Player, ):

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


def main():
    average_starting_points()
    # print("start")
    # deck = Card_Deck()
    # player1 = Player(deck, "Justin")
    # player2 = Player(deck, "Thomas")
    # player3 = Player(deck, "Martha")
    # game = Game([player1, player2, player3], deck)
    # game.start_game()

if __name__ == "__main__":
    main()