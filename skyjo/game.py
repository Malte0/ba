
from card import Card
from deck import Card_Deck
from player import Player

class Game:
    middle_card: Card
    card_deck: Card_Deck
    players: list[Player]

    def __init__(self, players: list[Player], card_deck: Card_Deck):
        self.players = players
        self.card_deck = card_deck
        self.middle_card = Card(card_deck.draw_card())

    def start_game(self):
        # all players make opening move
        for player in self.players:
            player.makeStartingMove(player)
        # choose starting player who has the most points
        most_open_points = -100
        index_of_player_with_most_points = None
        for i in range(len(self.players)):
            player = self.players[i]
            open_points = player.open_points()
            if open_points > most_open_points:
                most_open_points = open_points
                index_of_player_with_most_points = i
        
        self.play(index_of_player_with_most_points)
        
    def play(self, index_of_player_with_most_points):
        last_index_to_play = 10000
        last_round = False

        current_player_index = index_of_player_with_most_points
        while current_player_index < last_index_to_play:
            player_to_move: Player = self.players[current_player_index % len(self.players)]
            # Draw or take middle card
            # if draw, take card or open card

            new_middle_card = player_to_move.makeMove(player_to_move, self.middle_card, self.card_deck)
            self.middle_card = new_middle_card

            if player_to_move.has_finished() and not last_round:
                last_index_to_play = current_player_index + len(self.players)-1
                last_round = True
            current_player_index += 1
        
        self.print_results()

    def print_results(self):
        results = {}
        for player in self.players:
            player.open_all_cards()
            open_points = player.open_points()
            results[player.name] = open_points
        print(results)