.. include:: globals.inc


###############
Getting Started
###############

This is an overview of all of the methods/functions that users will likely use most.

.. contents::
    :depth: 3


Install/Uninstall with `pip`_
=============================

I recommend downloading and installing `pip`_, if you haven't already, and using that to install PyDealer, from the `Python Package Index`_.

Enter one of the following commands into your \*nix Bash console, Windows Command Prompt, etc. (after installing pip_).

Install
-------
.. code-block:: bash

    $ pip install pydealer

Update
------
.. code-block:: bash

    $ pip install pydealer -U

Uninstall
---------
.. code-block:: bash

    $ pip uninstall pydealer

----------------


Import PyDealer
===============

I'm sure most of you know how this is done already, but for those that don't, here is how you import pydealer.

.. code-block:: python

    # Import PyDealer
    import pydealer

    # I, personally, prefer to import PyDealer with a shorter name:
    # import pydealer as pd

    # I also like to alias the utility functions:
    # import pydealer.utils as utils

Import Specific Classes/Functions
---------------------------------

You can, of course also just import the specific classes/functions that you need.

.. code-block:: python

    # Import the base classes:
    from pydealer import (
        Card,
        Deck,
        Stack
    )

    # Import specific utility functions:
    from pydealer.utils import (
        build_cards,
        compare_stacks,
        check_sorted
        # And/or any other functions you wish to import
    )

----------------


Stack/Deck Manipulation
=======================

Construct a Deck
----------------

Constructing a new, full deck of cards is about as simple as it gets, but let's just get it out of the way, so I don't have to explain it in every subsequent example.

.. code-block:: python

    import pydealer

    # Construct a Deck instance, with 52 cards.
    deck = pydealer.Deck()

Set Rank Dict to Reference for Sorting, Etc.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You may supply a new |deck|/|stack| instance with a rank dict, which it will refer to when sorting, etc. If none is provided, it defaults to ``pydealer.const.DEFAULT_RANKS``.

.. code-block:: python

    import pydealer
    from pydealer.const import POKER_RANKS

    # Set the default rank dict to reference.
    deck = pydealer.Deck(ranks=POKER_RANKS)

You can, of course always change the rank dict after instantiation as well.

.. code-block:: python

    deck.ranks = POKER_RANKS

Construct a Deck that Rebuilds when Empty
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can construct a deck that will rebuild itself when you have dealt all of the cards from it, and try to deal any more, with the ``rebuild`` argument.

.. code-block:: python

    import pydealer

    # Construct a Deck instance, with 52 cards.
    deck = pydealer.Deck(rebuild=True)

    # If you want it shuffle when rebuilding:
    deck = pydealer.Deck(rebuild=True, re_shuffle=True)

----------------


Construct an Empty Stack
------------------------

Constructing a new, empty stack, for use as a hand, discard pile, etc., is as simple as constructing a deck.

.. code-block:: python

    import pydealer

    # Construct a Stack instance, for use as a hand in this case.
    hand = pydealer.Stack()

----------------


Shuffle a Stack/Deck
--------------------

Shuffling is also simple, and done probably exactly how you might expect. Pretty much everything with PyDealer is simple, because it's such a simple package.

.. code-block:: python

    import pydealer

    deck = pydealer.Deck()

    # Shuffle the deck, in place.
    deck.shuffle()

----------------


Sort a Stack/Deck
-----------------

Sorting is also done like you might expect.

.. code-block:: python

    import pydealer

    deck = pydealer.Deck()

    # Sort the deck, in place.
    deck.sort()

----------------


Deal Cards from a Stack/Deck
----------------------------

In this example we will create a |deck| instance, and then deal 7 cards from it.

.. code-block:: python

    import pydealer

    deck = pydealer.Deck()

    # Deal some cards from the deck.
    dealt_cards = deck.deal(7)

----------------


Add Cards to a Stack/Deck
-------------------------

Add to the Top
^^^^^^^^^^^^^^

In this example we will create a |deck| instance, representing a deck of cards, and a |stack| instance, which will represent a hand. We will then deal 7 cards from the deck, and add them to the exisiting hand.

.. code-block:: python

    import pydealer

    deck = pydealer.Deck()
    hand = pydealer.Stack()

    dealt_cards = deck.deal(7)

    # Add the cards to the top of the hand (Stack).
    hand.add(dealt_cards)

If you don't care where the dealt cards are placed in the |stack|, or are just adding them to the top, you can just use the ``+=`` operand to add cards to the top of a |stack|.

.. code-block:: python

    hand += deck.deal(7)

Add to the Bottom
^^^^^^^^^^^^^^^^^

You can also add cards to the bottom of a |stack|/|deck| as well, if that is preferred.

.. code-block:: python

    from pydealer.const import BOTTOM

    # Note that the constant ``BOTTOM`` is just the string ``"bottom"``.
    # The constant ``TOP`` is the string ``"top"``. This is the default value.
    hand.add(dealt_cards, end=BOTTOM)

Insert Card Into Position of a Stack/Deck
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can also insert a card into any given position (indice) of the |stack|/|deck|.

.. code-block:: python

    # ``deck`` is a Deck instance, and ``card`` is a Card instance. ``20`` is
    # the position (or indice) the card is inserted to.
    deck.insert(card, 20)

Insert List of Cards Into Position of a Stack/Deck
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can also insert a card into any given position (indice) of the |stack|/|deck|.

.. code-block:: python

    # ``stack`` is a Stack instance, and ``cards`` is a list of Card instances,
    # or a Stack/Deck instance. ``20`` is the  position (or indice) the card is
    # inserted into.
    stack.insert_list(cards, 20)

----------------


Retrieve a Card at a Given Stack/Deck Indice
--------------------------------------------

In this example we will retrieve (but not remove) the card at a given |deck| indice (or position, if you prefer). You can access the cards in a PyDealer |stack| or |deck| instance just like you would access the items in a list or other sequence in Python.

.. code-block:: python

    import pydealer

    deck = pydealer.Deck()

    # Access the indice of the ``Deck`` instance.
    card = deck[25]

----------------


Find Specific Card Locations in a Stack/Deck
--------------------------------------------

Single Card
^^^^^^^^^^^

In this example we will search for a given card in the deck. Users can search using full card names, abbreviations, suits, or values. Just remember that ``Deck.find`` (and ``Stack.find``) return the *indices* of the cards, not the cards themselves, and they always return a list, even if there is only one item in it.

.. code-block:: python

    import pydealer

    deck = pydealer.Deck()

    # Find the indice(s) of the Ace of Spades.
    indices = deck.find("Ace of Spades")

List of Cards
^^^^^^^^^^^^^

In this example we will search for a given list of cards in the deck. Users can search using full card names, abbreviations, suits, or values, or a mixture of any/all of those. Just remember that ``Deck.find_list`` (and ``Stack.find_list``) return the *indices* of the cards, not the cards themselves,  always return a list, even if there is only one item in it.

.. code-block:: python

    import pydealer

    deck = pydealer.Deck()

    # Construct a list of terms to search for.
    terms = ["Ace of Spades", "QH", "2", "Clubs"]

    # Find the indices of the cards matching the terms in the given list.
    indices = deck.find_list(terms)

----------------


Get & Remove Specific Cards from a Stack/Deck
---------------------------------------------

You can get & remove specific cards from a :class:`~pydealer.stack.Stack` or :class:`~pydealer.deck.Deck` instance with a given full card name, abbreviation, suit, value, or indice.

Note that the ``Stack`` and ``Deck`` "get methods" always return a list, even if there is only one item in it. And also remember that unlike ``Stack`` and ``Deck`` "find methods", which return indices, the ``Stack`` and ``Deck`` "get methods" return the card instances themselves.

Single Card
^^^^^^^^^^^

In this example we will retrieve and remove a given card from the deck. If there were more than one "Ace of Spades" in the deck, it would retrieve them all.

.. code-block:: python

    import pydealer

    deck = pydealer.Deck()

    # Get the card with the given name from the deck.
    cards = deck.get("Ace of Spades")

List of Cards
^^^^^^^^^^^^^

In this example we will retrieve and remove a given list of terms from the deck. For demonstration purposes, I am going to construct a mixed list of terms, including a full card name, abbreviation, face, suit, and indice, just to show that you can do that, if you really want to.

.. code-block:: python

    import pydealer

    deck = Deck()

    # Construct a list of terms to search for.
    terms = ["Queen of Hearts", "KD", "2", "Clubs", 25]

    # Get the cards matching the terms and indices in the given list.
    cards = deck.get_list(terms)

----------------


Empty a Stack/Deck
------------------

If, for some reason, you want to empty a Stack/Deck of it's cards, you can use the ``Stack.empty`` method. This will remove all of the cards from the Stack/Deck and will also return them in a list.

.. code-block:: python

    import pydealer

    deck = pydealer.Deck()

    deck.empty()
    # Or if you would like to keep the emptied cards elsewhere:
    cards = deck.empty()

----------------


Comparisons/Checks
==================

Get the Size of a Stack/Deck
----------------------------

To get the number of cards in a Stack/Deck, simply access the ``size`` property. It's the same as doing ``len(deck)``, which you could also do.

.. code-block:: python

    import pydealer

    deck = pydealer.Deck()

    deck_size = deck.size

----------------


Compare Two Stacks/Decks
------------------------

Using the :func:`~pydealer.utils.compare_stacks` function, you can compare two given ``Stack`` or ``Deck`` instances, checking whether or not they contain all of the same cards, based on card faces and suits, *not* card instance. This function *does not* take into account the ordering of either Stack/Deck.

.. code-block:: python

    import pydealer
    from pydealer.utils import compare_stacks

    deck_x = pydealer.Deck()
    deck_y = pydealer.Deck()

    result = compare_stacks(deck_x, deck_y)

If you care about the ordering of the Stack/Deck instances as well, you can simply use the ``==`` (or ``!=``) operand. This is the same as using the :func:`~pydealer.utils.compare_stacks` function, except it also takes into account the order of each Stack/Deck.

.. code-block:: python

    import pydealer
    from pydealer.utils import compare_stacks

    deck_x = pydealer.Deck()
    deck_y = pydealer.Deck()

    result = deck_x == deck_y

You can also, obviously, check whether two Stack/Deck are the same object, using ``is``.

.. code-block:: python

    import pydealer
    from pydealer.utils import compare_stacks

    deck_x = pydealer.Deck()
    deck_y = pydealer.Deck()

    result = deck_x is deck_y

----------------


Compare Two Cards
-----------------

You can compare two cards just as you would compare a couple of integers, using the standard operands (``==``, ``!=``, ``>``, ``>=``, ``<``, ``<=``). By default, it will compare based on ``DEFAULT_RANKS``.

.. code-block:: python

    import pydealer

    deck = pydealer.Deck()

    card_x = deck.deal()
    card_y = deck.deal()

    result = card_x == card_y
    result = card_x != card_y
    result = card_x > card_y
    result = card_x >= card_y
    result = card_x < card_y
    result = card_x <= card_y

If you would prefer to compare using a different rank dictionary, you can use the comparison methods built into the card, and supply the dictionary.

.. code-block:: python

    import pydealer
    from pydealer.const import POKER_RANKS

    deck = pydealer.Deck()

    card_x = deck.deal()
    card_y = deck.deal()

    result = card_x.eq(card_y, POKER_RANKS)  # ==
    result = card_x.ne(card_y, POKER_RANKS)  # !=
    result = card_x.gt(card_y, POKER_RANKS)  # >
    result = card_x.ge(card_y, POKER_RANKS)  # >=
    result = card_x.lt(card_y, POKER_RANKS)  # <
    result = card_x.le(card_y, POKER_RANKS)  # <=

----------------


Check if a Stack/Deck is Sorted
-------------------------------

Using the :func:`~pydealer.utils.check_sorted` function, you can check to see if the cards in a given Stack/Deck or list are sorted.

.. code-block:: python

    import pydealer
    from pydealer.utils import check_sorted

    deck = pydealer.Deck()

    result = check_sorted(deck)

----------------


Defining New Rank Dictionaries
==============================

Defining your own rank dictionaries, for use with sorting functions/methods, etc., is straight forward.

Rank dictionaries are just nested dictionaries containing a ``"values"`` dict, which itself contains all of the card values, and/or a ``"suits"`` dict, which itself contains all of the card suits, and their associated values.

.. code-block:: python

    # Define a new rank dict, ``new_ranks``, with ranks for card faces only.
    new_ranks = {
        "values": {
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
    }

    # Define a new rank dict, with ranks for card suits only.
    new_ranks = {
        "suits": {
            "Spades": 4,
            "Hearts": 3,
            "Clubs": 2,
            "Diamonds": 1
        }
    }

    # Define a new rank dict, with both faces & suits.
    new_ranks = {
        "values": {
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
        },
        "suits": {
            "Spades": 4,
            "Hearts": 3,
            "Clubs": 2,
            "Diamonds": 1
        }
    }
