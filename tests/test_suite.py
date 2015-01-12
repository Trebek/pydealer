#===============================================================================
# PyDealer - Tests - Test Suite
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

from test_card import TestCard
from test_deck import TestDeck
from test_stack import TestStack
from test_tools import TestTools


#===============================================================================
# Tests List
#===============================================================================

TESTS = [TestCard, TestStack, TestDeck, TestTools]


#===============================================================================
# Main
#===============================================================================

def main():
    """"""
    suite = unittest.TestSuite()
    runner = unittest.TextTestRunner()
    for test in TESTS:
        suite.addTest(unittest.makeSuite(test))
    runner.run(suite)


if __name__ == '__main__':
   main()