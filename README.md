PyDealer: Playing Card Simulator
=============================

A module containing classes/methods for simulating decks of playing cards (standard 'French deck'). Could possibly be used for a command prompt/console, card-based game.

**[See a demo.](http://repl.it/MVy/1)**

**Features:**

- Generates a standard 'French deck' of 52 playing cards.
- Can shuffle the deck.
- Can deal a specified number of cards from the deck.
    - When a deck runs out of cards while dealing, PyDealer, by default, builds a new deck, shuffles, and continues on. This is togglable.
- Can find the locations of all of the cards of a given value, suit, name, or abbreviation.
- Can peek at a card in a given location in the deck.
- Each card is it's own object, with a value (Ace, Queen, 2, etc.), a suit (Spades, Hearts, Clubs, etc.), a name ("Ace of Spades", "2 of Clubs", "Queen of Hearts", etc.), and an abbreviation ("AS", "2C", "QH", etc.).

**Relevant links:**  

[Standard 52-card deck Wikipedia Article](http://en.wikipedia.org/wiki/Standard_52-card_deck)  
[Playing card Wikipedia Article](http://en.wikipedia.org/wiki/Playing_card)  
