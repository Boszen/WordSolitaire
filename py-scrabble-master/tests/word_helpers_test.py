import unittest
import os
import sys
sys.path.insert(0, os.path.abspath('.'))
from word_helpers import *


class WordScoreTest(unittest.TestCase):
    def test(self):
        self.assertEqual(wordScore('A'), 1)
        self.assertEqual(wordScore('SQUEEZE'), 25)

        # Lowercase testing
        self.assertEqual(wordScore('dab'), 0)

class WordDictionaryTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.wd = WordDictionary('sowpods.txt')

    def testInit(self):
        self.assertEqual(self.wd.words[0], 'AA')
        self.assertEqual(self.wd.words[-1], 'ZZZS')

    def testValidity(self):
        self.assertTrue(self.wd.isValid('ZYZZYVA'))
        self.assertTrue(self.wd.isValid('ZZZS'))
        self.assertTrue(self.wd.isValid('AA'))
        self.assertTrue(self.wd.isValid('QUETZAL'))
        self.assertTrue(self.wd.isValid('KNOCKING'))

        # Lowercase testing
        self.assertTrue(self.wd.isValid('knocking'))

    def testInvalidity(self):
        self.assertFalse(self.wd.isValid('A'))
        self.assertFalse(self.wd.isValid('Z'))
        self.assertFalse(self.wd.isValid('ZZZZ'))
        self.assertFalse(self.wd.isValid('ALAKAZAM'))
        self.assertFalse(self.wd.isValid('BEHIVE'))

        # Lowercase testing
        self.assertFalse(self.wd.isValid('sticktack'))

        # Idiot testing
        self.assertFalse(self.wd.isValid(''))

if __name__ == '__main__':
    unittest.main()
