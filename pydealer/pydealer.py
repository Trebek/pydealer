#===============================================================================
# PyDealer: Playing Card Package
#-------------------------------------------------------------------------------
# Version: 1.3.0
# Updated: 03-07-2014
# Author: Alex Crawford
# License: MIT
#===============================================================================

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

"""
A simple package with classes for constructing ``Deck`` instances, of 52 common
playing cards. Each card is a separate ``Card`` instance, with a name, value,
suit, and abbreviation.

"""
#===============================================================================
# Imports
#===============================================================================

from collections import deque
import random

try:
    xrange
except:
    xrange = range

#===============================================================================
# Card Data
#===============================================================================

SUITS = ["Diamonds", "Clubs", "Hearts", "Spades"]
FACES = ["Jack", "Queen", "King"]
NUMBERS = ["2", "3", "4", "5", "6", "7", "8", "9", "10"]

#===============================================================================
# Helper Dicts
#===============================================================================

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

    def __init__(self, cards=[], jokers=False, num_jokers=2, build=True,
            sort=False):
        """
        Deck constructor method.

        :param jokers:
            Whether or not to include jokers in the deck.
        :type jokers:
            Bool.
        :param num_jokers:
            How many jokers to add to the deck.
        :type num_jokers:
            Int.
        :param build:
            Whether or not to build the deck on instantiation.
        :type build:
            Bool.
        :param sort:
            Whether or not to sort the deck, by poker ranks.
        :type sort:
            Bool.

        """
        self.cards = deque(cards)
        self.decks_used = 0

        if build:
            self.build(jokers, num_jokers, sort)

    def __add__(self, other):
        """
        Allows you to add (merge) decks together, with the ``+`` operand.

        :param other:
            The other Deck to add to the Deck.
        :type other:
            Deck.

        :returns:
            A new Deck instance, with the combined cards.

        """
        new_deck = Deck(build=False)
        new_deck.cards = self.cards + other.cards
        return new_deck

    def __contains__(self, card):
        """
        Allows for Card instance (not suit & value) inclusion checks.

        :param card:
            The Card instance to check for.
        :type card:
            Card.

        :returns:
            Whether or not the Card instance is in the Deck.

        """
        id_list = [id(x) for x in self.cards]
        return id(card) in id_list

    def __delitem__(self, indice):
        """
        Allows for deletion of a Card instance, using del.

        :param indice:
            The indice to delete.
        :type indice:
            Int.

        """
        del self.cards[indice]

    def __eq__(self, other):
        """
        Allows for Deck ordering comparisons.

        :param other:
            The other Deck to compare to.
        :type other:
            Deck.

        :returns:
            Whether or not the decks are in the same order.

        """
        return (isinstance(other, Deck) and compare_decks(self, other))

    def __getitem__(self, indice):
        """
        Allows for getting of cards, using ``Deck[indice]``.

        :param indice:
            The indice to get.
        :type indice:
            Int.

        :returns:
            The Card at the given indice.

        """
        return self.cards[indice]

    def __iter__(self):
        """
        Allows looping through the Deck, using for loops.

        :returns:
            An iterator of the Cards in the deck.

        """
        for card in self.cards:
            yield card

    def __len__(self):
        """
        Allows check the deck length, with len.

        :returns:
            The length of the deck (self.cards).

        """
        return len(self.cards)

    def __repr__(self):
        """
        The repr magic method.

        :returns:
            A string representation of the Deck instance.

        """
        return "Deck(cards=%r)" % (self.cards)

    def __setitem__(self, indice, value):
        """
        Allows you to assign cards to specific deck indices.

        :param indice:
            The indice to set.
        :type indice:
            Int.
        :param value:
            The Card to set the indice to.
        :type value:
            Card.

        :returns:
            The Card at the given indice.

        """
        self.cards[indice] = value

    def __str__(self):
        """
        The str magic method.

        :returns:
            A str of the names of the cards in the deck.

        """
        card_names = "".join([x.name + "\n" for x in self.cards]).rstrip("\n")
        return "%s" % (card_names)

    def build(self, jokers=False, num_jokers=2, sort=False):
        """
        Builds a standard 52 card French deck of Card instances.

        :param jokers:
            Whether or not to include jokers in the deck.
        :type jokers:
            Bool.
        :param num_jokers:
            The number of jokers to include.
        :type num_jokers:
            Int.
        :param sort:
            Whether or not to sort the deck by poker ranks.
        :type sort:
            Bool.

        :returns:
            A new Deck instance.

        """
        self.decks_used += 1

        temp_deck = [
            Card(number, suit) for number in NUMBERS for suit in SUITS
        ]
        temp_deck.extend(
            [Card(face, suit) for face in FACES for suit in SUITS]
        )
        temp_deck.extend([Card("Ace", suit) for suit in SUITS])

        if jokers:
            temp_deck.extend([Card("Joker", None) for i in xrange(num_jokers)])

        if sort:
            self.cards = sorted(
                temp_deck,
                key=lambda x: POKER_RANKS[x.value]
            )
        else:
            self.cards = temp_deck

    def deal(self, num=1, rebuild=True):
        """
        Returns a list of cards, which are removed from the deck.

        :param num:
            The number of cards to deal.
        :type num:
            Int.
        :param rebuild:
            Whether or not to rebuild the deck when cards run out.
        :type rebuild:
            Bool.

        :returns:
            A given number of cards from the deck.

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

    def find(self, term, sort=False):
        """
        Searches the deck for cards with a suit, value, name, or
        abbreviation matching the given argument, 'terms'.

        :param term:
            The search term. Can be a card full name, suit, value,
            or abbreviation.
        :type term:
            Str.
        :param sort:
            Whether or not to sort the results, by poker ranks.
        :type sort:
            Bool.

        :returns:
            A list of deck indices for the cards matching the given terms,
            if found.

        """
        found_indices = []

        for i, card in enumerate(self.cards):
            if check_term(card, term):
                found_indices.append(i)

        if sort:
            found_indices = sort_card_indices(found_indices, self)

        return found_indices

    def find_list(self, terms, sort=False):
        """
        Searches the deck for cards with a suit, value, name, or
        abbreviation matching the given argument, 'terms'.

        :param terms:
            The search terms. Can be card full names, suits, values,
            or abbreviations.
        :type terms:
            List of str.
        :param sort:
            Whether or not to sort the results, by poker ranks.
        :type sort:
            Bool.

        :returns:
            A list of deck indices for the cards matching the given terms,
            if found.

        """
        found_indices = []

        for term in terms:
            for i, card in enumerate(self.cards):
                if check_term(card, term):
                    if i not in found_indices:
                        found_indices.append(i)

        if sort:
            found_indices = sort_card_indices(found_indices, self)

        return found_indices

    def get(self, term, sort=False):
        """
        Get the specified card from the deck.

        :param term:
            The search term. Can be a card full name, suit, value,
            abbreviation, or deck indice.
        :type term:
            Str|int.
        :param sort:
            Whether or not to sort the results, by poker ranks.
        :type sort:
            Bool.

        :returns:
            A list of the specified cards, if found.

        """
        got_cards = []

        try:
            indices = self.find(term)
            got_cards = [self.cards[i] for i in indices]
        except:
            got_cards = [self.cards[term]]

        for card in got_cards:
            self.cards.remove(card)

        if sort:
            got_cards = sort_cards(got_cards)

        return got_cards

    def get_list(self, terms, sort=False):
        """
        Get the specified cards from the deck.

        :param term:
            The search term. Can be a card full name, suit, value,
            abbreviation, or deck indice.
        :type term:
            List of str|int.
        :param sort:
            Whether or not to sort the results, by poker ranks.
        :type sort:
            Bool.

        :returns:
            A list of the specified cards, if found.

        """
        got_cards = []

        for item in terms:
            try:
                indices = self.find(item)
                got_cards.extend(
                    [
                        self.cards[i] for i in indices if
                        self.cards[i] not in got_cards
                    ]
                )
            except:
                got_cards.append(self.cards[item])

        for card in got_cards:
            self.cards.remove(card)

        if sort:
            got_cards = sort_cards(got_cards)

        return got_cards

    def set_cards(self, cards):
        """
        Change the Deck's current contents to the given cards.

        :param cards:
            The Cards to assign to the deck.
        :type cards:
            List of Cards.

        """
        self.cards = deque(cards)

    def shuffle(self, times=1):
        """
        Shuffles the deck.

        :param time:
            The number of times to shuffle.
        :param time:
            Int.

        """
        for _ in xrange(times):
            random.shuffle(self.cards)

    @property
    def size(self):
        """
        Counts the number of cards currently in the deck.

        :returns:
            The number of cards in the deck.

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

        :param value:
            The card value.
        :type value:
            Str.
        :param suit:
            The card suit.
        :type suit:
            Str.

        """
        self.value = value
        self.suit = str(suit).capitalize()
        self.abbrev = self.gen_abbrev(value, suit)
        self.name = self.gen_name(value, suit)

    def __eq__(self, other):
        """
        Allows for Card value/suit equality comparisons.

        :param other:
            The other card to compare to.
        :type other:
            Card.

        :returns:
            Whether or not the cards are equal.

        """
        return (
            isinstance(other, Card) and self.value == other.value and
            self.suit == other.suit
        )

    def __gt__(self, other):
        """
        Allows for Card value comparisons. Uses poker ranks.

        :param other:
            The other card to compare to.
        :type other:
            Card.

        :returns:
            Whether or not self > other.

        """
        return POKER_RANKS[self.value] > POKER_RANKS[other.value]

    def __hash__(self):
        """
        The hash magic method.

        :returns:
            A unique number, or hash for the Card.

        """
        return hash((self.value, self.suit))

    def __repr__(self):
        """
        The repr magic method.

        :returns:
            A string representation of the Card instance.

        """
        return "Card(value=%r, suit=%r)" % (self.value, self.suit)

    def __str__(self):
        """
        The str magic method.

        :returns:
            The card name.

        """
        return "%s" % (self.name)

    def gen_abbrev(self, value, suit):
        """
        Constructs an abbreviation for the card, using the given
        value, and suit.

        :param value:
            The value to use.
        :type value:
            Str.
        :param suit:
            The suit to use.
        :type suit:
            Str.

        :returns:
            A newly constructed abbreviation, using the given value
            & suit

        """
        if value is "Joker":
            return "JKR"
        elif value is "10":
            return "10%s" % (suit[0])
        else:
            return "%s%s" % (value[0], suit[0])

    def gen_name(self, value, suit):
        """
        Constructs a name for the card, using the given value,
        and suit.

        :param value:
            The value to use.
        :type value:
            Str.
        :param suit:
            The suit to use.
        :type suit:
            Str.

        :returns:
            a newly constructed name, using the given value & suit.

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

    :param card:
        The card to check.
    :type card:
        Card.
    :param term:
        The search term to check for. Can be a card full name, suit,
        value, or abbreviation.
    :type terms:
        Str.

    :returns:
        True/False, depending on the check.

    """
    check_list = [
        x.lower() for x in
        [
            card.name, card.suit, card.value, card.abbrev,
            card.suit[0], card.value[0]
        ]
    ]

    term = term.lower()

    for check in check_list:
        if check == term:
            return True

    return False


def compare_decks(deck_x, deck_y):
    """
    Checks whether two given Decks contain the same cards.

    :param deck_x:
        The first deck to check.
    :type deck_x:
        Deck.
    :param deck_y:
        The second deck to check.
    :type deck_y:
        Deck.

    :returns:
        True/False, depending on the result.

    """
    _deck_x = sort_cards(deck_x, method=BIG2_RANKS)
    _deck_y = sort_cards(deck_y, method=BIG2_RANKS)

    if _deck_x == _deck_y:
        return True

    return False


def sort_card_indices(indices, deck, method=POKER_RANKS):
    """
    Sorts the given Deck indices by poker ranks. Must also supply the Deck
    instance that the indices are from.

    :param indices:
        The indices to sort.
    :type indices:
        List of int.
    :param deck:
        The deck the indices are from.
    :type deck:
        Deck.

    :returns:
        The sorted indices.

    """
    if method is POKER_RANKS:
        indices = sorted(
            indices,
            key=lambda x: POKER_RANKS[deck[x].value]
        )
    elif method is BIG2_RANKS:
        indices = sorted(
            indices,
            key=lambda x: BIG2_RANKS["suits"][deck[x].suit]
        )
        indices = sorted(
            indices,
            key=lambda x: BIG2_RANKS["values"][deck[x].value]
        )

    return indices


def sort_cards(cards, method=POKER_RANKS):
    """
    Sorts the given cards, by poker ranks.

    :param cards:
        The cards to sort.
    :type cards:
        List of Cards.

    :returns:
        The sorted cards.

    """
    if method is POKER_RANKS:
        cards = sorted(
            cards,
            key=lambda x: POKER_RANKS[x.value]
        )
    elif method is BIG2_RANKS:
        cards = sorted(
            cards,
            key=lambda x: BIG2_RANKS["suits"][x.suit]
        )
        cards = sorted(
            cards,
            key=lambda x: BIG2_RANKS["values"][x.value]
        )

    return cards

#===============================================================================
# IF '__MAIN__'
#===============================================================================

if __name__ == "__main__":
    pass
