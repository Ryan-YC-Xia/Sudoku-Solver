from Entry import Entry


class Invalid_Board(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class SB:
    def __init__(self, board):
        self.board_dict = {}
        for i in range(9):
            for j in range(9):
                e = Entry(board[i][j])
                self.board_dict[(i, j)] = e
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    res = self.enforce((i, j))
                    if res == False:
                        raise Invalid_Board(0)

    # Reduce the range of board entries by applying rules of Sudoku
    # Return False if doing so cause the board to be invalid.
    def enforce(self, loc):
        v = self.board_dict[loc].value
        relatives = self.get_relative_set(loc)
        for relative in relatives:
            e = self.board_dict[relative]
            e.eliminate_val(v)
            if e.get_liberty() == 0:
                return False
        return True

    # Return a set of locations exclusive by rules of Sudoku with loc
    def get_relative_set(self, loc):
        x = loc[0]
        xr = (x//3)*3
        y = loc[1]
        yr = (y//3)*3
        r_set = set()
        for i in range(3):
            for j in range(3):
                r_set.add((xr+i, yr+j))
        for i in range(9):
            r_set.add((i, y))
        for j in range(9):
            r_set.add((x, j))
        r_set.discard(loc)
        return r_set

    # Rerurn the location with the least liberty (i.e., most constraints)
    def get_llp(self):
        llp = None
        lib = 10
        for loc, entry in self.board_dict.items():
            if entry.value == '.' and entry.get_liberty() < lib:
                llp = loc
                lib = entry.get_liberty()
        return llp

    def loc_get_range(self, loc):
        return self.board_dict[loc].range

    # Must make sure v is within range of loc entry
    def loc_set_val(self, loc, v):
        self.board_dict[loc].set_val(v)
        return self.enforce(loc)

    # Return true if board is solved
    def check_solved(self):
        return self.get_llp() is None

    # Print out the current Sudoku board
    def print_b(self):
        board = [[0 for i in range(9)] for j in range(9)]
        for key in self.board_dict.keys():
            board[key[0]][key[1]] = self.board_dict[key].value
        for i in range(9):
            for j in range(9):
                print(board[i][j], end='')
            print()
