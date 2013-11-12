#===============================================================================
# PyDeck
#-------------------------------------------------------------------------------
# Version: 0.1.1
# Updated: 11-11-2013
# Author: Alex Crawford
# License: MIT
#===============================================================================

"""A fairly useless module, containing a class with methods for instantiating / 
generating a French deck of 52 cards (common playing cards). Also has methods
for shuffling the deck, and dealing (returning) cards from the deck. Each card
is an object with a name, abbreviation, and value.
"""

#===============================================================================
# IMPORTS
#===============================================================================

from random import shuffle as shuff

#===============================================================================
# CLASSES
#===============================================================================

class Deck(object):
    """Class and methods for generating a deck of standard poker cards."""

    def __init__(self):
        """deck = Deck()
        
        Deck init method.
        """
        self.cards = []
        
        self.gendeck()
        
    def gendeck(self):
        """deck.gendeck()
        
        Fills an instantiated deck with cards (unshuffled).
        """
        cardleft = 52
        numleft = 9
        value = 2
        tempdeck = []
        
        while cardleft > 0:
            while numleft > 0:
                for suit in Card.SUITS:
                    tempdeck.append(Card(value, suit))
                    cardleft -= 1
                value += 1
                numleft -= 1
            for face in Card.FACES:
                for suit in Card.SUITS:
                    tempdeck.append(Card(face, suit))
                    cardleft -= 1
            for suit in Card.SUITS:
                tempdeck.append(Card('Ace', suit))
                cardleft -= 1

        self.cards = tempdeck
        
    def shuffle(self):
        """deck.shuffle()
        
        Shuffles the deck instance.
        """
        shuff(self.cards)

    def size(self):
        """deck.size() -> number of cards left in deck
        
        Returns the number of cards left in the deck.
        """
        return len(self.cards)

    def dealcards(self, numx=1):
        """deck.dealcard([numx]) -> list of dealt cards
        
        numx = Number of cards to deal
        
        Returns a list of dealt cards.
        """
        dealt = False
        count = 0
        left = numx
        cards = []
        
        while len(self.cards) > 0 and not dealt:
            while left > 0:
                if len(self.cards) > 0:
                    _card = self.cards.pop()
                    cards.append(_card)
                    left -= 1
                    count += 1
                else:
                    print 'Out of cards. Getting a new deck.'
                    self.gendeck()
                    shuff(self.cards)
                    left = numx
                    cards = []
            dealt = True
        
        return cards


class Card(object):
    """Class for individual cards."""

    SUITS = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
    FACES = ['King','Queen','Jack']

    def __init__(self, value, suit):
        """Card init method."""

        self.suit = suit.capitalize()
        
        if type(value) is str:
            self.name = str(value) + " of " + str(suit)
            self.abbr = str(value)[0] + str(suit)[0]
        else:
            self.name = str(value) + " of " + str(suit)
            self.abbr = str(value) + str(suit)[0]
        
        if type(value) is int:
            self.value = value
        elif value in self.FACES:
            self.value = 10
        else:
            self.value = value.capitalize()

#===============================================================================
# TEST FUNCTION
#===============================================================================

def sect(title):
    """Prints a given title, with separators above and below it."""
    sep = "-" * 24
    
    print(sep)
    print title
    print(sep + "\n")

def test():
    """A function for testing the module."""
    nl = "\n"

    # Instantiate a deck, and fill it with cards.
    sect("Deck Instantiation")

    print("Instantiating deck / generating cards..." + nl)

    deck = Deck()
    #deck.gendeck()
    
    print("Number of cards: " + str(deck.size()) + nl)
    
    # Print out deck contents. Reversed so that top card on deck is first.
    sect("Deck Contents")

    print("Full names:" + nl)

    for card in reversed(deck.cards):
        print(card.name)
    print

    print("Abbreviated names:" + nl)

    for card in reversed(deck.cards):
        print(card.abbr + ','),
    print nl
    
    # Shuffle deck contents.
    sect("Shuffle Deck")
    
    print("Shuffling the deck...\n")
    
    deck.shuffle()
    
    # Print deck contents, post shuffle.
    sect("Deck Contents (Post Shuffle)")
    
    print("Full names:" + nl)
    
    for card in reversed(deck.cards):
        print(card.name)
    print

    print("Abbreviated names:" + nl)

    for card in reversed(deck.cards):
        print(card.abbr + ','),
    print nl
    
    # Deal 7 cards / display dealt cards / print number of cards left in deck.
    # Should be 45 cards left after dealing 7.
    sect("Deal Some Cards")
    
    print("Dealing cards..." + nl)
        
    hand = deck.dealcards(7)
    
    print(str(len(hand)) + " cards have been dealt:\n")

    print("Full names:" + nl)

    for card in hand:
        print(card.name)
    print
    
    print("Abbreviated names:" + nl)

    for card in hand:
        print(card.abbr + ','),
    print nl
    
    print("Cards left in deck: " + str(deck.size()) + nl)
    
#===============================================================================
# IF MAIN
#===============================================================================

if __name__ == '__main__':

    test()
    
    pass

