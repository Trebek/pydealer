==============================
PyDealer: Playing Card Package
==============================

A simple package for constructing a ``Deck`` object, of 52 common 
playing cards. Each card is a separate ``Card`` object, with a name, value, 
suit, and abbreviation. Could possibly be used for a command prompt/console, card-based game, or even a graphical game as well, I suppose.

Attention
=========

If you are going to make a pull request, please do so on the dev branch, thanks. And make sure you are working on the latest version of the dev branch.

Install/Uninstall with PIP_
===========================

Install Latest Version
----------------------
::

    pip install https://github.com/Trebek/pydealer/archive/master.zip

Install Development Version
---------------------------
::

    pip install https://github.com/Trebek/pydealer/archive/dev.zip

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

Peek at Specific Deck Indice
----------------------------
::

    import pydealer

    deck = pydealer.Deck()
    deck.shuffle()

    i = 25
    card = deck.peek(i)

    print card

**Example output:**
::

    3 of Spades

Find Specific Card(s) Locations
-------------------------------

You can search using full card names, abbreviations, suits, or values.

Single Card
^^^^^^^^^^^
::

    import pydealer

    deck = pydealer.Deck()
    deck.shuffle()

    name = "Ace of Spades"
    i = deck.find(name)

    card = deck.peek(i)
    print "deck.cards[%d] = %s" % (i, card)

**Example output:**
::

    deck.cards[28] = Ace of Spades

List of Cards
^^^^^^^^^^^^^
The list can contain full card names, abbreviations, suits, values, or a mixture of any/all of them.
::

    import pydealer

    deck = pydealer.Deck()
    deck.shuffle()

    terms = ["AS", "Queen of Hearts", "2"]
    indices = deck.find(terms)

    for i in indices:
        card = deck.peek(i)
        print "deck.cards[%d] = %s" % (i, card)

**Example output:**
::

    deck.cards[16] = 2 of Hearts
    deck.cards[19] = Queen of Hearts
    deck.cards[21] = 2 of Spades
    deck.cards[24] = 2 of Diamonds
    deck.cards[28] = 2 of Clubs
    deck.cards[34] = Ace of Spades

Get & Remove Specific Card(s)
-----------------------------
::

    import pydealer

    deck = Deck()
    deck.shuffle()

    name = "Ace of Spades"
    card = deck.get(name)

    print card

    terms = ["KD", "Queen of Hearts", "2"]
    cards = deck.get(terms)

    for card in cards:
        print card

**Example output:**
::

    Ace of Spades
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