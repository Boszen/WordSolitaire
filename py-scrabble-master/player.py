import tile
import resman
import move
import pygame

class Player:
    '''
    A representation of the player, complete with current score and hand.
    Should only draw the player's own hand, and not the current move.
    '''
    def __init__(self, pos):
        '''
        Initializes score and hand.
        hand should only have characters (max size 7).
        '''
        self.pos = pos
        self.score = 0
        self.hand = []
        self.currentMove = move.Move()
        self.size = (7 * resman.Tile_Size[0],
                     resman.Tile_Size[1])
        self.rect = pygame.Rect(self.pos, self.size)

    def __contains__(self, pos):
        '''
        Returns true if point is inside player hand rectangle, and false if
        otherwise.
        Uses pygame Rect.collidepoint method to compact code.
        '''
        return self.rect.collidepoint(pos)

    def get_tile_pos(self, pos):
        '''
        Returns the index of the tile, if it exists at position pos.
        Otherwise, return -1. Assumes that the position is already in the player
        hand.
        '''
        # Normalize the position
        pos[0] -= self.pos[0]

        ind = pos[0] // resman.Tile_Size[0]
        if ind < len(self.hand):
            return ind
        else:
            return -1

    def get_tile(self, pos):
        '''
        Returns a single character from the position.
        If the character doesn't exist, raises an exception.
        '''
        ind = self.get_tile_pos(pos)

        if ind == -1:
            raise Exception("error: that isn't a tile")

        t = self.hand[ind]
        return t

    def make_move(self, x, y, letter):
        '''
        Removes tile from hand and places it into active move (and ideally, the
        board).
        '''
        if letter not in self.hand:
            raise Exception("error: cannot move what is not yours")

        self.currentMove.add_move(x, y, letter)

    def takeback_move(self, x, y):
        '''
        Removes tile from active move (placed on board) and replace it back into
        hand.
        '''
        self.hand.append(self.currentMove.remove_move(x, y))

    def deck_draw(self, deck, n):
        '''
        Draws n tiles from deck
        '''
        self.hand.extend(deck.take(n))

    def deck_exchange(self, deck, l):
        '''
        Exchanges tiles in hand (list l) with random tiles in deck.
        First checks to see that the list is a subset of hand.
        '''
        if not all(map(lambda i: i in self.hand, l)):
            raise Exception("error: cannot exchange non-existant tiles")

        deck.place(l)

        for i in l:
            self.hand.remove(i)

    def draw(self, scrn, rman):
        '''
        Draws player's hand
        '''
        for i in range(len(self.hand)):
            scrn.blit(rman.tiles[self.hand[i]],
                      (self.pos[0] + resman.Tile_Size[0] * i,
                       self.pos[1]))
