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
        ones = np.ones((self._GRID_LENGTH, 1), dtype=np.uint16)

        # Check dimensions
        if self.SUDOKU_GRID.shape != self._GRID_SHAPE:
            # Should never happen
            raise Exception(f'Sudoku Grid shape invalid {self.SUDOKU_GRID.shape}')

        # Check rows
        row_sum = self.SUDOKU_GRID @ ones
        if not np.all(row_sum == self._VALID_SUM):
            return False

        # Check columns
        col_sum = self.SUDOKU_GRID.T @ ones
        if not np.all(col_sum == self._VALID_SUM):
            return False

        # Check each sub square
        ones = ones.reshape(self._SUBGRID_SHAPE)

        # Loop the rows, stepping by the length of the subgrid
        for row_start in range(0, self._GRID_LENGTH, self._SUBGRID_LENGTH):
            # Compute the end of the subgrid row
            row_end = row_start + self._SUBGRID_LENGTH

            # Loop through the columns now
            for col_start in range(0, self._GRID_LENGTH, self._SUBGRID_LENGTH):
                # Compute the end of the subgrid column
                col_end = col_start + self._SUBGRID_LENGTH

                # Get a view of the subgrid
                subgrid = self.SUDOKU_GRID[row_start:row_end, col_start:col_end]

                # Check if the subgrid contains all the numbers
                if np.vdot(subgrid, ones) != self._VALID_SUM:
                    return False

        return True

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
