
EMPTY_SPACE = "."
BOARD_LENGTH = 9
BOARD_LENGTH_SQRT = 3


class Sudoku(object):

    def __init__(self, symbols=None):

        self.clear()

        if symbols is not None:
            self.symbols = symbols

    @property
    def symbols(self):
        """Returns a string of all symbols on the board."""

        all_symbols = []

        for y in range(BOARD_LENGTH):
            for x in range(BOARD_LENGTH):
                all_symbols.append(self.board[y][x])

        return "".join(all_symbols)

    @symbols.setter
    def symbols(self, value):
        """Sets all 81 symbols on the board to the 81 elements of the string, value"""

        for i, symbol in enumerate(value):
            self.board[i // BOARD_LENGTH][i % BOARD_LENGTH] = symbol

    def clear(self):
        """
        Initialises an empty 9x9 Sudoku board.
        Sets all symbols on the board to EMPTY_SPACE.
        """
        self.board = [[EMPTY_SPACE] *
                      BOARD_LENGTH for i in range(BOARD_LENGTH)]

    def solve(self):
        """Backtracking algorithm"""

        find = self.find_empty()
        if not find:
            return True
        else:
            row, col = find

        for i in range(1, 10):
            if self.is_valid(i, (row, col)):
                self.board[row][col] = i
                if self.solve():
                    return True

                self.board[row][col] = EMPTY_SPACE

        return False

    def is_valid(self, value, pos):
        """Checks if an int value is allowed in a given position on the board."""

        value = str(value)
        row, col = pos

        # Check row
        for x in range(BOARD_LENGTH):
            if value in [self.board[row][x] for x in range(BOARD_LENGTH)]:
                return False

        # Check column
        for y in range(BOARD_LENGTH):
            if value in [self.board[y][col] for y in range(BOARD_LENGTH)]:
                return False

        # Check box
        box_x = col // BOARD_LENGTH_SQRT
        box_y = row // BOARD_LENGTH_SQRT

        for y in range(box_y*3, box_y*3 + 3):
            for x in range(box_x * 3, box_x*3 + 3):
                if self.board[y][x] == value:
                    return False

        return True

    def find_empty(self):
        """Returns the position of the next empty space"""

        for row in range(BOARD_LENGTH):
            for col in range(BOARD_LENGTH):
                if self.board[row][col] == EMPTY_SPACE:
                    return (row, col)

        return None

    def __str__(self):
        """
        Returns a string representation of the board with grid-lines to separate the boxes.
        """
        all_rows = []

        for y in range(BOARD_LENGTH):
            row = [self.board[y][x] for x in range(BOARD_LENGTH)]

            row.insert(3, '|')
            row.insert(7, '|')

            all_rows.append(' '.join(map(str, row)))

            if y == 2 or y == 5:
                all_rows.append('------+-------+------')

        return '\n'.join(map(str, all_rows))

    def __repr__(self):
        """Returns a string that is a representation of a SudokuBoard object."""

        return "Sudoku(symbols={0!r})".format(self.symbols)


# b = Sudoku(
#     symbols='73851.962.493.7..5.51.2....3.27.......64.27534..6..21....2...3.....3.64...39.5.2.')

"""
7 3 8 | 5 1 . | 9 6 2
. 4 9 | 3 . 7 | . . 5
. 5 1 | . 2 . | . . .
------+-------+------
3 . 2 | 7 . . | . . .
. . 6 | 4 . 2 | 7 5 3
4 . . | 6 . . | 2 1 .
------+-------+------
. . . | 2 . . | . 3 .
. . . | . 3 . | 6 4 .
. . 3 | 9 . 5 | . 2 .
"""

"""Currently doing some kind of bug where 4 is inserted into (2,5) during solve, even though it should not be possible"""

b = Sudoku(
    symbols='73851496224936718565182....3.27.......64.27534..6..21....2...3.....3.64...39.5.2.')

# b.solve()
print(b)
print()
print(f"4 valid in (2,5): {b.is_valid(4, (2,5))}")
