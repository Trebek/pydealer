==================
PyDealer Changelog
==================

v1.2.0 (25-06-2014)
-------------------

Changes
^^^^^^^

- Moved the constants ``Deck.SUITS``, ``Deck.FACES``, and ``Deck.NUMBERS`` out of ``Deck`` and into the global scope. They can now be accessed using ``SUITS``, ``FACES``, and ``NUMBERS``.
- Moved ``Deck.check_term`` out of ``Deck``, and into the global scope. It can now be accessed by calling ``check_term``.

Features
^^^^^^^^

- Added some magic methods to the ``Card``, and ``Deck`` objects.
    - Added to ``Card``:
        - ``__eq__``
        - ``__gt__``
        - ``__hash__``
        - ``__repr__``
        - ``__str__``
    - Added to ``Deck``:  
        - ``__add__``
        - ``__contains__``
        - ``__delitem__``
        - ``__eq__``
        - ``__getitem__``
        - ``__iter__``
        - ``__len__``
        - ``__repr__``
        - ``__setitem__``
        - ``__str__``
- Added a few global constants, for use with some common card games:
    - ``POKER_RANKS``, which is a dict of poker ranks.
        - This is also used by ``Card.__gt__``.
    - ``BIG2_RANKS``, which is a dict of ranks for the game Big Two (Deuces).
    - ``BLACKJACK_VALS``, which is a dict of card values for Black Jack (Twenty One).
- ``Deck.peek``, in addition to accepting a single deck indice for an argument, can now accept a list of deck indices as well.
- ``Deck.get``, in addition to accepting card names/values/suits/abbrevs. as an argument, can now accept deck indices as well.

Refactoring
^^^^^^^^^^^

- Refactored most of the methods in ``Deck``.
    - Refactored ``Deck.deal``.
    - Refactored ``Deck.find``.
    - Refactored ``Deck.get``.
- Refactored the methods in ``Card``.
    - Refactored ``Card.gen_abbrev``.
    - Refactored ``Card.gen_name``.
- Refactored ``check_term``

Bugfixes
^^^^^^^^

- Fixed ``Card.gen_abbrev``, so it now properly abbreviates 10s.

Other
^^^^^

- Added argument & return value descriptions to the method & function docstrings.
- Reformatted the changelog, ``CHANGES.rst``.

v1.1.0 (22-06-2014)
-------------------

Changes
^^^^^^^

- Pydealer is now a proper package, that can be installed/uninstalled using PIP.
- No longer have to call ``Deck.build_deck`` after instantiating a deck. It it done on initialization now.
- Shortened a few method names.
    - ``Deck.build_deck`` is now ``Deck.build``.
    - ``Deck.find_cards`` is now ``Deck.find``.
    - ``Deck.get_cards`` is now ``Deck.get``.

Features
^^^^^^^^

- Decks can now be built with jokers.
    - This can be done by passing the argument ``jokers=True`` to ``Deck``, when instantiating:
        deck = pydealer.Deck(jokers=True)

Other
^^^^^

- Negligibly optimized a few methods, by replacing some simple loops with list comprehensions.
- Fixed up the readme. Added simple usage examples.
- Fixed up the changelog, ``CHANGES.rst``.

v1.0.0 (11-05-2014)
-------------------

- Initial release.