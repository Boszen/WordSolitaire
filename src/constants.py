WIDTH = 1280
HEIGHT = 720

BOARD_SIZE = 7
CELL_SIZE = 70

#Board + gap SIZE = 60*7 + 20*6 = 420 + 120 = 640 -> 640*640

RANK_EASY = "./rankEasy.lst"
RANK_MEDIUM = "./rankMedium.lst"
RANK_HARD = "./rankHard.lst"

WORDS = []

with open('./words.txt', 'r') as file:
    for line in file:
        word = line.strip()
        if 3 <= len(word) <= 7:
            # Add the word to the list
            WORDS.append(word)

ALPHABETS = [
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z'
]

ALPHABET_SCORE = {
    'a': 1,
    'b': 3,
    'c': 3,
    'd': 2,
    'e': 1,
    'f': 4,
    'g': 2,
    'h': 1,
    'i': 1,
    'j': 8,
    'k': 5,
    'l': 1,
    'm': 3,
    'n': 1,
    'o': 1,
    'p': 3,
    'q': 10,
    'r': 1,
    's': 1,
    't': 1,
    'u': 1,
    'v': 4,
    'w': 4,
    'x': 8,
    'y': 4,
    'z': 10
}