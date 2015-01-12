#===============================================================================
# PyDealer - Tests - Tools
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
# TestTools Class
#===============================================================================

class TestTools(unittest.TestCase):

    def setUp(self):
        """"""
        self.ace_spades = pydealer.Card("Ace", "Spades")
        self.two_diamonds = pydealer.Card("2", "Diamonds")
        self.queen_hearts = pydealer.Card("Queen", "Hearts")
        self.seven_clubs = pydealer.Card("7", "Clubs")
        self.cards = [self.ace_spades, self.two_diamonds, self.queen_hearts,
                      self.seven_clubs]
        self.names = ["Ace of Spades", "2 of Diamonds", "Queen of Hearts",
                      "7 of Clubs"]
        self.deck = pydealer.Deck()
        self.stack = pydealer.Stack(cards=self.cards)
        # pass

    def find_list_helper(self, stack, got_cards):
        """"""
        self.assertEqual(len(got_cards), 4)

        for i, name in enumerate(self.names):
            self.assertEqual(stack[got_cards[i]].name, name)

    def get_list_helper(self, left, got_cards):
        """"""
        self.assertEqual(len(got_cards), 4)
        self.assertEqual(len(left), 0)

        for i, name in enumerate(self.names):
            self.assertEqual(got_cards[i].name, name)

    def test_build_cards(self):
        """"""
        cards = pydealer.tools.build_cards()

        self.assertEqual(list(self.deck.cards), cards)

    def test_check_sorted(self):
        """"""
        result = pydealer.tools.check_sorted(self.deck)

        self.assertEqual(result, True)

    def test_check_term(self):
        """"""
        result = pydealer.tools.check_term(self.deck[0], "2 of Diamonds")

        self.assertEqual(result, True)

    def test_compare_stacks(self):
        """"""
        other_deck = pydealer.Deck()

        result = pydealer.tools.compare_stacks(self.deck, other_deck)

        self.assertEqual(result, True)

    def test_find_card_abbrev(self):
        """"""
        found = pydealer.tools.find_card(self.deck, "AS")
        i = found[0]

        self.assertEqual(len(found), 1)
        self.assertEqual(self.deck[i].name, "Ace of Spades")

    def test_find_card_full(self):
        """"""
        found = pydealer.tools.find_card(self.deck, "Ace of Spades")
        i = found[0]

        self.assertEqual(len(found), 1)
        self.assertEqual(self.deck[i].name, "Ace of Spades")

    def test_find_card_partial_value(self):
        """"""
        found = pydealer.tools.find_card(self.deck, "Ace")

        self.assertEqual(len(found), 4)
        for i in found:
            self.assertEqual(self.deck[i].value, "Ace")

    def test_find_card_partial_suit(self):
        """"""
        found = pydealer.tools.find_card(self.deck, "Spades")

        self.assertEqual(len(found), 13)
        for i in found:
            self.assertEqual(self.deck[i].suit, "Spades")

    def test_find_card_limit(self):
        """"""
        found = pydealer.tools.find_card(self.deck, "Spades", limit=1)

        self.assertEqual(len(found), 1)

    def test_find_list_full(self):
        """"""
        full_list = ["Ace of Spades", "2 of Diamonds", "Queen of Hearts",
            "7 of Clubs"]

        found = pydealer.tools.find_list(self.stack, full_list)

        self.find_list_helper(self.stack, found)

    def test_find_list_abbrev(self):
        """"""
        abbrev_list = ["AS", "2D", "QH", "7C"]

        found = pydealer.tools.find_list(self.stack, abbrev_list)

        self.find_list_helper(self.stack, found)

    def test_find_list_partial_value(self):
        """"""
        partial_list = ["Ace", "2", "Queen", "7"]

        found = pydealer.tools.find_list(self.stack, partial_list)

        self.find_list_helper(self.stack, found)

    def test_find_list_partial_suit(self):
        """"""
        partial_list = ["Spades", "Diamonds", "Hearts", "Clubs"]

        found = pydealer.tools.find_list(self.stack, partial_list)

        self.find_list_helper(self.stack, found)

    def test_find_list_mixed(self):
        """"""
        mixed_list = ["AS", "2 of Diamonds", "Hearts", "7"]

        found = pydealer.tools.find_list(self.stack, mixed_list)

        self.find_list_helper(self.stack, found)

    def test_find_list_limit(self):
        """"""
        found = pydealer.tools.find_list(self.stack, ["Spades"], limit=1)

        self.assertEqual(len(found), 1)

    def test_get_card_abbrev(self):
        """"""
        left, got_cards = pydealer.tools.get_card(self.deck, "AS")
        card = got_cards[0]

        self.assertEqual(len(got_cards), 1)
        self.assertEqual(len(left), 51)
        self.assertEqual(card.name, "Ace of Spades")

    def test_get_card_full(self):
        """"""
        left, got_cards = pydealer.tools.get_card(self.deck, "Ace of Spades")
        card = got_cards[0]

        self.assertEqual(len(got_cards), 1)
        self.assertEqual(len(left), 51)
        self.assertEqual(card.name, "Ace of Spades")

    def test_get_card_partial_value(self):
        """"""
        left, got_cards = pydealer.tools.get_card(self.deck, "Ace")

        self.assertEqual(len(got_cards), 4)
        self.assertEqual(len(left), 48)
        for card in got_cards:
            self.assertEqual(card.value, "Ace")

    def test_get_card_partial_suit(self):
        """"""
        left, got_cards = pydealer.tools.get_card(self.deck, "Spades")

        self.assertEqual(len(got_cards), 13)
        self.assertEqual(len(left), 39)
        for card in got_cards:
            self.assertEqual(card.suit, "Spades")

    def test_get_card_limit(self):
        """"""
        left, got_cards = pydealer.tools.get_card(self.deck, "Spades", limit=1)

        self.assertEqual(len(got_cards), 1)
        self.assertEqual(len(left), 51)

    def test_get_list_full(self):
        """"""
        full_list = ["Ace of Spades", "2 of Diamonds", "Queen of Hearts",
            "7 of Clubs"]

        left, got_cards = pydealer.tools.get_list(self.stack, full_list)

        self.get_list_helper(left, got_cards)

    def test_get_list_abbrev(self):
        """"""
        abbrev_list = ["AS", "2D", "QH", "7C"]

        left, got_cards = pydealer.tools.get_list(self.stack, abbrev_list)

        self.get_list_helper(left, got_cards)

    def test_get_list_partial_value(self):
        """"""
        partial_list = ["Ace", "2", "Queen", "7"]

        left, got_cards = pydealer.tools.get_list(self.stack, partial_list)

        self.get_list_helper(left, got_cards)

    def test_get_list_partial_suit(self):
        """"""
        partial_list = ["Spades", "Diamonds", "Hearts", "Clubs"]

        left, got_cards = pydealer.tools.get_list(self.stack, partial_list)

        self.get_list_helper(left, got_cards)

    def test_get_list_mixed(self):
        """"""
        mixed_list = ["AS", "2 of Diamonds", "Hearts", "7"]

        left, got_cards = pydealer.tools.get_list(self.stack, mixed_list)

        self.get_list_helper(left, got_cards)

    def test_get_list_limit(self):
        """"""
        left, got_cards = pydealer.tools.get_list(self.stack, ["Spades"], limit=1)

        self.assertEqual(len(got_cards), 1)


# if __name__ == '__main__':
#     unittest.main()