#===============================================================================
# PyDealer - Card Class
#-------------------------------------------------------------------------------
# Version: 1.4.0
# Updated: 03-08-2014
# Author: Alex Crawford
# License: MIT
#===============================================================================

"""
This module contains the Card class, used for creating Card instances. Each
Card instance represents a single playing card, of a given face and suit.

"""

#===============================================================================
# Imports
#===============================================================================

from pydealer.const import DEFAULT_RANKS


#===============================================================================
# Card Class
#===============================================================================

class Card(object):
    """
    The Card class, each instance representing a single playing card.

    :arg str face:
        The card face.
    :arg str suit:
        The card suit.

    """
    def __init__(self, face, suit):
        """
        Card constructor method.

        :arg str face:
            The card face.
        :arg str suit:
            The card suit.

        """
        self.face = face
        self.suit = str(suit).capitalize()
        self.abbrev = card_abbrev(face, suit)
        self.name = card_name(face, suit)

    def __eq__(self, other):
        """
        Allows for Card face/suit equality comparisons.

        :arg Card other:
            The other card to compare to.

        :returns:
            ``True`` or ``False``.

        """
        return (
            isinstance(other, Card) and self.face == other.face and
            self.suit == other.suit
        )

    def __ne__(self, other):
        """
        Allows for Card face/suit equality comparisons.

        :arg Card other:
            The other card to compare to.

        :returns:
            ``True`` or ``False``.

        """
        return (
            isinstance(other, Card) and self.face != other.face and
            self.suit != other.suit
        )

    def __ge__(self, other):
        """
        Allows for Card ranking comparisons. Uses DEFAULT_RANKS for comparisons.

        :arg Card other:
            The other card to compare to.

        :returns:
            ``True`` or ``False``.

        """
        if isinstance(other, Card):
            return (
                DEFAULT_RANKS["faces"][self.face] >
                DEFAULT_RANKS["faces"][other.face] or
                (
                    DEFAULT_RANKS["faces"][self.face] >=
                    DEFAULT_RANKS["faces"][other.face] and
                    DEFAULT_RANKS["suits"][self.suit] >=
                    DEFAULT_RANKS["suits"][other.suit]
                )
            )
        else:
            return False

    def __gt__(self, other):
        """
        Allows for Card ranking comparisons. Uses DEFAULT_RANKS for comparisons.

        :arg Card other:
            The other card to compare to.

        :returns:
            ``True`` or ``False``.

        """
        if isinstance(other, Card):
            return (
                DEFAULT_RANKS["faces"][self.face] >
                DEFAULT_RANKS["faces"][other.face] or
                (
                    DEFAULT_RANKS["faces"][self.face] >=
                    DEFAULT_RANKS["faces"][other.face] and
                    DEFAULT_RANKS["suits"][self.suit] >
                    DEFAULT_RANKS["suits"][other.suit]
                )
            )
        else:
            return False

    def __hash__(self):
        """
        Returns the hash value of the ``Card`` instance.

        :returns:
            A unique number, or hash for the Card.

        """
        return hash((self.face, self.suit))

    def __repr__(self):
        """
        Returns a string representation of the ``Card`` instance.

        :returns:
            A string representation of the Card instance.

        """
        return "Card(face=%r, suit=%r)" % (self.face, self.suit)

    def __str__(self):
        """
        Returns the full name of the ``Card`` instance.

        :returns:
            The card name.

        """
        return "%s" % (self.name)

    def eq(self, other, ranks=None):
        """
        Compares the card against another card, ``other``, and checks whether
        the card is equal to ``other``, based on the given rank dict.

        :arg Card other:
            The second Card to compare.
        :arg dict ranks:
            The ranks to refer to for comparisons.

        :returns:
            ``True`` or ``False``.

        """
        ranks = ranks or DEFAULT_RANKS
        if isinstance(other, Card):
            if ranks.get("suits"):
                return (
                    ranks["faces"][self.face] ==
                    ranks["faces"][other.face] and
                    ranks["suits"][self.suit] ==
                    ranks["suits"][other.suit]
                )
            else:
                return ranks[self.face] == ranks[other.face]
        else:
            return False

    def ge(self, other, ranks=None):
        """
        Compares the card against another card, ``other``, and checks whether
        the card is greater than or equal to ``other``, based on the given rank
        dict.

        :arg Card other:
            The second Card to compare.
        :arg dict ranks:
            The ranks to refer to for comparisons.

        :returns:
            ``True`` or ``False``.

        """
        ranks = ranks or DEFAULT_RANKS
        if isinstance(other, Card):
            if ranks.get("suits"):
                return (
                    ranks["faces"][self.face] >
                    ranks["faces"][other.face] or
                    (
                        ranks["faces"][self.face] >=
                        ranks["faces"][other.face] and
                        ranks["suits"][self.suit] >=
                        ranks["suits"][other.suit]
                    )
                )
            else:
                return ranks[self.face] >= ranks[other.face]
        else:
            return False

    def gt(self, other, ranks=None):
        """
        Compares the card against another card, ``other``, and checks whether
        the card is greater than ``other``, based on the given rank dict.

        :arg Card other:
            The second Card to compare.
        :arg dict ranks:
            The ranks to refer to for comparisons.

        :returns:
            ``True`` or ``False``.

        """
        ranks = ranks or DEFAULT_RANKS
        if isinstance(other, Card):
            if ranks.get("suits"):
                return (
                    ranks["faces"][self.face] >
                    ranks["faces"][other.face] or
                    (
                        ranks["faces"][self.face] >=
                        ranks["faces"][other.face] and
                        ranks["suits"][self.suit] >
                        ranks["suits"][other.suit]
                    )
                )
            else:
                return ranks[self.face] > ranks[other.face]
        else:
            return False

    def le(self, other, ranks=None):
        """
        Compares the card against another card, ``other``, and checks whether
        the card is less than or equal to ``other``, based on the given rank
        dict.

        :arg Card other:
            The second Card to compare.
        :arg dict ranks:
            The ranks to refer to for comparisons.

        :returns:
            ``True`` or ``False``.

        """
        ranks = ranks or DEFAULT_RANKS
        if isinstance(other, Card):
            if ranks.get("suits"):
                return (
                    ranks["faces"][self.face] <=
                    ranks["faces"][other.face] or
                    (
                        ranks["faces"][self.face] <=
                        ranks["faces"][other.face] and
                        ranks["suits"][self.suit] <=
                        ranks["suits"][other.suit]
                    )
                )
            else:
                return ranks[self.face] <= ranks[other.face]
        else:
            return False

    def lt(self, other, ranks=None):
        """
        Compares the card against another card, ``other``, and checks whether
        the card is less than ``other``, based on the given rank dict.

        :arg Card other:
            The second Card to compare.
        :arg dict ranks:
            The ranks to refer to for comparisons.

        :returns:
            ``True`` or ``False``.

        """
        ranks = ranks or DEFAULT_RANKS
        if isinstance(other, Card):
            if ranks.get("suits"):
                return (
                    ranks["faces"][self.face] <
                    ranks["faces"][other.face] or
                    (
                        ranks["faces"][self.face] <=
                        ranks["faces"][other.face] and
                        ranks["suits"][self.suit] <
                        ranks["suits"][other.suit]
                    )
                )
            else:
                return ranks[self.face] < ranks[other.face]
        else:
            return False

    def ne(self, other, ranks=None):
        """
        Compares the card against another card, ``other``, and checks whether
        the card is not equal to ``other``, based on the given rank dict.

        :arg Card other:
            The second Card to compare.
        :arg dict ranks:
            The ranks to refer to for comparisons.

        :returns:
            ``True`` or ``False``.

        """
        ranks = ranks or DEFAULT_RANKS
        if isinstance(other, Card):
            if ranks.get("suits"):
                return (
                    ranks["faces"][self.face] !=
                    ranks["faces"][other.face] or
                    ranks["suits"][self.suit] !=
                    ranks["suits"][other.suit]
                )
            else:
                return ranks[self.face] != ranks[other.face]
        else:
            return False


#===============================================================================
# Helper Functions
#===============================================================================

def card_abbrev(face, suit):
    """
    Constructs an abbreviation for the card, using the given
    face, and suit.

    :arg str face:
        The face to use.
    :arg str suit:
        The suit to use.

    :returns:
        A newly constructed abbreviation, using the given face
        & suit

    """
    if face is "Joker":
        return "JKR"
    elif face is "10":
        return "10%s" % (suit[0])
    else:
        return "%s%s" % (face[0], suit[0])


def card_name(face, suit):
    """
    Constructs a name for the card, using the given face,
    and suit.

    :arg str face:
        The face to use.
    :arg str suit:
        The suit to use.

    :returns:
        A newly constructed name, using the given face & suit.

    """
    if face is "Joker":
        return "Joker"
    else:
        return "%s of %s" % (face, suit)