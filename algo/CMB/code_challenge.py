import random


class Player:

    def __init__(self, name=None, deck = []):
        self.name = name
        self.deck = deck

    def sort(self):
        print(self.deck)
        self.deck.sort(key=lambda card: card[1])
        print(self.deck)
        self.deck = sorted(self.deck, key=lambda card: str(card[0]))
        print(self.deck)

    def __repr__(self) -> str:
        res = ' '
        for card in self.deck:
            res += f'{card},'

        return self.name + res[:len(res)-1]

class Game:

    def __init__(self) -> None:
        self.players = []
        self.winner = None


class Deck:
    """A class that represents a deck of 52 playing cards"""

    def __init__(self):
        self.types = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
        self.irregular_types = ['Jack', 'Queen', 'King', 'Ace']
        self.deck = []

        for type in self.types:
            for i in range(1, 10):
                self.deck.append((i + 1, type))

        for type in self.types:
            for irr_type in self.irregular_types:
                self.deck.append((irr_type, type))

    def __str__(self) -> str:
        result = ''
        for card, card_type in self.deck:
            result += f'{card} of {card_type},'

        return result[:len(result) - 1]

    def shuffle(self, amount: int):
        for _ in range(amount):
            random.shuffle(self.deck)

    def deal(self, *players):
        game = Game()

        for player, amount_of_cards in players:
            cards = []
            for _ in range(amount_of_cards):
                cards.append(self.deck.pop())
            game.players.append(Player(player, cards))

        return game

    def __len__(self):
        return len(self.deck)


# initializes a deck of 52 playing cards
# i.e.: thirteen ranks (2, 3, ..., 10, J, Q, K, A) of four suits (Spades, Hearts, Diamonds, Clubs)
deck = Deck()

# shuffles the deck some number of times
deck.shuffle(3)

# prints "Deck contains: A of Spades, 8 of Hearts, 3 of Diamonds, etc"
print(f'Deck contains: {deck}')

# creates a game with 2 or more players and deals some number of cards from the deck to each player's hand
game = deck.deal(("Erik Sidel", 5), ("Phil Ivy", 5))

# print the number of cards left in the deck
print(f'{len(deck)} cards left in the deck')

# sort all the cards first by suit, then by rank (face card)
# suits are sorted alphabetically (highest to lowest): Spades, Hearts, Diamonds, Clubs
for player in game.players:
    player.sort()

# # prints "Erik Sidel's hand: 8 of Spades, 10 of Spades, J of Spades, etc" for each player
print('\n'.join([str(player) for player in game.players]))

# # print the name of the player who has the largest top card
# print(f'{game.winner.name} wins!')
