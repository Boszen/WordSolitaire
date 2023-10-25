import state
import resman
import board
import player
import deck
import pygame
import word_helpers as wh

class PlayState(state.State):
    '''
    The play state, the state which is shown while the user is
    playing the game, which is, all the time in this prototype.

    Loads everything necessary and starts the game.
    '''
    def __init__(self, rman, ai = False):
        self.ai = ai
        self.rman = rman
        self.board = board.ScrabbleBoard((0, 0), self.rman)
        self.p1 = player.Player((0, 750))
        self.p2 = player.Player((0, 750))
        self.wd = wh.WordDictionary('sowpods.txt')
        self.deck = deck.Deck()
        self.turn = "1"             # Player 1 always goes first
        self.selectedTile = None    # Selected tile should be a letter only

        # Place players into dictionary for less if-statements
        self.ps = {"1": self.p1, "2": self.p2}

        # First, draw 7 tiles
        self.p1.deck_draw(self.deck, 7)
        self.p2.deck_draw(self.deck, 7)

    def handle(self, evt):
        '''
        Handles all events passed into the state.
        '''
        if evt.type == pygame.MOUSEBUTTONUP:
            pos = list(pygame.mouse.get_pos())
            if pos in self.board:
                if self.selectedTile is None:
                    # Removes selected tile from board, and thus, from moveset
                    self.handle_board_removal(pos)
                else:
                    # Places selected tile into moveset, and thus, places tile
                    # onto board
                    self.handle_board_place(pos)
            elif pos in self.ps[self.turn]:
                if self.selectedTile is None:
                    # Select tile, and remove from correct hand
                    self.handle_hand_select(pos)
                else:
                    # Replaces removed tile from hand
                    self.handle_hand_replace(pos)

    def handle_board_removal(self, pos):
        '''
        Handles the removal of tile. If the tile isn't in the current moveset,
        don't remove anything. Because that is cheating. Cheating is not
        tolerated.
        '''
        ind = self.board.get_tile_pos(pos)

        try:
            l = self.ps[self.turn].currentMove.remove_move(*ind)
            self.selectedTile = l
        except:
            return

    def handle_board_place(self, pos):
        '''
        Handles the placing of the selected tile onto the board. Assumes that
        there is already a selected tile.
        '''
        ind = self.board.get_tile_pos(pos)
        if self.board.tiles[ind[0]][ind[1]] is None:
            try:
                # Stops people from trying to place tiles on a non-empty tile
                # that is in moveset (it throws a nasty little error when it
                # does).
                self.ps[self.turn].currentMove.add_move(ind[0], ind[1],
                                                        self.selectedTile)
                self.selectedTile = None
            except:
                pass

    def handle_hand_replace(self, pos):
        '''
        Handles the replacing of selected tile into hand.
        '''
        # Gets the tile index, if any
        ind = self.ps[self.turn].get_tile_pos(pos)

        # Places tile into hand
        if ind == -1:
            self.ps[self.turn].hand.append(self.selectedTile)
        else:
            self.ps[self.turn].hand.insert(ind, self.selectedTile)

        # Removes selected tile
        self.selectedTile = None

    def handle_hand_select(self, pos):
        '''
        Handles the tile selection and removal (from the corresponding hand, of
        course).
        '''
        # Grab tile from hand and place into tile selection
        try:
            self.selectedTile = self.ps[self.turn].get_tile(pos)
        except:
            return

        # Removes tile from hand
        self.ps[self.turn].hand.remove(self.selectedTile)

    def draw(self, scrn):
        '''
        Draws the state onto the screen scrn.
        '''
        self.board.draw(scrn, self.ps[self.turn].currentMove)

        if self.turn == "1":
            self.p1.draw(scrn, self.rman)
        else:
            self.p2.draw(scrn, self.rman)

        if self.selectedTile is not None:
            # Tile is selected and should hang onto the mouse
            x, y = pygame.mouse.get_pos()
            scrn.blit(self.rman.tiles[self.selectedTile],
                      (x - resman.Tile_Size[0] / 2,
                       y - resman.Tile_Size[1] / 2))

    def update(self, delta):
        '''
        Updates the state as a whole.
        '''
        pass
