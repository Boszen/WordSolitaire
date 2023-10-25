import word_helpers

class Tile:
    def __init__(self, letter):
        '''
        All letters are uppercase unless it is lowercase, in which case, it is a
        blank tile.
        '''
        self.isblank = letter.islower()
        self.letter = letter.upper()
        self.value = word_helpers.POINTS(letter)

        if self.isblank:
            self.value = 0

    def draw(self, scrn, pos, rman):
        '''
        '''
        scrn.blit(rman.tiles[self.letter], pos)

class Bonus:
    def __init__(self, b):
        self.b = b

    def draw(self, scrn, pos, rman):
        '''
        '''
        scrn.blit(rman.tiles[self.b], pos)
