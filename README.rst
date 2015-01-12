==============================
PyDealer: Playing Card Package
==============================

|pd| is a simple to use Python package for "simulating" decks of standard playing cards (also known as a |fd|). PyDealer let's you easily create ``Deck`` instances, each containing a full 52 card deck of playing cards. Each card is a separate ``Card`` instance, with a name, value, suit, and abbreviation. There is also the ``Stack`` class, which is useful for creating hands, or discard piles, etc. It is the backbone of the PyDealer package, and actually the ``Deck`` class is just a subclass of the ``Stack`` class.

|pd| could possibly be used as part of a CLI (command line interface) card-based game, or even a graphical game as well, I suppose. It may also be of interest to beginner Python programmers, since it's a relatively simple package, which I created as a way to learn Python, packaging, testing, documentation (Sphinx), etc. I even ended up learning how to use Git a bit, which I must say was slightly frustrating at first. This package has taught me a lot, and maybe someone else can benefit from it as well. Or maybe not. Either way, here it is.

The PyDealer package can be found at the `Python Package Index`_, and should be downloaded from there, and, ideally, installed with `pip`_.

**Note to Developers**

If you want to work on this project, please make sure you are working on the latest version of the `dev branch <https://github.com/Trebek/pydealer/tree/dev>`_, and make your pull requests to that branch. Thanks.

Documentation
=============

Full documentation for PyDealer can be found on readthedocs.org:

`http://pydealer.readthedocs.org/en/latest/ <http://pydealer.readthedocs.org/en/latest/>`_


Quick Usage Example
===================

Here is a quick example, using IDLE, demonstrating how to construct a new |deck| instance, representing a full |fd| of cards, as well as how to shuffle the deck, and deal some cards (7 of them) from it, to a hand. Then we'll print a listing of the contents of the hand, in a human readable way, with a simple print statement.

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


Install/Update/Uninstall with `pip`_
====================================

I recommend downloading and installing `pip`_, if you haven't already, and using that to install PyDealer, from the `Python Package Index`_.

Enter one of the following commands into your \*nix Bash or Windows Command Prompt (after installing `pip`_).

Install
-------
::

    $ pip install pydealer

Update
------
::

    $ pip install pydealer -U

Uninstall
---------
::

    $ pip uninstall pydealer


Relevant Links
==============

.. | `PyDealer Documentation <https://readthedocs.org/>`_

| `Standard 52-card deck Wikipedia Article <http://en.wikipedia.org/wiki/Standard_52-card_deck>`_
| `Playing card Wikipedia Article <http://en.wikipedia.org/wiki/Playing_card>`_


.. Replacement Text/Links
.. ======================

.. _pip: https://pypi.python.org/pypi/pip/
.. _Python Package Index: https://pypi.python.org/pypi/pydealer/

.. |pd| replace:: PyDealer
.. |fd| replace:: French Deck

.. |card| replace:: ``Card``
.. |deck| replace:: ``Deck``
.. |stack| replace:: ``Stack``