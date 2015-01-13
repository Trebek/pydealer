.. include:: globals.inc


##############################
PyDealer: Playing Card Package
##############################

.. image:: images/guy-1-256px-4.png
  :align: right

|pd| is a simple to use Python package for "simulating" decks of standard playing cards (also known as a |_fd|). PyDealer let's you easily create |deck| instances, each containing a full 52 card deck of playing cards. Each card is a separate |card| instance, with a name, value, suit, and abbreviation. There is also the |stack| class, which is useful for creating hands, or discard piles, etc. It is the backbone of the PyDealer package, and actually the ``Deck`` class is just a subclass of the ``Stack`` class.

|pd| could possibly be used as part of a CLI (command line interface) card-based game, or even a graphical game as well, I suppose. It may also be of interest to beginner Python programmers, since it's a relatively simple package, which I created as a way to learn Python, packaging, testing, documentation (Sphinx), etc. I even ended up learning how to use Git a bit, which I must say was slightly frustrating at first. This package has taught me a lot, and maybe someone else can benefit from it as well. Or maybe not. Either way, here it is.


Quick Usage Example
===================

Here is a quick example, using IDLE, demonstrating how to construct a new |deck| instance, representing a full |_fd| of cards, as well as how to shuffle the deck, and deal some cards (7 of them) from it, to a hand. We'll then sort the hand, and print a listing of it's contents, in a human readable way, with a simple print statement.

.. code-block:: pycon

    >>> import pydealer
    >>> deck = pydealer.Deck()
    >>> deck.shuffle()
    >>> hand = deck.deal(7)
    >>> hand.sort()
    >>> print hand
    2 of Diamonds
    5 of Hearts
    9 of Hearts
    9 of Spades
    Jack of Spades
    King of Clubs
    Ace of Clubs


Table of Contents
=================

.. toctree::
    :maxdepth: 3

    usage
    code
    license

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`