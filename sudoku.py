import numpy as np

class Sudoku:
    # Binary encoding of the numbers
    _1 = 0b000000001
    _2 = 0b000000010
    _3 = 0b000000100
    _4 = 0b000001000
    _5 = 0b000010000
    _6 = 0b000100000
    _7 = 0b001000000
    _8 = 0b010000000
    _9 = 0b100000000

    # List of encoded numbers used for easy conversions
    _NUM = [None, _1, _2, _3, _4, _5, _6, _7, _8, _9]
    # _NUM = [None] + [(1 << i) for i in range(1, 10)]

    # Valid summation for a row/column/sub square
    _VALID_SUM = sum(_NUM[1:])

    # Sudoku dimensions (has to be a square, at least for now)
    _GRID_SHAPE = (9, 9)
    _GRID_LENGTH = _GRID_SHAPE[0]

    _SUBGRID_SHAPE = (3, 3)
    _SUBGRID_LENGTH = _SUBGRID_SHAPE[0]

    # Base Sudoku grid (is valid)
    SUDOKU_GRID = np.array([
        [_1, _2, _3, _4, _5, _6, _7, _8, _9],
        [_7, _8, _9, _1, _2, _3, _4, _5, _6],
        [_4, _5, _6, _7, _8, _9, _1, _2, _3],
        [_9, _1, _2, _3, _4, _5, _6, _7, _8],
        [_6, _7, _8, _9, _1, _2, _3, _4, _5],
        [_3, _4, _5, _6, _7, _8, _9, _1, _2],
        [_8, _9, _1, _2, _3, _4, _5, _6, _7],
        [_5, _6, _7, _8, _9, _1, _2, _3, _4],
        [_2, _3, _4, _5, _6, _7, _8, _9, _1],
    ], dtype=np.uint16)

    def __init__(self, shuffled: bool = True):
        # Shuffle the grid if required
        if (shuffled):
            self.shuffle()

    def is_valid(self) -> bool:
        """
        Checks for validity of the sudoku grid.

        Returns:
            bool: True if valid, False otherwise
        """
        pass

    def shuffle(self) -> None:
        """
        Shuffles the grid in a way that it is still valid.
        Note: validity is checked after shuffle.

        How its shuffled:
        - every 3 sets of rows can be shuffled
        - every 3 sets of cols can be shuffled
        """
        pass

if __name__ == '__main__':
    sudoku = Sudoku(False)

    print(sudoku.SUDOKU_GRID)
