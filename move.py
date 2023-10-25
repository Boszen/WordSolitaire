class Move:
    '''
    A move is an array of formatted tuples:
        (posx, posy, letter)

    This is to simulate the (mostly) multiple tile placings you see in all
    scrabble play. Of course, these moves are constructed on a tile-by-tile
    basis.

    The tuples only include the ones placed by the player, and not the ones that
    are on the board already.
    '''
    def __init__(self):
        self.m = []

        # The type of move can be one of 3 characters:
        # 'M' -> Your standard move (placing tiles on board)
        # 'E' -> Exchange (the placed tiles on board get swapped with others in
        #        the deck
        # 'P' -> Pass (all placed tiles return to hand and the next turn
        #        happens)
        # Defaults to 'M'
        self.t = 'M'

        # If the move is chained together with other tiles on the board, it will
        # be true, otherwise, if nothing is adjacent to it, it will be false.
        self.is_chain = False

        self.vert, self.horz = None, None

    def get_item(self, x, y):
        '''
        Finds the move with coordinates equal to (x, y). Raises ValueError if
        move doesn't exist.
        '''
        for i, j, l in self.m:
            if i == x and j == y:
                return (i, j, l)
        raise ValueError('invalid indices (%d, %d)' % (x, y))

    def add_move(self, x, y, letter):
        '''
        Appends the entire thing onto move array. Checks for letters that are in
        the same position.
        '''
        for i, j, l in self.m:
            if i == x and j == y:
                raise Exception("error: attempt to place letter in same position")

        self.m.append((x, y, letter))

    def remove_move(self, x, y):
        '''
        Returns the removed letter
        '''
        rem = None
        for i, j, l in self.m:
            if i == x and j == y:
                # A match!
                rem = (i, j, l)

        if rem is None:
            raise Exception("error: letter doesn't exist and cannot be removed")

        self.m.remove(rem)
        return rem[2]

    def validate(self, tiles):
        '''
        Checks to see if the move made by the player is valid.
        Only checks tile placement (vertical or horizontal), and not the words
        itself.

        Returns true if the move is valid in said direction, and false
        otherwise.
        '''
        print(self.validate_continuity(tiles))
        return (self.validate_vertical() or self.validate_horizontal()) and\
            self.validate_continuity(tiles)

    def _validate_directional_continuity(self, tiles, i):
        '''
        Gets the endpoints of the moveset and checks to see if there is a path
        spanning between tem, starting from an endpoint.

        Note that i can only be either 1 or 0 - anything other than that, and
        this function will work unexpectedly.

        Returns true if there is a route between the 2 endpoints, and false
        otherwise.
        '''
        akey = lambda m: m[i]
        y = self.m[0][int(not bool(i))]
        left, right = min(self.m, key = akey), max(self.m, key = akey)
        print(left, right)

        for x in range(left[i], right[i]):
            a, b = x, y
            if i == 1:
                b, a = x, y
            if tiles[a][b] is None:
                try:
                    self.get_item(a, b)
                except:
                    return False

        return True


    def validate_continuity(self, tiles):
        '''
        Checks for continuity errors (i.e. moves with gaps in between).

        Takes the endpoints of the moveset (leftmost/rightmost or
        uppermost/lowermost), and checks to see if there is a path spanning
        between them, starting from 1 endpoint. If there is, the move is joint
        and continuous. If there isn't, the move is disjoint and stupid.

        Returns true if there is continuity, and false otherwise.
        '''
        # The default 1-move moveset should always be continuous
        if len(self.m) == 1: return True

        if self.horz:
            return self._validate_directional_continuity(tiles, 0)
        elif self.vert:
            return self._validate_directional_continuity(tiles, 1)
        else:
            # This shouldn't happen unless it is called from the outside before
            # everything initializes
            return False

    def _validate_helper(self, i):
        '''
        Checks to see if the mvoe made by the player is in an i direction line.

        Returns true if it is, and false otherwise.
        '''
        if len(self.m) <= 1: return True

        s = self.m[0][i]
        for m in self.m:
            if m[i] != s:
                return False
        return True

    def validate_horizontal(self):
        '''
        Checks to see if the move made by the player is in a horizontal line (y
        coordinates the same).

        Returns true if it is, and false otherwise.
        '''
        self.horz = self._validate_helper(1)
        return self.horz

    def validate_vertical(self):
        '''
        Checks to see if the move made by the player is in a vertical line (x
        coordinates the same).

        Returns true if it is, and false otherwise.
        '''
        self.vert = self._validate_helper(0)
        return self.vert
