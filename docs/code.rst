#################
API Documentation
#################

This is the PyDealer API documentation. It contains the documentation extracted from the docstrings of the various classes, methods, and functions in the PyDealer package. If you want to know what a certain function/method does, this is the place to look.

.. contents::
    :depth: 2


:mod:`card` Module
==================

`Source <https://github.com/Trebek/pydealer/blob/master/pydealer/card.py>`__

.. automodule:: pydealer.card
    :members:
    :undoc-members:


:mod:`stack` Module
===================

`Source <https://github.com/Trebek/pydealer/blob/master/pydealer/stack.py>`__

.. automodule:: pydealer.stack
    :members:
    :undoc-members:


:mod:`deck` Module
==================

`Source <https://github.com/Trebek/pydealer/blob/master/pydealer/deck.py>`__

.. automodule:: pydealer.deck
    :members:
    :undoc-members:
    :show-inheritance: :class:`pydealer.stack.Stack`


:mod:`tools` Module
===================

`Source <https://github.com/Trebek/pydealer/blob/master/pydealer/tools.py>`__

.. automodule:: pydealer.tools
    :members:
    :undoc-members:


:mod:`const` Module
===================

`Source <https://github.com/Trebek/pydealer/blob/master/pydealer/const.py>`__

.. automodule:: pydealer.const
    :members:
    :undoc-members:

.. data:: SUITS
.. code-block:: python

    ["Diamonds", "Clubs", "Hearts", "Spades"]

.. data:: VALUES
.. code-block:: python

    ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

.. data:: BIG2_RANKS
.. code-block:: python

    {
        "values": {
            "2": 13,
            "Ace": 12,
            "King": 11,
            "Queen": 10,
            "Jack": 9,
            "10": 8,
            "9": 7,
            "8": 6,
            "7": 5,
            "6": 4,
            "5": 3,
            "4": 2,
            "3": 1,
        },
        "suits": {
            "Spades": 4,
            "Hearts": 3,
            "Clubs": 2,
            "Diamonds": 1
        }
    }

.. data:: DEFAULT_RANKS
.. code-block:: python

    {
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

.. data:: POKER_RANKS
.. code-block:: python

    {
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

.. data:: TOP
.. code-block:: python

    "top"

.. data:: BOTTOM
.. code-block:: python

    "bottom"