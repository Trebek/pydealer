#===============================================================================
# PyDealer - Card Deck Simulator
#-------------------------------------------------------------------------------
# Version: 1.0.0
# Updated: 25-01-2014
# Author: Alex Crawford
# License: MIT
#===============================================================================

"""
A module for simulating a French deck of 52 playing cards (common playing 
cards). Each card is a separate object with a name, abbreviation, value, and 
suit. Has methods for shuffling the deck, dealing from the deck, peeking at 
cards in the deck, and finding the locations of all the cards of a given name, 
abbreviation, value, or suit in the deck. 

"""

#===============================================================================
# IMPORTS
#===============================================================================

import random

#===============================================================================
# DECK CLASS
#===============================================================================

class Deck(object):
    """Deck class, representing the deck that the cards will be in."""

    SUITS = ["Spades", "Hearts", "Diamonds", "Clubs"]
    FACES = ["King", "Queen", "Jack"]
    NUMBERS = [2, 3, 4, 5, 6, 7, 8, 9, 10]

    def __init__(self):
        """Deck constructor method."""

        self.cards = []
        self.decks_used = 0
        
    def build_deck(self):
        """Builds a standard 52 card French deck of card objects."""
        
        cards_left = 52
        temp_deck = []

        self.decks_used += 1

        while cards_left > 0:
            for number in self.NUMBERS:
                for suit in self.SUITS:
                    temp_deck.append(Card(number, suit))
                    cards_left -= 1
            for face in self.FACES:
                for suit in self.SUITS:
                    temp_deck.append(Card(face, suit))
                    cards_left -= 1
            for suit in self.SUITS:
                temp_deck.append(Card('Ace', suit))
                cards_left -= 1

        self.cards = temp_deck[::-1]

    def deal(self, num=1, rebuild=True):
        """Returns a list of cards, which are removed from the deck."""

        cards = []
        left_to_deal = num

        while left_to_deal > 0:
            if self.size > 0:
                card = self.cards.pop()
                cards.append(card)
                left_to_deal -= 1
            elif rebuild:
                self.build_deck()
                self.shuffle()
            else:
                break
   
        return cards

    def find_cards(self, term):
        """Searches the deck for cards with a suit, value, name, or
        abbreviation matching the given argument, 'search_term'.

        """
        found_cards = []

        for card in self.cards:
            if (card.suit == term or card.value == term or 
                    card.name == term or card.abbrev == term):
                found_cards.append(self.cards.index(card))

        return found_cards

    def peek(self, position, ret_value="name"):
        """Peek at the card in the given position (list index) of the deck."""

        if ret_value == "name":
            return self.cards[position].name
        elif ret_value == "abbrev":
            return self.cards[position].abbrev
        elif ret_value == "value":
            return self.cards[position].value
        elif ret_value == "suit":
            return self.cards[position].suit

    def shuffle(self):
        """Shuffles the deck."""

        random.shuffle(self.cards)

    @property
    def size(self):
        """Returns the number of cards currently in the deck."""

        return len(self.cards)

#===============================================================================
# CARD CLASS
#===============================================================================

class Card(object):
    """The Card class, representing a single card."""

    def __init__(self, value, suit):
        """Card constructor method."""

        self.value = value
        self.suit = suit.capitalize()
        self.abbrev = self.gen_abbrev(value, suit)
        self.name = self.gen_name(value, suit)

    def gen_abbrev(self, value, suit):
        """Constructs an abbreviation for the card, using the given 
        value, and suit.

        """
        value_str = str(value)

        if type(value) is str:
            return "{0}{1}".format(value_str[0], suit[0])
        elif type(value) is int:
            return "{0}{1}".format(value_str, suit[0])

    def gen_name(self, value, suit):
        """Constructs a name for the card, using the given value, 
        and suit.

        """
        return "{0} of {1}".format(str(value), suit)

#===============================================================================
# IF __NAME__ == '__MAIN__'
#===============================================================================

if __name__ == '__main__':
    pass
