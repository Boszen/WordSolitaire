import unittest
import os
import sys
sys.path.insert(0, os.path.abspath('.'))
from board import *
from move import *
from word_helpers import WordDictionary

class ScrabbleBoardTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.wd = WordDictionary('sowpods.txt')

    def testGetScore(self):
        b = ScrabbleBoard((0,0), None)
        ms = Move()

        # Idiot testing
        self.assertEqual(b.get_score(ms), 0)

        '''
        # Test first move in middle
        ms.m = [(6, 7, 'B'),
                (7, 7, 'A'),
                (8, 7, 'T')]
        self.assertEqual(b.get_score(ms), 10)
        b.execute(ms)

        # Test second move
        ms.m = [(6, 8, 'Y'),
                (7, 8, 'E'),
                (8, 8, 'A')]
        self.assertEqual(b.get_score(ms), 27)

        # Test move with blanks
        ms.m[1] = (7, 8, 'e')
        self.assertEqual(b.get_score(ms), 25)
        '''

        # Test combo x9
        ms.m = [(0, 0, 'Q'),
                (1, 0, 'U'),
                (3, 0, 'T'),
                (4, 0, 'Z'),
                (5, 0, 'A'),
                (6, 0, 'L'),
                (7, 0, 'S')]
        b.tiles[2][0] = 'E'
        self.assertEqual(b.get_score(ms), 293)

    def testValidate(self):
        b = ScrabbleBoard((0,0), None)
        ms, ex, ps = Move(), Move(), Move()
        ex.t, ps.t = 'E', 'P'

        # Idiot testing (nothing to move is invalid)
        self.assertFalse(b.validate(ms, self.wd))
        self.assertFalse(b.validate(ex, self.wd))
        self.assertTrue(b.validate(ps, self.wd))

        # Test of first move with valid word
        ms.m = [(6, 7, 'B'),
                (7, 7, 'A'),
                (8, 7, 'T')]
        self.assertTrue(b.validate(ms, self.wd))

        # Test of first move with invalid word
        ms.m = [(6, 7, 'Z'),
                (7, 7, 'A'),
                (8, 7, 'T')]
        self.assertFalse(b.validate(ms, self.wd))

        # Test invalid move with spaced-out moves
        ms.m = [(6, 7, 'Z'),
                (8, 7, 'A')]
        self.assertFalse(b.validate(ms, self.wd))

    def testFindConnectedWords(self):
        b = ScrabbleBoard((0,0), None)
        validms = Move()

        # Test with a standard word
        validms.m = [(7, 6, 'A'),
                     (7, 7, 'B'),
                     (7, 8, 'A')]
        validms_answer = [((7, 6), 'ABA', (7, 8))]
        self.assertEqual(b.find_connected_words(validms),
                         validms_answer)

        # Test with actual things on the board
        validms_answer = [((7, 6), 'ABA', (7, 8)),
                          ((7, 6), 'AA',  (8, 6)),
                          ((7, 7), 'BA',  (8, 7))]
        b.tiles[8][6] = 'A'
        b.tiles[8][7] = 'A'
        self.assertSetEqual(set(b.find_connected_words(validms)),
                            set(validms_answer))

        # Test checking overbite
        b.tiles[7][10] = 'A'
        b.tiles[5][6] = 'A'
        self.assertSetEqual(set(b.find_connected_words(validms)),
                            set(validms_answer))

        # Test for checking letters inserted between
        validms.m = [(6, 6, 'A'),
                     (8, 6, 'A')]
        validms_answer = [((6, 6), 'ABA', (8, 6))]
        b.tiles[8][6] = None
        b.tiles[8][7] = None
        b.tiles[7][10] = None
        b.tiles[5][6] = None
        b.tiles[7][6] = 'B'
        self.assertEqual(b.find_connected_words(validms),
                         validms_answer)

