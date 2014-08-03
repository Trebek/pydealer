#===============================================================================
# PyDealer - Deck Class
#-------------------------------------------------------------------------------
# Version: 1.4.0
# Updated: 03-08-2014
# Author: Alex Crawford
# License: MIT
#===============================================================================

"""
This module contains the Deck class, used for creating Deck instances. Each
instance contains a full, 52 card French deck of playing cards. The Deck class
is basically just a kind of Stack, with a few extra methods, and is therefore a
subclass of Stack.

"""

#===============================================================================
# Imports
#===============================================================================

from collections import deque

from pydealer.const import (
    BOTTOM,
    TOP
)
from pydealer.stack import Stack
from pydealer.utils import (
    build_cards,
    compare_stacks,
)

# Dirty little try/except, to make PyDealer work with Python 3.
try:
    xrange
except:
    xrange = range


#===============================================================================
# Deck Class
#===============================================================================

class Deck(Stack):
    """
    The Deck class, representing the deck that the cards will be in. It is
    a sublcass of Stack, sharing all of the same methods, in addition to a
    couple of others you would expect a deck class to have.

    :arg cards:
        A list of cards to be the initial contents of the Deck. If provided,
        the deck will not automatically build a new deck. Can be a ``Stack``,
        ``Deck``, or ``list`` instance.
    :arg bool jokers:
        Whether or not to include jokers in the deck.
    :arg int num_jokers:
        How many jokers to add to the deck.
    :arg bool build:
        Whether or not to build the deck on instantiation.

    """
    def __init__(self, cards=None, jokers=False, num_jokers=2, build=True):
        """
        Deck constructor method.

        :arg cards:
            A list of cards to be the initial contents of the Deck. If
            provided, the deck will not automatically build a new deck.
            Can be a ``Stack``, ``Deck``, or ``list`` instance.
        :arg bool jokers:
            Whether or not to include jokers in the deck.
        :arg int num_jokers:
            How many jokers to add to the deck.
        :arg bool build:
            Whether or not to build the deck on instantiation.

        """
        if cards:
            self.cards = deque(cards)
        else:
            self.cards = deque([])

        self.decks_used = 0

        if build and not cards:
            self.build(jokers, num_jokers)

    def __add__(self, other):
        """
        Allows you to add (merge) decks together, with the ``+`` operand.

        :arg other:
            The other Deck to add to the Deck. Can be a ``Stack`` or ``Deck``
            instance.

        :returns:
            A new Deck instance, with the combined cards.

        """
        new_deck = Deck(list(self.cards) + list(other.cards))

        return new_deck

    def __eq__(self, other):
        """
        Allows for Deck comparisons.

        :arg Deck other:
            The other ``Deck`` instance to compare to.

        :returns:
            Whether or not the decks contain the same cards.

        """
        return (isinstance(other, Deck) and compare_stacks(self, other))

    def __repr__(self):
        """
        Returns a string representation of the ``Deck`` instance.

        :returns:
            A string representation of the Deck instance.

        """
        return "Deck(cards=%r)" % (self.cards)

    def build(self, jokers=False, num_jokers=2):
        """
        Builds a standard 52 card French deck of Card instances.

        :arg bool jokers:
            Whether or not to include jokers in the deck.
        :arg int num_jokers:
            The number of jokers to include.

        """
        self.decks_used += 1

        self.cards = deque(build_cards(jokers, num_jokers))

    def deal(self, num=1, rebuild=True, shuffle=True, end=0):
        """
        Returns a list of cards, which are removed from the deck.

        :arg int num:
            The number of cards to deal.
        :arg bool rebuild:
            Whether or not to rebuild the deck when cards run out.
        :arg bool shuffle:
            Whether or not to shuffle on rebuild.
        :arg int end:
            Which end to deal from. Can be ``0`` (top) or ``1`` (bottom).

        :returns:
            A given number of cards from the deck.

        """
        dealt_cards = [None] * num

        pop = {TOP: self.cards.pop, BOTTOM: self.cards.popleft}

        for n in xrange(num):
            if self.size == 0:
                if rebuild:
                    self.build()
                    if shuffle:
                        self.shuffle()
                else:
                    break

            card = pop[end]()
            dealt_cards[n] = card

        return dealt_cards


#===============================================================================
# Helper Functions
#===============================================================================

def convert(stack):
    """
    Convert a ``Stack`` to a ``Deck``.

    :arg Stack deck:
        The ``Stack`` instance to convert.

    """
    return Deck(list(stack.cards))