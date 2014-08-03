#===============================================================================
# PyDealer - Constants
#-------------------------------------------------------------------------------
# Version: 1.4.0
# Updated: 03-08-2014
# Author: Alex Crawford
# License: MIT
#===============================================================================

"""
These are the few constants that are used by PyDealer. The poker ranks, and big
two ranks could be used by anyone making a game that relies on those ranks or
values. PyDealer references ``DEFAULT_RANKS`` by default, for sorting order,
and ordering of newly instantiated decks.

"""

#===============================================================================
# Card Data
#===============================================================================

SUITS = ["Diamonds", "Clubs", "Hearts", "Spades"]
FACES = ["2", "3", "4", "5", "6", "7", "8", "9","10",
         "Jack", "Queen", "King", "Ace"]

#===============================================================================
# Card Rank Dicts
#===============================================================================

POKER_RANKS = {
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

BIG2_RANKS = {
    "faces": {
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

DEFAULT_RANKS = {
    "faces": POKER_RANKS,
    "suits": BIG2_RANKS["suits"]
}

#===============================================================================
# Misc.
#===============================================================================

# Stack/Deck ends.
TOP = 0
BOTTOM = 1