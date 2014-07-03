==============================
PyDealer: Playing Card Package
==============================

A simple package for constructing ``Deck`` instances, of 52 common 
playing cards. Each card is a separate ``Card`` instance, with a name, value, 
suit, and abbreviation. Could possibly be used for a CLI card-based game, or even a graphical game as well, I suppose.

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

Make a Deck, Deal Some Cards
----------------------------
::

    import pydealer

    deck = pydealer.Deck()
    deck.shuffle()

    hand = deck.deal(7)

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

Peek at a Deck Indice
---------------------
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

You can search using full card names, abbreviations, suits, or values.

Single Card
^^^^^^^^^^^
::

    import pydealer

    deck = pydealer.Deck()
    deck.shuffle()

    name = "Ace of Spades"
    i = deck.find(name)

    card = deck[i]
    print "deck[%d] = %s" % (i, card)

**Example output:**
::

    deck[28] = Ace of Spades

List of Cards
^^^^^^^^^^^^^
The list can contain full card names, abbreviations, suits, values, or a mixture of any/all of them.
::

    import pydealer

    deck = pydealer.Deck()
    deck.shuffle()

    terms = ["AS", "Queen of Hearts", "2"]
    indices = deck.find_list(terms)

    for i in indices:
        card = deck[i]
        print "deck[%d] = %s" % (i, card)

**Example output:**
::

    deck.cards[16] = 2 of Hearts
    deck.cards[19] = Queen of Hearts
    deck.cards[21] = 2 of Spades
    deck.cards[24] = 2 of Diamonds
    deck.cards[28] = 2 of Clubs
    deck.cards[34] = Ace of Spades

Get & Remove Specific Cards
---------------------------
::

    import pydealer

    deck = Deck()
    deck.shuffle()

    name = "Ace of Spades"
    card = deck.get(name)

    print card

**Example output:**
::

    Ace of Spades

Get & Remove a List of Cards
----------------------------
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