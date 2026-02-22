
from card import Card
from deck import Card_Deck
from player import Player

class Game:
    middle_card: Card
    card_deck: Card_Deck
    players: list[Player]
    number_of_rounds: int = 1
    results: dict[str, list[int]] = {}
    verbose = False

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
        
        for _ in range(self.number_of_rounds):
            self.play(index_of_player_with_most_points)
            self.save_results()
            self.reset_game()
        self.print_results()
        
        
    def play(self, index_of_player_with_most_points):
        last_index_to_play = 10000
        last_round = False

        current_player_index = index_of_player_with_most_points
        while current_player_index < last_index_to_play:
            player_to_move: Player = self.players[current_player_index % len(self.players)]
            # Draw or take middle card
            # if draw, take card or open card

            self.middle_card.open_up() # just to make sure it's open
            if self.verbose:
                print(f"{player_to_move.name}")
                print(f"Middle {self.middle_card.value}")
                print(player_to_move.print_grid())
            new_middle_card = player_to_move.makeMove(player_to_move, self.middle_card, self.card_deck)
            if self.verbose:
                print("After Move:")
                print(player_to_move.print_grid())
                print("==============================")
            self.middle_card = new_middle_card

            if player_to_move.has_finished() and not last_round:
                last_index_to_play = current_player_index + len(self.players)-1
                last_round = True
            current_player_index += 1

    def reset_game(self):
        self.card_deck = Card_Deck()
        for player in self.players:
            player.card_grid = []
            player.draw_grid(self.card_deck)
        self.middle_card = Card(self.card_deck.draw_card())


    def save_results(self):
        for player in self.players:
            player.open_all_cards()
            open_points = player.open_points()
            if player.name not in self.results:
                self.results[player.name] = []
            self.results[player.name].append(open_points)
            if self.verbose:
                print(f"{player.name}: {open_points}")
    
    def print_results(self):
        for player_name in self.results:
            points = sum(self.results[player_name]) // len(self.results[player_name])
            print(f"{player_name}: {points}")
        
        lowest_score = 10000
        lowest_player = ""
        for player_name in self.results:
            for score in self.results[player_name]:
                if score < lowest_score:
                    lowest_score = score
                    lowest_player = player_name
        print(f"Lowest Score: {lowest_score} by {lowest_player}")
