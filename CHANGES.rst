##################
PyDealer Changelog
##################

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

--------


v1.4.0 (2015-01-10)
===================


Changes
-------


General
^^^^^^^

- PyDealer is now under a GPLv3 license. I know I probably shouldn't be switching licenses suddenly, but the MIT license was just a little too open for my liking. I like open, but I also like to have my rights protected, and to make sure that PyDealer, or anything derived from it, remains open source, literally.

- Moved all constants, classes, utility functions into their own separate files, because they're easier to manage that way, instead of having everything in one large file.
    - ``card.py`` contains the ``Card`` class.
    - ``const.py`` contains the few constants used by PyDealer.
    - ``deck.py`` contains the ``Deck`` class.
    - ``stack.py`` contains the ``Stack`` class.
    - ``utils.py`` contains all of the utility functions, which are used by the various methods/functions in the PyDealer package, but can also be used on their own as well though.
- Changed the ``values`` argument name, in the following helper functions, to ``ranks``, because it makes more sense to me.
    - ``check_sorted``
    - ``sort_card_indices``
    - ``sort_cards``
- All of the sorting methods & functions now sort by ``DEFAULT_RANKS`` by default, instead of ``POKER_RANKS``. ``Deck`` instances are also built using this order.


card.py
^^^^^^^

- The attribute name ``Card.value`` is now ``Card.face``, because it makes more sense.
- The ``Card`` comparison magic methods now use ``pydealer.const.DEFAULT_RANKS`` instead of ``pydealer.const.POKER_RANKS`` for comparisons. If a user would rather use some other rank dict, they can use the newly added comparison functions described below, in the features section.


const.py
^^^^^^^^

- Merged the constant ``NUMBERS`` with ``FACES``. There was no point in having them separate.
- The ``"values"`` key in ``DEFAULT_RANKS``, and ``BIG2_RANKS`` is now named ``"faces"``, to match the change of the ``Card`` attribute name, described aboved, in the changes section.
- ``POKER_RANKS`` now has a ``"faces"`` key, to work with tweaked sorting functions.
- Removed ``BLACKJACK_VALS``, because it was pretty much useless, not being used for anything, and can be easily reproduced by anyone that needed it.


deck.py
^^^^^^^

- ``Deck.deal`` now returns a ``Stack`` instance, instead of a list.
- ``Deck.deal`` no longer accepts the arguments ``rebuild`` or ``shuffle``. They are now ``Deck`` attributes that you can set on instantiation. You may also change them any time afterwards as well.
- ``Deck.__init__`` now recieves a single ``**kwargs`` argument. The accepted arguments are still the same though. The only difference is that when providing cards on instantiation, you have to use the argument ``cards=<cards>``, where ``<cards>`` is a list of Card instances, or a ``Stack``/``Deck`` instance.
- Removed the argument ``sort`` from ``Deck.__init__``, and ``Deck.build``, because decks are built sorted by default now.


stack.py
^^^^^^^^

- ``Stack.deal`` now returns a ``Stack`` instance, instead of a list.
- ``Stack.__init__`` now recieves a single ``**kwargs`` argument. The accepted arguments are still the same. The only difference is that when providing cards, you have to use the argument ``cards=<cards>``, where ``<cards>`` is a list of Card instances, or ``Stack``/``Deck``.
- Changed the ``Stack.__eq__`` (and ``Deck.__eq__``) magic method, so that it doesn't compare instance type anymore, and so that it takes into account the ordering of the cards as well. This allows you to compare a ``Stack`` instance to a ``Deck`` instance, and vice versa, or compare a ``list`` of ``Cards`` instances to a ``Stack``/``Deck``.
- Removed the ``__iter__`` method. Was pointless.


Features
--------

General
^^^^^^^

- Added tests (98 of them). You can run all of the tests by running ``test_suite.py``, in the "tests" folder. May try out nose for testing, and Travis CI at a later date.
- Added documentation. It can be viewed at pydealer.readthedocs.org.
- Sorting now works with Jokers. They will always be at the bottom of the deck after sorting, when using any of the provided rank dicts.


card.py
^^^^^^^

- Added the comparison methods ``Card.ge``, ``Card.gt``, ``Card.le``, ``Card.lt``, ``Card.eq``,and ``Card.ne``, in case a user wants more control over which rank dict is used for ``Card`` rank/value comparisons. All of the functions accept the arguent ``ranks``, which can be ``DEFAULT_RANKS``, ``POKER_RANKS``, ``BIG2_RANKS``, or any other rank dict matching the pattern of the included rank dicts. The default is ``DEFAULT_RANKS``.


const.py
^^^^^^^^

- Added the constant ``DEFAULT_RANKS``, which is the default sorting order for sorting methods & functions, and freshly built ``Deck`` instances. It is a combination of ``POKER_RANKS`` and ``BIG2_RANKS``. The order of ``DEFAULT_RANKS``, from least to greatest value, is 2 - 10, Jack, Queen, King, and Ace, for card faces, and Diamonds, Clubs, Hearts, and Spades for card suits.
- Added the constants ``TOP`` and ``BOTTOM``, which are used by the ``end`` argument in ``Stack.deal``, ``Deck.deal``, and ``Stack.add``, to respresent the top and bottom of a ``Stack`` or ``Deck`` instance. They are just ints (``0``, and ``1`` respectively).


deck.py
^^^^^^^

- Added the bool argument ``rebuild`` to ``Deck.__init__``, to set whether or not the deck will be rebuilt when all of the cards are dealt from it.
    - Added the attribute ``Deck.rebuild``, to keep track of whether or not to rebuild. This way, you don't have to pass the ``rebuild`` argument to ``Deck.deal``. You can always turn rebuilding off with ``Deck.rebuild = False`` (or on with ``Deck.rebuild = True``). It is ``False`` by default.
- Added the bool argument ``re_shuffle`` to ``Deck.__init__``, to set whether or not the deck will be shuffled when/if it's rebuilt.
    - Added the attribute ``Deck.re_shuffle``, to keep track of whether or not to shuffle when rebuilding. This way, you don't have to pass the ``rebuild`` argument to ``Deck.deal``. You can always turn rebuild shuffling off with ``Deck.re_shuffle = False`` (or on with ``Deck.re_shuffle = True``). It is ``False`` by default.
- Added the attribute ``Deck.jokers``, which keeps track of whether the deck was built with jokers.
- Added the attribute ``Deck.num_jokers`` which keeps track of how many jokers the deck was built with.
- Added the function ``convert``, which will take a given ``Stack`` instance and return a new ``Deck`` instance, with the same cards.
- Added the argument ``end`` to ``Deck.deal``. It allows you to specify which end of the Deck to deal from (top or bottom). It accepts either ``0`` (top) or ``1`` (bottom).
- You can now add a list of ``Card`` instances, or a ``Stack``/``Deck`` instance to a ``Deck`` instance, using the ``+`` operand (or ``+=``).


stack.py
^^^^^^^^

- Added a ``Stack`` class, to represent a generic "card container", used to hold and work with cards (could be used as a hand, or a discard pile, etc.). It is essentially the old ``Deck`` class, with a new name, and a number of new methods. The ``Deck`` class is now just a subclass of ``Stack``, with a few extra methods, particular to decks.
    - All methods available to the ``Stack`` class are also available to the ``Deck`` class as well.
- Added the method ``Stack.add``, to add given card(s) to the stack.
    - Has one argument, ``end``, which can be either ``0`` (top) or ``1`` (bottom). ``end`` determines which end of the ``Stack`` the card(s) get added to.
- Added the method ``Stack.sort``, to sort a stack in place.
- Added the method ``Stack.split``, for splitting a stack in half, or at a given indice, and returning the two halves, as separate ``Stack`` instances.
- Added the method ``Stack.reverse``, which reverses the stack in place.
- Added the method ``Stack.save_cards``, for saving the cards in a stack, in plain text format in a txt file. Card order is maintained.
- Added the method ``Stack.open_cards``, for opening the cards in plain text files of cards generated by ``Stack.save_cards`` or ``pydealer.utils.save_cards``. Card order is maintained.
- Added the method ``Stack.empty``, which removes all cards from the stack and returns them as a list.
    - Has one argument, ``return_cards``, which accepts a bool value, and determines whether or not the cards are returned.
- Added the method ``Stack.random_card`` for getting a random card from the stack.
    - Has one argument, ``remove``, which accepts a bool value, and determines whether or not to remove the random card from the ``Stack``.
- Added the method  ``Stack.insert``, for inserting a card into the stack at a given indice.
- Added the method  ``Stack.insert_list``, for inserting a list of cards into a stack, at the given indice.
- Added the method ``Stack.count``, for counting the number of a card that matches a given term.
- Added the method ``Stack.count_list``, for counting the number of cards that match a given list of terms.
- Added the argument ``end`` to ``Stack.deal``. It allows a user to specify which end of the stack to deal from (top or bottom). It accepts either ``0`` (top) or ``1`` (bottom).
- Added the argument ``limit`` to ``Stack.find``, ``Stack.find_list``, ``Stack.get`` and ``Stack.get_list``. It lets a user specify a limit on how many items to retrieve for each term. For example, if you used ``Stack.get_list(["A", "2"], limit=1)`` then ``Stack.get_list`` would return only the first Ace, and first 2 that it found, instead of all 4 Aces and all 4 2s. ``Stack.get_list(["A", "2"], limit=2)`` would return the first and second Ace and 2 that it found, etc.
- Added the function ``convert``, which will take a given ``Deck`` instance and return a new ``Stack`` instance, with the same cards.
- Added ``Stack.__ne__``, so that ``!=`` comparisons should work properly now.
- Fleshed out ``Stack.__getitem__``, so ``Stack`` and ``Deck`` instances cards can now be accessed, sliced, or reversed like lists, like you might expect.
- Added the attribute ``Stack.ranks``, which allows you to set the rank dict to use for sorting methods, etc. You can set it on instantiation using the argument ``ranks=<rank_dict>``, or any time afterwards using ``Stack.ranks = <rank_dict>``, where ``<rank_dict>`` is the rank dict to use.
- You can now add a list of ``Card`` instances, or a ``Stack``/``Deck`` instance to a ``Stack`` instance, using the ``+`` operand (or ``+=``).


utils.py
^^^^^^^^

- Moved the function ``check_term`` to ``pydealer.utils``.
- Moved the function ``compare_stacks`` to ``pydealer.utils``.
- Moved the function ``sort_card_indices`` to ``pydealer.utils``.
- Moved the function ``sort_cards``  to ``pydealer.utils``.
- Added the function ``build_cards`` that builds and returns a list containing a full deck of ``Card`` instances (a French deck of 52 cards). I basically moved the meat of ``Deck.build`` out of that method, and into a separate helper function. ``Deck.build`` now calls ``build_cards``. I did this so that users can use the card building function as a standalone function, if they wish.
- Added the function ``check_sorted`` to check whether the given cards (a ``Stack``, ``Deck``, or list of ``Card`` instances) are sorted (by default ranks, poker ranks or big two ranks).
- Added the function ``find_card``, for finding a card with the given term, in the given ``Stack``, ``Deck``, or list of cards.
- Added the function ``find_list``, for finding cards with the given list of terms, in the given ``Stack``, ``Deck``, or list of cards.
- Added the function ``get_card``, for getting, and removing a card with the given term, from the given ``Stack``, ``Deck``, or list of cards.
- Added the function ``get_list``, for getting, and removing cards with the given list of terms, from the given ``Stack``, ``Deck``, or list of cards.
- Added the function ``open_cards`` for opening a plain txt list of cards, generated by ``save_cards`` or ``Stack.save_cards``.
- Added the function ``random_card``, which will return a random card from a given ``Stack`` instance, ``Deck`` instance, or ``list`` of ``Card`` instances.
- Added the function ``save_cards`` for saving a hand, deck, or list of cards in plain text, to a txt file. Card order is maintained.


Refactoring
-----------

General
^^^^^^^

- All modules now use absolute imports.
- ``__init__.py`` imports all of the classes, for easier, more convenient access. Users can import any class using ``from pydealer import <class>``, or ``import pydealer.<class>``, instead of ``from pydealer.<module> import <class>``, or ``import pydealer.<module>.<class>``. Users may still do it the longer way though, if that is prefered. Actually, the longer ways are probably the more "proper" ways to do it. Utility functions can be imported using ``from pydealer.utils import <function>`` or ``import pydealer.utils.<function>``.


deck.py
^^^^^^^

- The ``Deck`` class is now just a subclass of the ``Stack`` class, with a few extra methods.


stack.py
^^^^^^^^

- Tweaked ``Stack.get``, and ``Stack.get_list``.
    - Changed ``Stack.get`` and ``Stack.get_list`` so that they don't rely on ``deque.remove`` to remove cards from the deck, which was relatively slow. They now just make a new copy of the cards in the deck, minus the gotten cards, using list comprehensions, and assign it to ``self.cards``.
    - Did away with a slow ``for`` loop in ``Stack.get_list``. The loop made repeated calls (once for each term) to ``Stack.find``, and repeated addition to a list. Now makes one call to ``Stack.find_list``, and one list assignment. Now takes about 1/3rd the time.
- Added the property ``Stack.cards`` that, when assigning cards to ``Stack.cards`` directly, converts the given list of ``Card`` instances, or cards in a ``Stack``/``Deck`` to a deque first.


utils.py
^^^^^^^^

- Did away with all of the rank dict checks in ``sort_card_indices`` and ``sort_cards``. Should be slightly faster, and more generic now, meaning a user can feed in his own dictionary, as long as it follows the pattern of the included rank dicts.
- ``sort_card_indices`` and ``sort_cards`` are now a little more flexible, and can sort by just suit now as well, if provided with a rank dict that only has suit ranks, instead of only being able to sort by either face or face & suit, .


Bugfixes
--------

General
^^^^^^^

card.py
^^^^^^^

- Fixed the comparison magic methods in ``Card``, so they now work properly in Python 3.
- Fixed a bug in the ``Card.__eq__`` magic method (changed an ``and`` to an ``or``).
- Fixed ``card_abbrev`` so that it properly abbreviates 10s now.


stack.py
^^^^^^^^

- Fixed the division in ``Stack.split``. It now uses floor division (``//``), so it works with Python 3.


Other
-----


General
^^^^^^^

- Tried to clarify a few docstrings.
- Got rid of all trailing/extra spaces.
- Fixed up the readme a bit.
    - Added syntax highlighting to the examples.


utils.py
^^^^^^^^

- Added missing argument descriptions to the docstrings of ``sort_card_indices`` and ``sort_cards``.

--------

v1.3.0 (2014-07-03)
===================


Changes
-------

- Added a couple of extra arguments to ``Deck.__init__``.
    - ``Deck.__init__`` now takes a list of cards as the first argument, ``cards``, so you can instantiate a deck with a given list of cards.
    - You can now prevent a ``Deck`` from building itself automatically, on instantiation, with the bool argument ``build``. If ``build=False``, the ``Deck`` skips building.
- ``Deck.find``, and ``Deck.get`` no longer accept lists of terms, and only accept a single term. I have made separate methods for finding/getting lists of terms (see the features section below).
    - These methods also only return lists (empty or otherwise) now.
- Scrapped ``Deck.peek``, because it was pretty much useless.
- The abbreviation for jokers is now "JKR", instead of "JK".


Features
--------

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
-----------

- Changed ``Deck.cards`` to a deque, instead of a list.
- Tweaked the item retrieval methods ``Deck.find``, and ``Deck.find_list``, so that they use ``enumerate`` in their loops now, instead of getting card indexes using ``self.cards.index(card)``.
- Changed the ordering of the items in ``FACES``, and ``SUITS``, so that ``Deck`` instances are sorted by big two ranks by default, when built.


Bugfixes
--------

- Fixed ``check_term`` again. Should actually work with 10s now. Really.
- Added a dirty little try/except fix for the ``xrange`` function, because it doesn't exist in Python 3. If ``xrange`` can't be found, implying the package is being run under Python 3, then Python 3's ``range`` is assigned to the variable ``xrange``, using ``xrange = range``.
- Changed ``Deck.find``, so that it doesn't return lists with duplicates.


Other
-----

- Tweaked the function/method docstrings a bit, to try to make them easier to read.
- Updated the readme.
- Tweaked the section key at the top of the changelog slightly.

--------

v1.2.2 (2015-06-30)
===================


Bugfixes
--------

- Fixed ``check_term``, so that it works with Python 3.


Other
-----

- Filled out the docstring for ``Deck.__init__``.
- Filled out the docstring for ``Card.__init__``.
- Fixed a few little errors in the readme.

--------


v1.2.1 (2014-06-28)
===================


Bugfixes
--------

- Fixed the methods ``Deck.find``, ``Deck.get``, and ``Deck.peek``, so they don't throw an error when there is nothing to return. They now return ``None`` if nothing is found.


Other
-----

- Changed ``__init__.py``, so it now imports everything from the module, meaning you can now access the globals constants, and ``check_term``, when importing PyDealer.
- Stripped the extra "\n" at the end of the str representation of a ``Deck``.

--------


v1.2.0 (2014-06-25)
===================


Changes
-------

- Moved the constants ``Deck.SUITS``, ``Deck.FACES``, and ``Deck.NUMBERS`` out of ``Deck`` and into the global scope. They can now be accessed using ``SUITS``, ``FACES``, and ``NUMBERS``.
- Moved ``Deck.check_term`` out of ``Deck``, and into the global scope. It can now be accessed by calling ``check_term``.


Features
--------

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
-----------

- Refactored most of the methods in ``Deck``.
    - Refactored ``Deck.deal``.
    - Refactored ``Deck.find``.
    - Refactored ``Deck.get``.
- Refactored the methods in ``Card``.
    - Refactored ``Card.gen_abbrev``.
    - Refactored ``Card.gen_name``.
- Refactored ``check_term``


Bugfixes
--------

- Fixed ``Card.gen_abbrev``, so it now properly abbreviates 10s.


Other
-----

- Added argument & return value descriptions to the method & function docstrings.
- Reformatted the changelog, ``CHANGES.rst``.

--------

v1.1.0 (2014-06-22)
===================


Changes
-------

- Pydealer is now a proper package, that can be installed/uninstalled using PIP.
- No longer have to call ``Deck.build_deck`` after instantiating a deck. It it done on initialization now.
- Shortened a few method names.
    - ``Deck.build_deck`` is now ``Deck.build``.
    - ``Deck.find_cards`` is now ``Deck.find``.
    - ``Deck.get_cards`` is now ``Deck.get``.


Features
--------

- Decks can now be built with jokers.
    - This can be done by passing the argument ``jokers=True`` to ``Deck``, when instantiating:
        deck = pydealer.Deck(jokers=True)


Other
-----

- Negligibly optimized a few methods, by replacing some simple loops with list comprehensions.
- Fixed up the readme. Added simple usage examples.
- Fixed up the changelog, ``CHANGES.rst``.

--------


v1.0.0 (2014-05-11)
===================

- Initial release.