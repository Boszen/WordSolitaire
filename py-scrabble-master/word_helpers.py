# Letter point value system
# The spaces represent the blanks
POINTS = {"A": 1, "C": 3, "B": 3, "E": 1, "D": 2, "G": 2,
          "F": 4, "I": 1, "H": 4, "K": 5, "J": 8, "M": 3,
          "L": 1, "O": 1, "N": 1, "Q": 10, "P": 3, "S": 1,
          "R": 1, "U": 1, "T": 1, "W": 4, "V": 4, "Y": 4,
          "X": 8, "Z": 10, " ": 0}
# Letter distribution
# The spaces represent the blanks
DISTRIBUTION = {" ": 2, "E": 12, "A": 9, "I": 9, "O": 8, "N": 6, "R": 6, "T": 6,
                "L": 4, "S": 4, "U": 4, "D": 4, "G": 3, "B": 2, "C": 2, "M": 2,
                "P": 2, "F": 2, "H": 2, "V": 2, "W": 2, "Y": 2, "K": 1, "J": 1,
                "X": 1, "Q": 1, "Z": 1}
# Bingo bonus
# The bonus score you get when you get bingo (all 7 letters used)
BINGO_BONUS = 50

class WordDictionary:
    def __init__(self, fn):
        self.words = []
        with open(fn) as f:
            for line in f.readlines():
                self.words.append(line.rstrip().upper())

    def isValid(self, word):
        '''
        isValid(word)
        Uses a binary search to check if the word exists in the
        array.
        '''
        if word == '': return False

        word = word.upper()
        first, last = 0, len(self.words)
        while first != last:
            mid = (first + last) // 2
            if word == self.words[mid]:
                return True
            elif word > self.words[mid]:
                first = mid + 1
            elif word < self.words[mid]:
                last = mid
        return False

def letterScore(letter):
    if letter.islower():
        return 0
    else:
        return POINTS[letter]

def wordScore(word):
    return sum(map(letterScore, word))
