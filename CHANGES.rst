==================
PyDealer Changelog
==================

v1.1.0 (22-06-2014)
------------------

- Pydealer is now a proper package, that can be installed/uninstalled using PIP.
- Shortened a few method names.
    - ``Deck.build_deck`` is now ``Deck.build``.
    - ``Deck.find_cards`` is now ``Deck.find``.
    - ``Deck.get_cards`` is now ``Deck.get``.
- Decks can now be built with jokers.
    - This can be done by passing the argument ``jokers=True`` to ``Deck``, when instantiating:
        deck = pydealer.Deck(jokers=True)
- No longer have to call ``Deck.build_deck`` after instantiating a deck. It it done on initialization now.
- Negligibly optimized a few methods, by replacing some simple loops with list comprehensions.
- Fixed up the readme. Added a simple usage examples.
- Fixed up the changelog.

v1.0.0 (11-05-2014)
------------------

- Initial release.