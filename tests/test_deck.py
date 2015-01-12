#===============================================================================
# PyDealer - Tests - Deck
#-------------------------------------------------------------------------------
# Version: 1.4.0
# Updated: 10-01-2015
# Author: Alex Crawford
# License: GPLv3
#===============================================================================

#===============================================================================
# Imports
#===============================================================================

import unittest

import pydealer


#===============================================================================
# TestDeck Class
#===============================================================================

class TestDeck(unittest.TestCase):

    def setUp(self):
        """"""
        self.deck = pydealer.Deck()
        self.empty_deck = pydealer.Deck(build=False)
        # pass

    def test_add(self):
        """"""
        self.empty_deck = self.empty_deck + self.deck

        self.assertEqual(self.empty_deck, self.deck)

    def test_build(self):
        """"""
        self.empty_deck.build()

        self.assertEqual(len(self.empty_deck.cards), 52)

    def test_deal(self):
        """"""
        card_names = ["Ace of Spades", "Ace of Hearts",
                 "Ace of Clubs", "Ace of Diamonds"]

        dealt_cards = self.deck.deal(4)

        for i, name in enumerate(card_names):
            self.assertEqual(dealt_cards[i].name, name)

    def test_deal_rebuild(self):
        """"""
        card_names = ["Ace of Spades", "Ace of Hearts",
                 "Ace of Clubs", "Ace of Diamonds"]

        self.deck.rebuild = True

        dealt_cards = self.deck.deal(53)

        self.assertEquals(self.deck.size, 51)

    def test_repr(self):
        """"""
        result = repr(self.empty_deck)

        self.assertEquals(result, "Deck(cards=deque([]))")


# if __name__ == '__main__':
#     unittest.main()