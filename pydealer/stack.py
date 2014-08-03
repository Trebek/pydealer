#===============================================================================
# PyDealer - Stack Class
#-------------------------------------------------------------------------------
# Version: 1.4.0
# Updated: 03-08-2014
# Author: Alex Crawford
# License: MIT
#===============================================================================

"""
This module contains the Stack class, used for creating Stack instances,
which are essentially just generic 'card containers', with all of the methods
you may need to work with the cards they contain. Could be used to represent
a hand, or a discard pile, etc.

"""

#===============================================================================
# Imports
#===============================================================================

from collections import deque
import random

from pydealer.const import (
    BOTTOM,
    TOP
)
from pydealer.utils import (
    check_term,
    compare_stacks,
    open_cards,
    random_card,
    save_cards,
    sort_cards
)

# Dirty little try/except, to make PyDealer work with Python 3.
try:
    xrange
except:
    xrange = range


#===============================================================================
# Stack Class
#===============================================================================

class Stack(object):
    """
    The Stack class, representing a collection of cards. This is the main
    'card container' class, with methods for manipulating it's contents.

    :arg list cards:
        A list of cards to be the initial contents of the Stack.
    :arg bool sort:
        Whether or not to sort the stack, by poker ranks.

    """
    def __init__(self, cards=None, sort=False):
        """
        Stack constructor method.

        :arg list cards:
            A list of cards to be the initial contents of the Stack.
        :arg bool sort:
            Whether or not to sort the stack, by poker ranks.

        """
        if cards:
            self.cards = deque(cards)
        else:
            self.cards = deque([])

        if sort:
            self.sort()

    def __add__(self, other):
        """
        Allows you to add (merge) Hands together, with the ``+`` operand.

        :arg other:
            The other ``Stack`` or ``Deck`` to add to the ``Stack``.

        :returns:
            A new ``Stack`` instance, with the combined cards.

        """
        new_stack = Stack(list(self.cards) + list(other.cards))
        return new_stack

    def __contains__(self, card):
        """
        Allows for Card instance (not face & suit) inclusion checks.

        :arg Card card:
            The Card instance to check for.

        :returns:
            Whether or not the Card instance is in the Deck.

        """
        id_list = [id(x) for x in self.cards]
        return id(card) in id_list

    def __delitem__(self, indice):
        """
        Allows for deletion of a Card instance, using del.

        :arg int indice:
            The indice to delete.

        """
        del self.cards[indice]

    def __eq__(self, other):
        """
        Allows for Stack comparisons. Checks to see if the given ``other``
        contains the same cards (based on face & suit, not instance).

        :arg Stack other:
            The other ``Stack`` to compare to.

        :returns:
            ``True`` or ``False``.

        """
        return (isinstance(other, Stack) and compare_stacks(self, other))

    def __getitem__(self, key):
        """
        Allows for accessing, and slicing of cards, using ``Deck[indice]``,
        ``Deck[start:stop]``, etc.

        :arg int indice:
            The indice to get.

        :returns:
            The ``Card`` at the given indice.

        """
        self_len = len(self)
        if isinstance(key, slice):
            return [self[i] for i in xrange(*key.indices(self_len))]
        elif isinstance(key, int):
            if key < 0 :
                key += self_len
            if key >= self_len:
                raise IndexError("The index ({}) is out of range.".format(key))
            return self.cards[key]
        else:
            raise TypeError("Invalid argument type.")

    def __iter__(self):
        """
        Allows looping through the Stack, using for loops.

        :returns:
            An iterator of the cards in the stack.

        """
        for card in self.cards:
            yield card

    def __len__(self):
        """
        Allows check the Stack length, with len.

        :returns:
            The length of the stack (self.cards).

        """
        return len(self.cards)

    def __repr__(self):
        """
        The repr magic method.

        :returns:
            A string representation of the Heck instance.

        """
        return "Stack(cards=%r)" % (self.cards)

    def __setitem__(self, indice, value):
        """
        Allows you to assign cards to specific stack indices.

        :arg int indice:
            The indice to set.
        :arg Card value:
            The Card to set the indice to.

        """
        self.cards[indice] = value

    def __str__(self):
        """
        Allows you to print a human readable representation of the ``Stack``
        instance, using ``print``.

        :returns:
            A str of the names of the cards in the stack.

        """
        card_names = "".join([x.name + "\n" for x in self.cards]).rstrip("\n")
        return "%s" % (card_names)

    def add(self, cards, end=None):
        """
        Adds the given list of ``Card`` instances to the top of the stack.

        :arg cards:
            The cards to add to the ``Stack``. Can be a single ``Card``
            instance, or a ``list`` of cards.
        :arg int end:
            The end of the ``Stack`` to add the cards to. Can be ``0`` (top)
            or ``1`` (bottom).

        """
        end = end or TOP
        if end is TOP:
            try:
                self.cards += cards
            except:
                self.cards += [cards]
        elif end is BOTTOM:
            try:
                self.cards.extendleft(cards)
            except:
                self.cards.extendleft([cards])

    def deal(self, num=1, end=0):
        """
        Returns a list of cards, which are removed from the Stack.

        :arg int num:
            The number of cards to deal.
        :arg str end:
            Which end to deal from. Can be ``0`` (top) or ``1`` (bottom).

        :returns:
            The given number of cards from the stack.

        """
        ends = {TOP: self.cards.pop, BOTTOM: self.cards.popleft}

        self_size = self.size

        if num <= self_size:
            dealt_cards = [None] * num
        else:
            num = self_size
            dealt_cards = [None] * self_size

        if self_size:
            for n in xrange(num):
                try:
                    card = ends[end]()
                    dealt_cards[n] = card
                except:
                    break

            return dealt_cards
        else:
            return []

    def empty(self):
        """
        Empties the stack, removing all cards from it, and returns them.

        :returns:
            A list of all of the cards in the stack.

        """

        cards = list(self.cards)
        self.cards = deque([])

        return cards

    def find(self, term, limit=0, sort=False, ranks=None):
        """
        Searches the stack for cards with a face, suit, name, or
        abbreviation matching the given argument, 'term'.

        :arg str term:
            The search term. Can be a card full name, face, suit,
            or abbreviation.
        :arg int limit:
            The number of items to retrieve for each term. ``0`` equals
            no limit.
        :arg bool sort:
            Whether or not to sort the results.
        :arg dict ranks:
            The rank dict to reference for sorting. If ``None``, it will
            default to ``DEFAULT_RANKS``.

        :returns:
            A list of stack indices for the cards matching the given terms,
            if found.

        """
        found_indices = []
        count = 0

        if not limit:
            for i, card in enumerate(self.cards):
                if check_term(card, term):
                    found_indices.append(i)
        else:
            for i, card in enumerate(self.cards):
                if count < limit:
                    if check_term(card, term):
                        found_indices.append(i)
                        count += 1
                else:
                    break

        if sort:
            found_indices = sort_card_indices(self, found_indices, ranks)

        return found_indices

    def find_list(self, terms, limit=0, sort=False, ranks=None):
        """
        Searches the stack for cards with a face, suit, name, or
        abbreviation matching the given argument, 'terms'.

        :arg list terms:
            The search terms. Can be card full names, suits, faces,
            or abbreviations.
        :arg int limit:
            The number of items to retrieve for each term.
        :arg bool sort:
            Whether or not to sort the results, by poker ranks.
        :arg dict ranks:
            The rank dict to reference for sorting. If ``None``, it will
            default to ``DEFAULT_RANKS``.

        :returns:
            A list of stack indices for the cards matching the given terms,
            if found.

        """
        found_indices = []
        count = 0

        if not limit:
            for term in terms:
                for i, card in enumerate(self.cards):
                    if check_term(card, term) and i not in found_indices:
                        found_indices.append(i)
        else:
            for term in terms:
                for i, card in enumerate(self.cards):
                    if count < limit:
                        if check_term(card, term) and i not in found_indices:
                            found_indices.append(i)
                            count += 1
                    else:
                        break
                count = 0

        if sort:
            found_indices = sort_card_indices(self, found_indices, ranks)

        return found_indices

    def get(self, term, limit=0, sort=False):
        """
        Get the specified card from the stack.

        :arg term:
            The search term. Can be a card full name, face, suit,
            abbreviation, or stack indice.
        :arg int limit:
            The number of items to retrieve for each term.
        :arg bool sort:
            Whether or not to sort the results, by poker ranks.

        :returns:
            A list of the specified cards, if found.

        """
        got_cards = []

        try:
            indices = self.find(term, limit=limit)
            got_cards = [self.cards[i] for i in indices]
            self.cards = deque(
                [v for i, v in enumerate(self.cards) if
                i not in indices]
            )
        except:
            got_cards = [self.cards[term]]
            self.cards = deque(
                [v for i, v in enumerate(self.cards) if i is not term]
            )

        if sort:
            got_cards = sort_cards(got_cards)

        return got_cards

    def get_list(self, terms, limit=0, sort=False):
        """
        Get the specified cards from the stack.

        :arg term:
            The search term. Can be a card full name, face, suit,
            abbreviation, or stack indice.
        :arg int limit:
            The number of items to retrieve for each term.
        :arg bool sort:
            Whether or not to sort the results, by poker ranks.

        :returns:
            A list of the specified cards, if found.

        """
        got_cards = []

        try:
            indices = self.find_list(terms, limit=limit)
            got_cards = [self.cards[i] for i in indices if self.cards[i]
                not in got_cards]
            self.cards = deque(
                [v for i, v in enumerate(self.cards) if
                i not in indices]
            )
        except:
            for item in terms:
                got_cards.append(self.cards[item])
            self.cards = deque(
                [v for i, v in enumerate(self.cards) if i not in terms]
            )

        if sort:
            got_cards = sort_cards(got_cards)

        return got_cards

    def open_cards(self, filename=None):
        """
        Open cards from a txt file.

        :arg str filename:
            The filename of the deck file to open. If no filename given,
            defaults to "cards-YYYYMMDD.txt", where "YYYYMMDD" is the year,
            month, and day. For example, "cards-20140711.txt".

        """
        self.cards = deque(open_cards(filename))

    def random_card(self, remove=False):
        """
        Returns a random card from the Stack. If ``remove=True``, it will
        also remove the card from the deck.

        :arg bool remove:
            Whether or not to remove the card from the deck.

        :returns:
            A random Card object, from the Stack.

        """
        return random_card(self, remove)

    def reverse(self):
        """Reverse the order of the Stack in place."""

        self.cards = deque(self[::-1])

    def save_cards(self, filename=None):
        """
        Save the current stack contents, in plain text, to a txt file.

        :arg str filename:
            The filename to use for the file. If no filename given, defaults
            to "cards-YYYYMMDD.txt", where "YYYYMMDD" is the year, month, and
            day. For example, "cards-20140711.txt".

        """
        save_cards(self, filename)

    def set_cards(self, cards):
        """
        Change the Deck's current contents to the given cards.

        :arg list cards:
            The Cards to assign to the stack.

        """
        self.cards = deque(cards)

    def shuffle(self, times=1):
        """
        Shuffles the Stack.

        .. note::
            Shuffling multiple times can actually lead to less random ordering.

            Also, shuffling large numbers of cards (100,000+) may take a
            a while.

        :arg int times:
            The number of times to shuffle.

        """
        for _ in xrange(times):
            random.shuffle(self.cards)

    @property
    def size(self):
        """
        Counts the number of cards currently in the stack.

        :returns:
            The number of cards in the stack.

        """
        return len(self.cards)

    def sort(self, ranks=None):
        """
        Sorts the stack, either by poker ranks, or big two ranks.

        :arg dict ranks:
            The ranks to reference for sorting order.

        :returns:
            The sorted cards.

        """
        self.cards = deque(sort_cards(self.cards, ranks))

    def split(self, indice=None):
        """
        Splits the Stack, either in half, or at the given indice, into two
        separate Stacks.

        :arg int indice:
            Optional. The indice to split the Stack at. Defaults to the middle
            of the ``Stack``.

        :returns:
            The two parts of the Stack, as separate Stack instances.

        """
        self_size = self.size
        if self_size > 1:
            if not indice:
                mid = self_size / 2
                return Stack(self[0:mid]), Stack(self[mid::])
            else:
                return Stack(self[0:indice]), Stack(self[indice::])
        else:
            return Stack(self), Stack()


#===============================================================================
# Helper Functions
#===============================================================================

def convert(deck):
    """
    Convert a ``Deck`` to a ``Stack``.

    :arg Deck deck:
        The ``Deck`` to convert.

    :returns:
        A new ``Stack`` instance, containing the cards from the given ``Deck``
        instance.

    """
    return Stack(list(deck.cards))