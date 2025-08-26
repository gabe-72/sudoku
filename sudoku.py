import numpy as np

class Sudoku:
    # Binary encoding of the numbers
    # this allows us to easily compute whether a row has duplicates or not by simply adding up the rows
    # as long as the number of elements is equal to the number of unique numbers
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

    def _is_valid(self) -> bool:
        """
        Checks for validity of the sudoku grid.

        Validity checks:
        - dimension check for the grid
        - each row has the numbers 1-9
        - each column has the numbers 1-9
        - each subgrid has the numbers 1-9

        Returns:
            bool: True if valid, False otherwise
        """
        ones = np.ones((self._GRID_LENGTH, 1), dtype=np.uint16)

        # Check dimensions
        if self.SUDOKU_GRID.shape != self._GRID_SHAPE:
            # Should never happen
            raise Exception(f'Sudoku Grid shape invalid {self.SUDOKU_GRID.shape}')

        # Check rows, see if every row contains all the numbers
        # equivalent to summing the rows, but for a standard grid (9x9), this is faster
        row_sum = self.SUDOKU_GRID @ ones
        if not np.all(row_sum == self._VALID_SUM):
            return False

        # Check columns, see if every column contains all the numbers
        col_sum = self.SUDOKU_GRID.T @ ones
        if not np.all(col_sum == self._VALID_SUM):
            return False

        # Check the subgrids
        # Reshape the grid into (subgrid rows, num of rows in each subgrid, subgrid cols, num of cols in each subgrid)
        # indicies 0 -> subgrid row; 1 -> the row number in the subgrid; 2 -> subgrid col; 3 -> the col number in the subgrid
        reshaped_grid = self.SUDOKU_GRID.reshape(
            self._GRID_LENGTH // self._SUBGRID_LENGTH, self._SUBGRID_LENGTH,
            self._GRID_LENGTH // self._SUBGRID_LENGTH, self._SUBGRID_LENGTH
        )

        # Sum the rows in the subgrids and the columns in the subgrid
        subgrid_sums = reshaped_grid.sum(axis=(1, 3))
        print(subgrid_sums)

        if not np.all(subgrid_sums == self._VALID_SUM):
            return False

        # All checks passed
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
    print(sudoku._is_valid())
