#===============================================================================
# PyDealer - Stack Class
#-------------------------------------------------------------------------------
# Version: 1.4.0
# Updated: 10-01-2015
# Author: Alex Crawford
# License: GPLv3
#===============================================================================

"""
This module contains the ``Stack`` class, which is the backbone of the PyDealer
package. A ``Stack`` is essentially just a generic "card container", with all of
the methods users may need to work with the cards they contain. A ``Stack`` can
be used as a hand, or a discard pile, etc.

"""


#===============================================================================
# Imports
#===============================================================================

from collections import deque
import random

from pydealer.const import (
    BOTTOM,
    DEFAULT_RANKS,
    TOP
)
from pydealer.tools import (
    check_sorted,
    check_term,
    find_card,
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
    :arg dict ranks:
        If ``sort=True``, The rank dict to reference for sorting.
        Defaults to ``DEFAULT_RANKS``.
    :arg bool sort:
        Whether or not to sort the stack upon instantiation.

    """
    def __init__(self, **kwargs):
        """
        Stack constructor method.

        :arg list cards:
            A list of cards to be the initial contents of the Stack.
        :arg dict ranks:
            If ``sort=True``, The rank dict to reference for sorting.
            Defaults to ``DEFAULT_RANKS``.
        :arg bool sort:
            Whether or not to sort the stack upon instantiation.

        """
        self._cards = deque(kwargs.get("cards", []))
        self.ranks = kwargs.get("ranks", DEFAULT_RANKS)

        self._i = 0

        if kwargs.get("sort"):
            self.sort(self.ranks)

    def __add__(self, other):
        """
        Allows users to add (merge) Stack/Deck instances together, with the
        ``+`` operand. You can also add a list of ``Card`` instances to a
        Stack/Deck instance.

        :arg other:
            The other ``Stack``, or ``Deck`` instance, or list of ``Card``
            instances to add to the ``Stack``/``Deck`` instance.

        :returns:
            A new ``Stack`` instance, with the combined cards.

        """
        try:
            new_stack = Stack(cards=(list(self.cards) + list(other.cards)))
        except:
            new_stack = Stack(cards=(list(self.cards) + other))

        return new_stack

    def __contains__(self, card):
        """
        Allows for Card instance (not value & suit) inclusion checks.

        :arg Card card:
            The Card instance to check for.

        :returns:
            Whether or not the Card instance is in the Deck.

        """
        return id(card) in [id(x) for x in self.cards]

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
        contains the same cards, in the same order (based on value & suit,
        not instance).

        :arg other:
            The other ``Stack``/``Deck`` instance or ``list`` to compare to.

        :returns:
            ``True`` or ``False``.

        """
        if len(self.cards) == len(other):
            for i, card in enumerate(self.cards):
                if card != other[i]:
                    return False
            return True
        else:
            return False

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

    def __len__(self):
        """
        Allows check the Stack length, with len.

        :returns:
            The length of the stack (self.cards).

        """
        return len(self.cards)

    def __ne__(self, other):
        """
        Allows for Stack comparisons. Checks to see if the given ``other``
        does not contain the same cards, in the same order (based on value &
        suit, not instance).

        :arg other:
            The other ``Stack``/``Deck`` instance or ``list`` to compare to.

        :returns:
            ``True`` or ``False``.

        """
        if len(self.cards) == len(other):
            for i, card in enumerate(self.cards):
                if card != other[i]:
                    return True
            return False
        else:
            return True

    def __repr__(self):
        """
        The repr magic method.

        :returns:
            A representation of the ``Deck`` instance.

        """
        return "Stack(cards=%r)" % (self.cards)

    def __setitem__(self, indice, value):
        """
        Assign cards to specific stack indices, like a list.

        Example:
            stack[16] = card_object

        :arg int indice:
            The indice to set.
        :arg Card value:
            The Card to set the indice to.

        """
        self.cards[indice] = value

    def __str__(self):
        """
        Allows users to print a human readable representation of the ``Stack``
        instance, using ``print``.

        :returns:
            A str of the names of the cards in the stack.

        """
        card_names = "".join([x.name + "\n" for x in self.cards]).rstrip("\n")
        return "%s" % (card_names)

    def add(self, cards, end=TOP):
        """
        Adds the given list of ``Card`` instances to the top of the stack.

        :arg cards:
            The cards to add to the ``Stack``. Can be a single ``Card``
            instance, or a ``list`` of cards.
        :arg str end:
            The end of the ``Stack`` to add the cards to. Can be ``TOP`` ("top")
            or ``BOTTOM`` ("bottom").

        """
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

    @property
    def cards(self):
        """
        The cards property.

        :returns:
            The cards in the Stack/Deck.

        """
        return self._cards

    @cards.setter
    def cards(self, items):
        """
        The cards property setter. This makes sure that if ``Stack.cards`` is
        set directly, that the items are in a deque.

        :arg items:
            The list of Card instances, or a Stack/Deck instance to assign to
            the Stack/Deck.

        """
        self._cards = deque(items)

    def deal(self, num=1, end=TOP):
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

            return Stack(cards=dealt_cards)
        else:
            return Stack()

    def empty(self, return_cards=False):
        """
        Empties the stack, removing all cards from it, and returns them.

        :arg bool return_cards:
            Whether or not to return the cards.

        :returns:
            If ``return_cards=True``, a list containing the cards removed
            from the Stack.

        """
        cards = list(self.cards)
        self.cards = []

        if return_cards:
            return cards

    def find(self, term, limit=0, sort=False, ranks=None):
        """
        Searches the stack for cards with a value, suit, name, or
        abbreviation matching the given argument, 'term'.

        :arg str term:
            The search term. Can be a card full name, value, suit,
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
        ranks = ranks or self.ranks
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
        Searches the stack for cards with a value, suit, name, or
        abbreviation matching the given argument, 'terms'.

        :arg list terms:
            The search terms. Can be card full names, suits, values,
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
        ranks = ranks or self.ranks
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

    def get(self, term, limit=0, sort=False, ranks=None):
        """
        Get the specified card from the stack.

        :arg term:
            The search term. Can be a card full name, value, suit,
            abbreviation, or stack indice.
        :arg int limit:
            The number of items to retrieve for each term.
        :arg bool sort:
            Whether or not to sort the results, by poker ranks.
        :arg dict ranks:
            The rank dict to reference for sorting. If ``None``, it will
            default to ``DEFAULT_RANKS``.

        :returns:
            A list of the specified cards, if found.

        """
        ranks = ranks or self.ranks
        got_cards = []

        try:
            indices = self.find(term, limit=limit)
            got_cards = [self.cards[i] for i in indices]
            self.cards = [v for i, v in enumerate(self.cards) if
                i not in indices]
        except:
            got_cards = [self.cards[term]]
            self.cards = [v for i, v in enumerate(self.cards) if i is not term]

        if sort:
            got_cards = sort_cards(got_cards, ranks)

        return got_cards

    def get_list(self, terms, limit=0, sort=False, ranks=None):
        """
        Get the specified cards from the stack.

        :arg term:
            The search term. Can be a card full name, value, suit,
            abbreviation, or stack indice.
        :arg int limit:
            The number of items to retrieve for each term.
        :arg bool sort:
            Whether or not to sort the results, by poker ranks.
        :arg dict ranks:
            The rank dict to reference for sorting. If ``None``, it will
            default to ``DEFAULT_RANKS``.

        :returns:
            A list of the specified cards, if found.

        """
        ranks = ranks or self.ranks
        got_cards = []

        try:
            indices = self.find_list(terms, limit=limit)
            got_cards = [self.cards[i] for i in indices if self.cards[i]
                not in got_cards]
            self.cards = [v for i, v in enumerate(self.cards) if
                i not in indices]
        except:
            indices = []
            for item in terms:
                try:
                    card = self.cards[item]
                    if card not in got_cards:
                        got_cards.append(card)
                        indices.append(item)
                except:
                    indices += self.find(item, limit=limit)
                    got_cards += [self.cards[i] for i in indices if
                        self.cards[i] not in got_cards]
            self.cards = [v for i, v in enumerate(self.cards) if
                i not in indices]

        if sort:
            got_cards = sort_cards(got_cards, ranks)

        return got_cards

    def insert(self, card, indice=-1):
        """
        Insert a given card into the stack at a given indice.

        :arg Card card:
            The card to insert into the stack.
        :arg int indice:
            Where to insert the given card.

        """
        self_size = len(self.cards)

        if indice in [0, -1]:
            if indice == -1:
                self.cards.append(card)
            else:
                self.cards.appendleft(card)
        elif indice != self_size:
            half_x, half_y = self.split(indice)
            self.cards = list(half_x.cards) + [card] + list(half_y.cards)


    def insert_list(self, cards, indice=-1):
        """
        Insert a list of given cards into the stack at a given indice.

        :arg list cards:
            The list of cards to insert into the stack.
        :arg int indice:
            Where to insert the given cards.

        """
        self_size = len(self.cards)

        if indice in [0, -1]:
            if indice == -1:
                self.cards += cards
            else:
                self.cards.extendleft(cards)
        elif indice != self_size:
            half_x, half_y = self.split(indice)
            self.cards = list(half_x.cards) + list(cards) + list(half_y.cards)


    def is_sorted(self, ranks=None):
        """
        Checks whether the stack is sorted.

        :arg dict ranks:
            The rank dict to reference for checking. If ``None``, it will
            default to ``DEFAULT_RANKS``.

        :returns:
            Whether or not the cards are sorted.

        """
        ranks = ranks or self.ranks

        return check_sorted(self, ranks)

    def open_cards(self, filename=None):
        """
        Open cards from a txt file.

        :arg str filename:
            The filename of the deck file to open. If no filename given,
            defaults to "cards-YYYYMMDD.txt", where "YYYYMMDD" is the year,
            month, and day. For example, "cards-20140711.txt".

        """
        self.cards = open_cards(filename)

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

        self.cards = self[::-1]

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
        self.cards = cards

    def shuffle(self, times=1):
        """
        Shuffles the Stack.

        .. note::
            Shuffling large numbers of cards (100,000+) may take a while.

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
            The rank dict to reference for sorting. If ``None``, it will
            default to ``DEFAULT_RANKS``.

        :returns:
            The sorted cards.

        """
        ranks = ranks or self.ranks
        self.cards = sort_cards(self.cards, ranks)

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
                mid = self_size // 2
                return Stack(cards=self[0:mid]), Stack(cards=self[mid::])
            else:
                return Stack(cards=self[0:indice]), Stack(cards=self[indice::])
        else:
            return Stack(cards=self.cards), Stack()


#===============================================================================
# Helper Functions
#===============================================================================

def convert_to_stack(deck):
    """
    Convert a ``Deck`` to a ``Stack``.

    :arg Deck deck:
        The ``Deck`` to convert.

    :returns:
        A new ``Stack`` instance, containing the cards from the given ``Deck``
        instance.

    """
    return Stack(list(deck.cards))