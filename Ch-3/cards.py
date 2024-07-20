import random


class DeckOfCards:
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    RANKS = [
        "Ace",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
    ]

    def __init__(self):
        self.__cards = []
        self.create_deck() # Call create_deck to populate the list with cards

    def create_deck(self):
        for suit in self.SUITS:  # Iterate over each suit
            for rank in self.RANKS:  # Iterate over each rank
                # Append a tuple (rank, suit) to the list of cards
                self.__cards.append((rank, suit))

    def shuffle_deck(self):
        random.shuffle(self.__cards)

    def deal_card(self):
        if self.__cards:  # Check if there are any cards left in the deck
            return self.__cards.pop()  # Remove and return the last card (top of the deck)
        else:
            return None  # Return None if the deck is empty

    # don't touch below this line

    def __str__(self):
        return f"The deck has {len(self.__cards)} cards"
