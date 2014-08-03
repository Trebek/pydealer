==============================
PyDealer: Playing Card Package
==============================

A simple package for constructing ``Deck`` instances, of 52 common playing cards (also known as a French deck). Each card is a separate ``Card`` instance, with a name, value, suit, and abbreviation. Could possibly be used for a CLI card-based game, or even a graphical game as well. I suppose it might also be of interest to some beginner Python programmers, because of it's relative simplicity.

Attention
=========

If you are going to make a pull request, please do so on the dev branch, thanks. And make sure you are working on the latest version of the dev branch.

Install/Uninstall with PIP_
===========================

Install
-------
::

    pip install pydealer

Update
------
::

    pip install pydealer -U

Uninstall
---------
::

    pip uninstall pydealer

Basic Usage
===========

PyDealer has many other functions/methods that aren't described here. At the moment, you'll have to peruse the source to discover them (everything in the source is documented, and proper usage should be pretty easy to figure out). I am currently working on getting some proper documentation together, using Sphinx.

Deal Some Cards
---------------

In this example we will create a ``Deck`` instance, representing a deck of cards, and a ``Stack`` instance, which will represent a hand. We will then shuffle the deck, deal 7 cards from it, and add them to the hand.

::

    import pydealer

    deck = pydealer.Deck()
    hand = pydealer.Stack()

    deck.shuffle()

    dealt_cards = deck.deal(7)

    hand.add(dealt_cards)

    for card in hand:
        print card

**Example output:**
::

    9 of Clubs
    5 of Diamonds
    Ace of Diamonds
    Jack of Hearts
    10 of Diamonds
    4 of Clubs
    6 of Hearts

Retrieve a Card at a Given Deck Indice
--------------------------------------

In this example we will retrieve (but not remove) the card at a given deck indice (or position, if you prefer).

::

    import pydealer

    deck = pydealer.Deck()
    deck.shuffle()

    i = 25
    card = deck[i]

    print card

**Example output:**
::

    3 of Spades

Find Specific Card Locations
----------------------------

In this example we will search for a given card in the deck. Users can search using full card names, abbreviations, suits, or values. Just remember that ``Deck.find`` (and ``Stack.find``) always return a list, even if there is only one item.

Single Card
^^^^^^^^^^^
::

    import pydealer

    deck = pydealer.Deck()
    deck.shuffle()

    indices = deck.find("Ace of Spades")

    for i in indices:
        print "deck[%d] = %s" % (i, deck[i])

**Example output:**
::

    deck[28] = Ace of Spades

List of Cards
^^^^^^^^^^^^^

In this example we will search for a given list of cards in the deck. Users can search using full card names, abbreviations, suits, or values, or a mixture of any/all of those. Just remember that ``Deck.find_list`` (and ``Stack.find_list``) always return a list, even if there is only one item.

::

    import pydealer

    deck = pydealer.Deck()
    deck.shuffle()

    terms = ["AS", "Queen of Hearts", "2"]
    indices = deck.find_list(terms)

    for i in indices:
        print "deck[%d] = %s" % (i, deck[i])

**Example output:**
::

    deck[16] = 2 of Hearts
    deck[19] = Queen of Hearts
    deck[21] = 2 of Spades
    deck[24] = 2 of Diamonds
    deck[28] = 2 of Clubs
    deck[34] = Ace of Spades

Get & Remove Specific Cards
---------------------------

In this example we will retrieve and remove a given card from the deck. Users can get cards using full card names, abbreviations, suits, or values, or indices.

::

    import pydealer

    deck = Deck()
    deck.shuffle()

    card = deck.get("Ace of Spades")

    print card

**Example output:**
::

    Ace of Spades

Get & Remove a List of Cards
----------------------------

In this example we will retrieve and remove a given list of cards from the deck. Users can get cards using full card names, abbreviations, suits, or values, or indices, or a mixture of any/all of those.

::

    import pydealer

    deck = Deck()
    deck.shuffle()

    terms = ["KD", "Queen of Hearts", "2"]
    cards = deck.get_list(terms)

    for card in cards:
        print card

**Example output:**
::

    King of Diamonds
    Queen of Hearts
    2 of Diamonds
    2 of Clubs
    2 of Spades
    2 of Hearts

Relevant Links
==============

| `Standard 52-card deck Wikipedia Article <http://en.wikipedia.org/wiki/Standard_52-card_deck>`_
| `Playing card Wikipedia Article <http://en.wikipedia.org/wiki/Playing_card>`_

.. _PIP: https://pypi.python.org/pypi/pip/