#===============================================================================
# PyDealer - Deck Class
#-------------------------------------------------------------------------------
# Version: 1.4.0
# Updated: 10-01-2015
# Author: Alex Crawford
# License: GPLv3
#===============================================================================

"""
This module contains the ``Deck`` class. Each ``Deck`` instance contains a full,
52 card French deck of playing cards upon instantiation. The ``Deck`` class is
a subclass of the ``Stack`` class, with a few extra/differing methods.

"""


#===============================================================================
# Imports
#===============================================================================

from collections import deque

from pydealer.const import (
    BOTTOM,
    DEFAULT_RANKS,
    TOP
)
from pydealer.stack import Stack
from pydealer.tools import build_cards

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

    .. warning::
        At the moment, adding Jokers may cause some (most) functions/methods
        to throw errors.

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
    :arg bool rebuild:
        Whether or not to rebuild the deck when it runs out of
        cards due to dealing.
    :arg bool re_shuffle:
        Whether or not to shuffle the deck after rebuilding.
    :arg dict ranks:
        The rank dict that will be referenced by the sorting
        methods etc. Defaults to ``DEFAULT_RANKS``

    """
    def __init__(self, **kwargs):
        """
        Deck constructor method.

        """
        self._cards = deque(kwargs.get("cards", []))

        self.jokers = kwargs.get("jokers", False)
        self.num_jokers = kwargs.get("num_jokers", 0)
        self.rebuild = kwargs.get("rebuild", False)
        self.re_shuffle = kwargs.get("re_shuffle", False)
        self.ranks = kwargs.get("ranks", DEFAULT_RANKS)
        self.decks_used = 0

        if kwargs.get("build", True):
            self.build()

    def __add__(self, other):
        """
        Allows you to add (merge) decks together, with the ``+`` operand.

        :arg other:
            The other Deck to add to the Deck. Can be a ``Stack`` or ``Deck``
            instance.

        :returns:
            A new Deck instance, with the combined cards.

        """
        try:
            new_deck = self.__class__(
                    cards=(list(self.cards) + list(other.cards)), build=False)
        except:
            new_deck = self.__class__(
                    cards=list(self.cards) + other, build=False)

        return new_deck

    def __repr__(self):
        """
        Returns a string representation of the ``Deck`` instance.

        :returns:
            A string representation of the Deck instance.

        """
        return "Deck(cards=%r)" % (self.cards)

    def build(self, jokers=False, num_jokers=0):
        """
        Builds a standard 52 card French deck of Card instances.

        :arg bool jokers:
            Whether or not to include jokers in the deck.
        :arg int num_jokers:
            The number of jokers to include.

        """
        jokers = jokers or self.jokers
        num_jokers = num_jokers or self.num_jokers

        self.decks_used += 1

        self.cards += build_cards(jokers, num_jokers)

    def deal(self, num=1, rebuild=False, shuffle=False, end=TOP):
        """
        Returns a list of cards, which are removed from the deck.

        :arg int num:
            The number of cards to deal.
        :arg bool rebuild:
            Whether or not to rebuild the deck when cards run out.
        :arg bool shuffle:
            Whether or not to shuffle on rebuild.
        :arg str end:
            The end of the ``Stack`` to add the cards to. Can be ``TOP`` ("top")
            or ``BOTTOM`` ("bottom").

        :returns:
            A given number of cards from the deck.

        """
        _num = num

        rebuild = rebuild or self.rebuild
        re_shuffle = shuffle or self.re_shuffle

        self_size = self.size

        if rebuild or num <= self_size:
            dealt_cards = [None] * num
        elif num > self_size:
            dealt_cards = [None] * self_size

        while num > 0:
            ends = {TOP: self.cards.pop, BOTTOM: self.cards.popleft}
            n = _num - num
            try:
                card = ends[end]()
                dealt_cards[n] = card
                num -= 1
            except:
                if self.size == 0:
                    if rebuild:
                        self.build()
                        if re_shuffle:
                            self.shuffle()
                    else:
                        break

        return Stack(cards=dealt_cards)


#===============================================================================
# Helper Functions
#===============================================================================

def convert_to_deck(stack):
    """
    Convert a ``Stack`` to a ``Deck``.

    :arg Stack stack:
        The ``Stack`` instance to convert.

    """
    return Deck(list(stack.cards))
