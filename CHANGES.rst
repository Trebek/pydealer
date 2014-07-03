==================
PyDealer Changelog
==================

**Changes** -- *Will probably break things*
    Major changes to the package/code.
**Features** -- *May or may not break things*
    New, added features/functionality.
**Refactoring** -- *Shouldn't break things*
    Changes/improvements to the code.
**Bugfixes** -- *Won't break things*
    Smaller bugfixes, fixing broken functionality.
**Other** -- *Won't break things*
    Any other changes that may be of note, such as updating/modifying of documentation.

v1.3.0 (03-07-2014)
-------------------

Changes
^^^^^^^

- Added a couple of extra arguments to ``Deck.__init__``.
    - ``Deck.__init__`` now takes a list of cards as the first argument, ``cards``, so you can instantiate a deck with a given list of cards.
    - You can now prevent a ``Deck`` from building itself automatically, on instantiation, with the bool argument ``build``. If ``build=False``, the ``Deck`` skips building.
- ``Deck.find``, and ``Deck.get`` no longer accept lists of terms, and only accept a single term. I have made separate methods for finding/getting lists of terms (see the features section below).
    - These methods also only return lists (empty or otherwise) now.
- Scrapped ``Deck.peek``, because it was pretty much useless.
- The abbreviation for jokers is now "JKR", instead of "JK".

Features
^^^^^^^^

- PyDealer is now hosted on the PyPi! Installing just got that much easier.
- ``Deck``s now store their ``Cards`` in a deque, instead of a list.
- Added ``Deck.find_list``, and ``Deck.get_list``, for retrieving items matching the terms in a given list.
- Added a ``sort`` kwarg to ``Deck``, ``Deck.build``, ``Deck.find``, ``Deck.find_list``, ``Deck.get`` and ``Deck.get_list``.
    - ``sort`` is a boolean argument, which, if ``True``, will sort the newly built ``Deck``, or results by poker rank, otherwise they are built/returned in the order they are created/found. Default is ``False``.
- Added the global function ``compare_decks``, for checking whether two ``Deck`` instances have the same cards (``Card`` suits & values, not ``Card``  instances).
- Added the global functions ``sort_cards``, and ``sort_card_indices``, for sorting given cards, or deck indices by poker ranks.
- Added the method ``Deck.set_cards``, to set a ``Deck``'s contents to a given list of cards at any time. You could just do ``Deck.cards = deque([Card, Card, ...])`` as well. This method just handles the extra step of converting a list to a deque.
- ``Deck.shuffle()`` now takes the argument ``times``, which is the number of times to shuffle.

Refactoring
^^^^^^^^^^^

- Changed ``Deck.cards`` to a deque, instead of a list.
- Tweaked the item retrieval methods ``Deck.find``, and ``Deck.find_list``, so that they use ``enumerate`` in their loops now, instead of getting card indexes using ``self.cards.index(card)``.
- Changed the ordering of the items in ``FACES``, and ``SUITS``, so that ``Deck``s are sorted by big two ranks by default, when built.

Bugfixes
^^^^^^^^

- Fixed ``check_term`` again. Should actually work with 10s now. Really.
- Added a dirty little try/except fix for the ``xrange`` function, because it doesn't exist in Python 3. If ``xrange`` can't be found, implying the package is being run under Python 3, then Python 3's ``range`` is assigned to the variable ``xrange``, using ``xrange = range``.
- Changed ``Deck.find``, so that it doesn't return lists with duplicates.

Other
^^^^^

- Tweaked the function/method docstrings a bit, to try to make them easier to read.
- Updated the readme.
- Tweaked the section key at the top of the changelog slightly.

v1.2.2 (30-06-2014)
-------------------

Bugfixes
^^^^^^^^

- Fixed ``check_term``, so that it works with Python 3.

Other
^^^^^

- Filled out the docstring for ``Deck.__init__``.
- Filled out the docstring for ``Card.__init__``.
- Fixed a few little errors in the readme.

v1.2.1 (28-06-2014)
-------------------

Bugfixes
^^^^^^^^

- Fixed the methods ``Deck.find``, ``Deck.get``, and ``Deck.peek``, so they don't throw an error when there is nothing to return. They now return ``None`` if nothing is found.

Other
^^^^^

- Changed ``__init__.py``, so it now imports everything from the module, meaning you can now access the globals constants, and ``check_term``, when importing PyDealer.
- Stripped the extra "\n" at the end of the str representation of a ``Deck``.

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