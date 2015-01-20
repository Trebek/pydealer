import unittest

from pydealer import Deck, Card


class Test(unittest.TestCase):

    def test0010_deck(self):
        'Test deck'
        self.assertEqual(len(Deck()), 52)
        self.assertEqual(len(Deck(jokers=True)), 54)
        self.assertEqual(len(Deck() + Deck()), 104)

        deck = Deck()
        self.assertTrue(deck == Deck())
        self.assertEqual(len(deck.deal()), 1)
        self.assertEqual(len(deck), 51)
        self.assertEqual(len(deck.deal(4)), 4)
        self.assertEqual(len(deck), 47)
        card, = deck.deal()
        self.assertFalse(card in deck)
        self.assertIsInstance(card, Card)
        self.assertEqual(deck.find(str(card)), [])
        deck = Deck()
        card = deck.cards[0]
        self.assertTrue(card in deck)
        del deck[0]
        self.assertFalse(card in deck)
        self.assertEqual(len(deck.deal(53)), 53)
        deck = Deck()
        cards = deck.cards
        self.assertEqual(cards, [x for x in deck])
        deck = Deck()
        self.assertEqual(deck.get('Ace of Spades'), [Card('Ace', 'Spades')])
        deck = Deck()
        terms = ('Ace of Spades', 'Ace of Hearts')
        self.assertEqual(len(deck.find_list(terms)), 2)
        aces = deck.get_list(terms)
        self.assertEqual(aces[0], Card('Ace', 'Spades'))
        self.assertEqual(aces[1], Card('Ace', 'Hearts'))
        deck.set_cards(aces)
        self.assertEqual(len(deck), 2)

    def test0020_card(self):
        'Test card'
        card = Card('Ace', 'Spades')
        self.assertEqual(str(card), 'Ace of Spades')
        self.assertEqual(str(card), card.name)
        self.assertEqual(card.abbrev, 'AS')
        self.assertEqual(card, Card('Ace', 'Spades'))
        self.assertGreater(card, Card('9', 'Spades'))


if __name__ == '__main__':
    unittest.main()
