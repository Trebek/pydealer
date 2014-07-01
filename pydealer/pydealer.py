#===============================================================================
# PyDealer: Playing Card Package
#-------------------------------------------------------------------------------
# Version: 1.2.2
# Updated: 30-06-2014
# Author: Alex Crawford
# License: MIT
#===============================================================================

"""
A simple package with classes for constructing a ``Deck`` object, of 52 common 
playing cards. Each card is a separate ``Card`` object, with a name, value, 
suit, and abbreviation. Has methods for shuffling the deck, dealing from the 
deck, peeking at cards in the deck, and finding the locations of all the cards 
of a given name, abbreviation, value, or suit in the deck.

"""

# The MIT License (MIT)

# Copyright (c) 2014 Alex Crawford

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

#===============================================================================
# Imports
#===============================================================================

import random

#===============================================================================
# Global Constants
#===============================================================================

SUITS = ["Spades", "Hearts", "Diamonds", "Clubs"]
FACES = ["King", "Queen", "Jack"]
NUMBERS = ["2", "3", "4", "5", "6", "7", "8", "9", "10"]

POKER_RANKS = {
    "Ace": 13,
    "King": 12,
    "Queen": 11,
    "Jack": 10, 
    "10": 9,
    "9": 8,
    "8": 7,
    "7": 6,
    "6": 5,
    "5": 4, 
    "4": 3,
    "3": 2,
    "2": 1
}
BIG2_RANKS = {
    "values": POKER_RANKS,
    "suits": {
        "Spades": 4,
        "Hearts": 3,
        "Clubs": 2,
        "Diamonds": 1
    }
}
BLACKJACK_VALS = {
    "Ace": (1, 11),
    "King": 10,
    "Queen": 10,
    "Jack": 10, 
    "10": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5, 
    "4": 4,
    "3": 3,
    "2": 2
}

#===============================================================================
# Deck Class
#===============================================================================

class Deck(object):
    """Deck class, representing the deck that the cards will be in."""

    def __init__(self, jokers=False, num_jokers=2, build=True):
        """
        Deck constructor method.

        :param jokers: Whether or not to include jokers in the deck.
        :type jokers: Bool.
        :param num_jokers: How many jokers to add to the deck.
        :type num_jokers: Int.
        :param build: Whether or not to build the deck on instantiation.
        :type build: Bool.

        """
        self.cards = []
        self.decks_used = 0

        if build:
            self.build(jokers, num_jokers)

    def __add__(self, other):
        """
        Allows you to add (merge) decks together, with the ``+`` operand.

        :param other: The other deck to add to the deck.
        :type other: Deck.

        :returns: A new Deck object, with the combined cards.

        """
        new_deck = Deck(build=False)
        new_deck.cards = self.cards + other.cards
        return new_deck

    def __contains__(self, card):
        """
        Allows for Card object (not suit & value) inclusion checks.

        :param card: The Card object to check for.
        :type card: Card.

        :returns: Whether or not the Card is in the Deck.

        """
        id_list = [id(x) for x in self.cards]
        return id(item) in id_list

    def __delitem__(self, indice):
        """
        Allows for deletion of a Card object, using del.

        :param indice: The indice to delete.
        :type indice: int.

        """
        del self.cards[indice]

    def __eq__(self, other):
        """
        Allows for Deck ordering comparisons.

        :param other: The other Deck to compare to.
        :type other: Deck.

        :returns: Whether or not the decks are in the same order.

        """
        return (isinstance(other, Deck) and self.cards == other.cards)

    def __getitem__(self, indice):
        """
        Allows for getting of cards, using ``Deck[indice]``.

        :param indice: The indice to get.
        :type indice: int.

        :returns: The Card at the given indice.

        """
        return self.cards[indice]

    def __iter__(self):
        """
        Allows looping through the Deck, using for loops.

        :returns: An iterator of the Cards in the deck.

        """
        for card in self.cards:
            yield card

    def __len__(self):
        """
        Allows check the deck length, with len.

        :returns: The length of the deck (self.cards).

        """
        return len(self.cards)

    def __repr__(self):
        """
        The repr magic method.

        :returns: A string representation of the Deck object.

        """
        return 'Deck(cards=%r)' % (self.cards)

    def __setitem__(self, indice, value):
        """
        Allows you to assign cards to specific deck indices.

        :param indice: The indice to set.
        :type indice: int.
        :param value: The Card to set the indice to.
        :type value: Card.

        :returns: The Card at the given indice.

        """
        self.cards[indice] = value

    def __str__(self):
        """
        The str magic method.

        :returns: A str of the names of the cards in the deck.

        """
        card_names = "".join([x.name + "\n" for x in self.cards]).rstrip("\n")
        return '%s' % (card_names)

    def build(self, jokers=False, num_jokers=2):
        """
        Builds a standard 52 card French deck of card objects.

        :param jokers: Whether or not to include jokers in the deck.
        :type jokers: bool.
        :param num_jokers: The number of jokers to include.
        :type num_jokers: int.

        :returns: A new deck object.

        """
        self.decks_used += 1

        temp_deck = [
            Card(number, suit) for number in NUMBERS for 
            suit in SUITS
        ]
        temp_deck.extend(
            [
                Card(face, suit) for face in FACES for 
                suit in SUITS
            ]
        )
        temp_deck.extend([Card("Ace", suit) for suit in SUITS])

        if jokers:
            temp_deck.extend([Card("Joker", None) for i in xrange(num_jokers)])

        self.cards = temp_deck[::-1]

    def deal(self, num=1, rebuild=True):
        """
        Returns a list of cards, which are removed from the deck.

        :param num: The number of cards to deal.
        :type num: int.
        :param rebuild: Whether or not to rebuild the deck when cards run out.
        :type rebuild: bool.

        :returns: A given number of cards from the deck.

        """
        dealt_cards = []

        for n in xrange(num):
            if self.size == 0:
                if rebuild:
                    self.build()
                    self.shuffle()
                else:
                    break
                
            card = self.cards.pop()
            dealt_cards.append(card)
   
        return dealt_cards

    def find(self, terms):
        """
        Searches the deck for cards with a suit, value, name, or
        abbreviation matching the given argument, 'terms'.

        :param terms: The search terms. Can be card full names, suits, values,
            or abbreviations.
        :type terms: Str|list of str.

        :returns: A list of deck indices for the cards matching the given terms, 
            if found.

        """
        if type(terms) != list:
            terms = [terms]
        
        found_cards = [
            self.cards.index(x) for x in self.cards for y in terms if 
            check_term(x, y) 
        ]

        found_len = len(found_cards)

        if found_len > 1:
            return found_cards
        elif found_len > 0:
            return found_cards[0]
        else:
            return None

    def get(self, terms):
        """
        Get the specified cards from the deck.

        :param terms: The search terms. Can be card full names, suits, values,
            abbreviations, or deck indices.
        :type terms: str|int|list of str|int.

        :returns: A list of the specified cards, if found.

        """
        got_cards = []

        if type(terms) != list:
            terms = [terms]
            
        for item in terms:
            if type(item) is not int:
                indices = self.find(item)
                indices_type = type(indices)
                if indices_type is list:
                    got_cards.extend(
                        [
                            self.cards[i] for i in indices if 
                            self.cards[i] not in got_cards
                        ]
                    )
                elif indices:
                    got_cards.append(self.cards[indices])
            else:
                got_cards.append(self.cards[item])

        for card in got_cards:
            self.cards.remove(card)

        got_len = len(got_cards)

        if got_len > 1:
            return got_cards
        elif got_len > 0:
            return got_cards[0]
        else:
            return None

    def peek(self, indice, ret_val="card"):
        """
        Peek at the card in the given indice(s) (list index) of the deck.

        :param indice: The deck indice(s) to peek at.
        :type indice: int|list of ints.
        :param ret_value: What to return.
        :type ret_value: Str.

        :returns: The Card|name|suit|value|abbrev. at the given indice.

        """
        peeked = []

        if type(indice) is not list:
            indice = [indice]

        if ret_val is "card":
            for i in indice:
                peeked.append(self.cards[i])
        elif ret_val is "name":
            for i in indice:
                peeked.append(self.cards[i].name)
        elif ret_val in ["abbr", "abbrev", "abbreviation"]:
            for i in indice:
                peeked.append(self.cards[i].abbrev)
        elif ret_val in ["val", "value"]:
            for i in indice:
                peeked.append(self.cards[i].value)
        elif ret_val in "suit":
            for i in indice:
                peeked.append(self.cards[i].suit)

        peeked_len = len(peeked)

        if peeked_len > 1:
            return peeked
        elif peeked_len > 0:
            return peeked[0]
        else:
            return None

    def shuffle(self):
        """Shuffles the deck."""
        random.shuffle(self.cards)

    @property
    def size(self):
        """
        Counts the number of cards currently in the deck.

        :returns: The number of cards in the deck.

        """
        return len(self)

#===============================================================================
# Card Class
#===============================================================================

class Card(object):
    """The Card class, representing a single card."""

    def __init__(self, value, suit):
        """
        Card constructor method.

        :param value: The card value.
        :type value: Str.
        :param suit: The card suit.
        :type suit: Str.

        """
        self.value = value
        self.suit = str(suit).capitalize()
        self.abbrev = self.gen_abbrev(value, suit)
        self.name = self.gen_name(value, suit)

    def __eq__(self, other):
        """
        Allows for Card value/suit equality comparisons.

        :param other: The other card to compare to.
        :type other: Card.

        :returns: Whether or not the cards are equal.

        """
        return (
            isinstance(other, Card) and self.value == other.value and
            self.suit == other.suit
        )

    def __gt__(self, other):
        """
        Allows for Card value comparisons. Uses poker ranks.

        :param other: The other card to compare to.
        :type other: Card.

        :returns: Whether or not self > other.

        """
        return POKER_RANKS[self.value] > POKER_RANKS[other.value]

    def __hash__(self):
        """
        The hash magic method.

        :returns: A unique number, or hash for the Card.

        """
        return hash((self.value, self.suit))

    def __repr__(self):
        """
        The repr magic method.

        :returns: A string representation of the Card object.

        """
        return "Card(value=%r, suit=%r)" % (self.value, self.suit)

    def __str__(self):
        """
        The str magic method.

        :returns: The card name.

        """
        return "%s" % (self.name)

    def gen_abbrev(self, value, suit):
        """
        Constructs an abbreviation for the card, using the given 
        value, and suit.

        :param value: The value to use.
        :type value: Str.
        :param suit: The suit to use.
        :type suit: Str.

        :returns: A newly constructed abbreviation, using the given value
            & suit

        """
        if value is "Joker":
            return "JK"
        elif value is "10":
            return "10%s" % (suit[0])
        else:
            return "%s%s" % (value[0], suit[0]) 

    def gen_name(self, value, suit):
        """
        Constructs a name for the card, using the given value, 
        and suit.

        :param value: The value to use.
        :type value: Str.
        :param suit: The suit to use.
        :type suit: Str.

        :returns: a newly constructed name, using the given value & suit.

        """
        if value is "Joker":
            return "Joker"
        else:
            return "%s of %s" % (str(value), suit)

#===============================================================================
# Other Functions
#===============================================================================

def check_term(card, term):
    """
    Checks a given search term against a given card's name attributes.

    :param card: The card to check.
    :type card: Card.
    :param term: The search term to check for. Can be a card full name, suit, 
        value, or abbreviation.
    :type terms: Str.

    :returns: True/False, depending on the check.

    """
    check_list = [
        x.lower() for x in 
        [
            card.name, card.suit, card.value, card.abbrev,
            card.abbrev[0], card.abbrev[1]
        ]
    ]

    term = term.lower()

    for check in check_list:
        if check == term:
            return True
    return False

#===============================================================================
# IF '__MAIN__'
#===============================================================================

if __name__ == '__main__':
    pass
