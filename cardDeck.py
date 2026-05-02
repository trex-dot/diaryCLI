import random

class Card:
  
    RANK_ORDER = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
        '7': 7, '8': 8, '9': 9, '10': 10,
        'J': 11, 'Q': 12, 'K': 13, 'A': 14
    }

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        names = {'J': 'Jack', 'Q': 'Queen', 'K': 'King', 'A': 'Ace'}
        rank_name = names.get(self.rank, self.rank)
        return f"{rank_name} of {self.suit}"

    def __repr__(self):
        return f"Card('{self.rank}', '{self.suit}')"

    def __eq__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return self.rank == other.rank and self.suit == other.suit

    def __lt__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return Card.RANK_ORDER[self.rank] < Card.RANK_ORDER[other.rank]         
class Deck:
    SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    RANKS = ['2', '3', '4', '5', '6', '7', '8',
             '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self):
        # create all 52 cards
        self.cards = [Card(rank, suit) 
                      for suit in Deck.SUITS 
                      for rank in Deck.RANKS]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, n):
        dealt = self.cards[:n]
        self.cards = self.cards[n:]
        return dealt

    @property
    def cards_remaining(self):
        return len(self.cards)

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        return f"Deck with {len(self.cards)} cards remaining"