#===============================================================================
# PyDealer - Card Deck Simulator
#-------------------------------------------------------------------------------
# Version: 1.1.0
# Updated: 22-06-2014
# Author: Alex Crawford
# License: MIT
#===============================================================================

"""
A simple package with classes for constructing a ``Deck`` object, of 52 common 
playing cards. Each card is a separate ``Card`` object, with a name, value, 
suit, and abbreviation. Has methods for shuffling the deck, dealing from the 
deck, peeking at cards in the deck, and finding the locations of all the cards 
of a given name, abbreviation, value, or suit in the deck.

The MIT License (MIT)

Copyright (c) 2014 Alex Crawford

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

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
    NUMBERS = ["2", "3", "4", "5", "6", "7", "8", "9", "10"]

    def __init__(self, jokers=False, num_jokers=2):
        """Deck init method."""

        self.cards = []
        self.decks_used = 0

        self.build(jokers, num_jokers)

    def build(self, jokers=False, num_jokers=2):
        """
        Builds a standard 52 card French deck of card objects.

        :returns: A new deck object.

        """
        self.decks_used += 1

        temp_deck = [
            Card(number, suit) for number in self.NUMBERS for 
            suit in self.SUITS
        ]
        temp_deck.extend(
            [
                Card(face, suit) for face in self.FACES for 
                suit in self.SUITS
            ]
        )
        temp_deck.extend([Card("Ace", suit) for suit in self.SUITS])

        if jokers:
            temp_deck.extend([Card("Joker", None) for i in xrange(num_jokers)])

        self.cards = temp_deck[::-1]

    def check_term(self, card, term):
        """
        Checks a given search term against a given card's name attributes.

        :returns: True/False, depending on the check.

        """
        check_list = [
            card.name.lower(), card.suit.lower(), card.value.lower(), 
            card.abbrev[0].lower(), card.abbrev[1].lower(), 
            card.abbrev[0:2].lower()
        ]

        term = term.lower()

        for check in check_list:
            if check == term:
                return True

    def deal(self, num=1, rebuild=True):
        """
        Returns a list of cards, which are removed from the deck.

        :returns: A given number of cards from the deck.

        """
        cards = []

        while num:
            if self.size:
                card = self.cards.pop()
                cards.append(card)
                num -= 1
            elif rebuild:
                self.build()
                self.shuffle()
            else:
                break
   
        return cards

    def find(self, terms):
        """
        Searches the deck for cards with a suit, value, name, or
        abbreviation matching the given argument, 'terms'.

        :returns: A list of deck indices for the cards matching the given terms, 
            if found.

        """
        if type(terms) != list:
            found_cards = [
                self.cards.index(x) for x in self.cards if 
                self.check_term(x, terms)
            ]
        else:
            found_cards = [
                self.cards.index(x) for x in self.cards for y in terms if 
                self.check_term(x, y) 
            ]

        return found_cards

    def get(self, terms):
        """
        Get the specified cards from the deck.

        :returns: A list of the specified cards, if found.

        """
        got_cards = []

        if type(terms) != list:
            index = self.find(terms)
            if index:
                got_cards.extend([self.cards[i] for i in index])
        else:
            for item in terms:
                index = self.find(item)
                if index:
                    got_cards.extend(
                        [self.cards[i] for i in index if 
                        self.cards[i] not in got_cards]
                    )

        for card in got_cards:
            self.cards.remove(card)

        return got_cards

    def peek(self, position, ret_value="card"):
        """
        Peek at the card in the given position (list index) of the deck.

        :returns: The card at the given deck index.

        """
        return_vals = {
            "name": self.cards[position].name,
            "abbrev": self.cards[position].abbrev,
            "value": self.cards[position].value,
            "face": self.cards[position].value,
            "suit": self.cards[position].suit,
            "card": self.cards[position]
        }

        return return_vals[ret_value]

    def shuffle(self):
        """Shuffles the deck."""

        random.shuffle(self.cards)

    @property
    def size(self):
        """
        Counts the number of cards currently in the deck.

        :returns: The number of cards in the deck.

        """
        return len(self.cards)

#===============================================================================
# CARD CLASS
#===============================================================================

class Card(object):
    """The Card class, representing a single card."""

    def __init__(self, value, suit):
        """Card constructor method."""

        self.value = value
        self.suit = str(suit).capitalize()
        self.abbrev = self.gen_abbrev(value, suit)
        self.name = self.gen_name(value, suit)

    def gen_abbrev(self, value, suit):
        """
        Constructs an abbreviation for the card, using the given 
        value, and suit.

        :returns: A newly constructed abbreviation, made using the given value
            & suit

        """
        value_str = str(value)
        val_type = type(value)

        if val_type is str:
            if value != "Joker":
                return "%s%s" % (value_str[0], suit[0])
            else:
                return "%s%s" % (value_str[0], "K")
        elif val_type is int:
            return "%s%s" % (value_str, suit[0])

    def gen_name(self, value, suit):
        """
        Constructs a name for the card, using the given value, 
        and suit.

        :returns: a newly constructed name, using the given value & suit.

        """
        if value != "Joker":
            return "%s of %s" % (str(value), suit)
        else:
            return value

#===============================================================================
# IF '__MAIN__'
#===============================================================================

if __name__ == '__main__':
    pass
