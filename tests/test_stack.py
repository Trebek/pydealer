#===============================================================================
# PyDealer - Tests - Stack
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
from pydealer.const import BOTTOM


#===============================================================================
# TestStack Class
#===============================================================================

class TestStack(unittest.TestCase):

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
        self.stack = pydealer.Stack()
        self.full_stack = pydealer.Stack(cards=pydealer.tools.build_cards())
        self.small_stack = pydealer.Stack(cards=self.cards)

    def find_list_helper(self, stack, found):
        """"""
        self.assertEqual(len(found), 4)

        for i, name in enumerate(self.names):
            self.assertEqual(stack[found[i]].name, name)

    def get_list_helper(self, found):
        """"""
        self.assertEqual(len(found), 4)

        for i, name in enumerate(self.names):
            self.assertEqual(found[i].name, name)

    def test_add_top(self):
        """"""
        self.stack.add(self.two_diamonds)
        self.assertIs(self.stack[-1], self.two_diamonds)

    def test_add_bottom(self):
        """"""
        self.stack.add(self.ace_spades, BOTTOM)
        self.assertIs(self.stack[0], self.ace_spades)

    def test_add_plus_eq(self):
        """"""
        self.stack += [self.ace_spades]
        self.assertIs(self.stack[-1], self.ace_spades)

    def test_contains(self):
        """"""
        self.stack.add(self.ace_spades)
        result = self.ace_spades in self.stack
        self.assertTrue(result)

    def test_deal_single(self):
        """"""
        cards = self.full_stack.deal()

        self.assertEqual(len(cards), 1)
        self.assertIsInstance(cards[0], pydealer.Card)

    def test_deal_multiple(self):
        """"""
        cards = self.full_stack.deal(7)

        self.assertEqual(len(cards), 7)
        self.assertIsInstance(cards[0], pydealer.Card)

    def test_del_item(self):
        """"""
        card = self.full_stack[0]
        del self.full_stack[0]
        result = card in self.full_stack

        self.assertFalse(result)

    def test_empty(self):
        """"""
        cards = self.full_stack.empty(True)

        self.assertEqual(len(cards), 52)
        self.assertEqual(len(self.full_stack), 0)

    def test_eq(self):
        """"""
        other_stack = pydealer.Stack(cards=pydealer.tools.build_cards())

        result = self.full_stack == other_stack

        self.assertTrue(result)

    def test_find_abbrev(self):
        """"""
        found = self.full_stack.find("AS")
        i = found[0]

        self.assertEqual(len(found), 1)
        self.assertEqual(self.full_stack[i].name, "Ace of Spades")

    def test_find_full(self):
        """"""
        found = self.full_stack.find("Ace of Spades")
        i = found[0]

        self.assertEqual(len(found), 1)
        self.assertEqual(self.full_stack[i].name, "Ace of Spades")

    def test_find_partial_value(self):
        """"""
        found = self.full_stack.find("Ace")

        self.assertEqual(len(found), 4)
        for i in found:
            self.assertEqual(self.full_stack[i].value, "Ace")

    def test_find_partial_suit(self):
        """"""
        found = self.full_stack.find("Spades")

        self.assertEqual(len(found), 13)
        for i in found:
            self.assertEqual(self.full_stack[i].suit, "Spades")

    def test_find_limit(self):
        """"""
        found = self.full_stack.find("Spades", limit=1)

        self.assertEqual(len(found), 1)

    def test_find_sort(self):
        """"""
        found = self.full_stack.find("Spades", sort=True)

        self.assertEqual(len(found), 13)
        self.assertEqual(self.full_stack[found[0]].value, "2")

    def test_find_list_full(self):
        """"""
        full_list = ["Ace of Spades", "2 of Diamonds", "Queen of Hearts",
            "7 of Clubs"]

        found = self.small_stack.find_list(full_list)

        self.find_list_helper(self.small_stack, found)

    def test_find_list_abbrev(self):
        """"""
        abbrev_list = ["AS", "2D", "QH", "7C"]

        found = self.small_stack.find_list(abbrev_list)

        self.find_list_helper(self.small_stack, found)

    def test_find_list_partial_value(self):
        """"""
        partial_list = ["Ace", "2", "Queen", "7"]

        found = self.small_stack.find_list(partial_list)

        self.find_list_helper(self.small_stack, found)

    def test_find_list_partial_suit(self):
        """"""
        partial_list = ["Spades", "Diamonds", "Hearts", "Clubs"]

        found = self.small_stack.find_list(partial_list)

        self.find_list_helper(self.small_stack, found)

    def test_find_list_mixed(self):
        """"""
        mixed_list = ["AS", "2 of Diamonds", "Hearts", "7"]

        found = self.small_stack.find_list(mixed_list)

        self.find_list_helper(self.small_stack, found)

    def test_find_list_limit(self):
        """"""
        found = self.full_stack.find_list(["Spades"], limit=1)

        self.assertEqual(len(found), 1)

    def test_get_abbrev(self):
        """"""
        found = self.full_stack.get("AS")
        card = found[0]

        self.assertEqual(len(found), 1)
        self.assertEqual(card.name, "Ace of Spades")

    def test_get_full(self):
        """"""
        found = self.full_stack.get("Ace of Spades")
        card = found[0]

        self.assertEqual(len(found), 1)
        self.assertEqual(card.name, "Ace of Spades")

    def test_get_partial_value(self):
        """"""
        found = self.full_stack.get("Ace")

        self.assertEqual(len(found), 4)
        for card in found:
            self.assertEqual(card.value, "Ace")

    def test_get_partial_suit(self):
        """"""
        found = self.full_stack.get("Spades")

        self.assertEqual(len(found), 13)
        for card in found:
            self.assertEqual(card.suit, "Spades")

    def test_get_limit(self):
        """"""
        found = self.full_stack.get("Spades", limit=1)

        self.assertEqual(len(found), 1)

    def test_get_list_full(self):
        """"""
        full_list = ["Ace of Spades", "2 of Diamonds", "Queen of Hearts",
            "7 of Clubs"]

        found = self.small_stack.get_list(full_list)

        self.get_list_helper(found)

    def test_get_list_abbrev(self):
        """"""
        abbrev_list = ["AS", "2D", "QH", "7C"]

        found = self.small_stack.get_list(abbrev_list)

        self.get_list_helper(found)

    def test_get_list_partial_value(self):
        """"""
        partial_list = ["Ace", "2", "Queen", "7"]

        found = self.small_stack.get_list(partial_list)

        self.get_list_helper(found)

    def test_get_list_partial_suit(self):
        """"""
        partial_list = ["Spades", "Diamonds", "Hearts", "Clubs"]

        found = self.small_stack.get_list(partial_list)

        self.get_list_helper(found)

    def test_get_list_mixed(self):
        """"""
        mixed_list = ["AS", "2 of Diamonds", "Hearts", "7"]

        found = self.small_stack.get_list(mixed_list)

        self.get_list_helper(found)

    def test_get_list_limit(self):
        """"""
        found = self.full_stack.get_list(["Spades"], limit=1)

        self.assertEqual(len(found), 1)

    def test_getitem(self):
        """"""
        card = self.full_stack[0]

        self.assertIsInstance(card, pydealer.card.Card)

        card = self.full_stack[-1]

        self.assertIsInstance(card, pydealer.card.Card)

    def test_insert(self):
        """"""
        self.full_stack.insert(self.ace_spades, 1)

        self.assertIs(self.full_stack[1], self.ace_spades)

    def test_insert_list(self):
        """"""
        self.full_stack.insert_list(self.cards, 1)

        stack_slice = self.full_stack[1:5]

        self.assertEqual(stack_slice, self.cards)

    def test_iter(self):
        """"""
        for card in self.full_stack:
            self.assertIsInstance(card, pydealer.card.Card)

    def test_len(self):
        """"""
        result = len(self.full_stack)

        self.assertIs(result, 52)

    def test_ne(self):
        """"""
        result = self.full_stack != self.stack

        self.assertTrue(result)

    def test_open_cards(self):
        """"""
        indices = [0, 1, 2, 3]
        self.stack.open_cards("cards.txt")

        self.find_list_helper(self.stack, indices)

    def test_random_card(self):
        """"""
        card = self.full_stack.random_card()

        self.assertIsInstance(card, pydealer.Card)

    def test_repr(self):
        """"""
        result = repr(self.stack)

        self.assertEquals(result, "Stack(cards=deque([]))")

    def test_reverse(self):
        """"""
        cards_reversed_x = list(self.small_stack.cards)[::-1]

        self.small_stack.reverse()
        cards_reversed_y = list(self.small_stack.cards)

        self.assertEqual(cards_reversed_x, cards_reversed_y)

    def test_save_cards(self):
        """"""
        names = ["Ace Spades\n", "2 Diamonds\n", "Queen Hearts\n", "7 Clubs"]

        self.small_stack.save_cards("cards-save.txt")

        with open("cards-save.txt", "r") as cards_save:
            lines = cards_save.readlines()
            for i, name in enumerate(names):
                self.assertEqual(lines[i], name)

    def test_set_cards(self):
        """"""
        self.stack.set_cards(self.cards)

        self.assertEqual(list(self.stack.cards), self.cards)

    def test_setitem(self):
        """"""
        self.full_stack[0] = self.ace_spades

        self.assertIs(self.full_stack[0], self.ace_spades)

    def test_shuffle(self):
        """"""
        cards_before = list(self.full_stack.cards)
        self.full_stack.shuffle()
        cards_after = list(self.full_stack.cards)

        self.assertNotEqual(cards_before, cards_after)

    def test_size(self):
        """"""
        self.assertEqual(self.full_stack.size, 52)

    def test_sort(self):
        """"""
        ordered = [self.two_diamonds, self.seven_clubs, self.queen_hearts,
                   self.ace_spades]

        self.small_stack.sort()

        self.assertEqual(list(self.small_stack.cards), ordered)

    def test_split(self):
        """"""
        s1, s2 = self.small_stack.split()

        self.assertEqual(list(s1.cards), self.small_stack[0:2])
        self.assertEqual(list(s2.cards), self.small_stack[2::])

    def test_str(self):
        """"""
        result = str(self.full_stack[0])

        self.assertEquals(result, "2 of Diamonds")


# if __name__ == '__main__':
#     unittest.main()
