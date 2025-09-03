import numpy as np

from sudokuz import sudoku

_1 = sudoku.Sudoku._1
_2 = sudoku.Sudoku._2
_3 = sudoku.Sudoku._3
_4 = sudoku.Sudoku._4
_5 = sudoku.Sudoku._5
_6 = sudoku.Sudoku._6
_7 = sudoku.Sudoku._7
_8 = sudoku.Sudoku._8
_9 = sudoku.Sudoku._9


def test_base_game_validity():
    """Test if the base game board is valid or not"""
    game = sudoku.Sudoku(debug=False)
    assert game._is_valid()


def test_invalid_row():
    """Test the validity of the board with an invalid row"""
    game = sudoku.Sudoku(debug=False)

    # Set the grid to have two invalid rows
    game.SUDOKU_GRID = np.array(
        [
            [_1, _2, _3, _1, _5, _6, _7, _8, _9],  # invalid row at col 3 (0-index)
            [_7, _8, _9, _4, _2, _3, _4, _5, _6],  # invalid row at col 6 (0-index)
            [_4, _5, _6, _7, _8, _9, _1, _2, _3],
            [_9, _1, _2, _3, _4, _5, _6, _7, _8],
            [_6, _7, _8, _9, _1, _2, _3, _4, _5],
            [_3, _4, _5, _6, _7, _8, _9, _1, _2],
            [_8, _9, _1, _2, _3, _4, _5, _6, _7],
            [_5, _6, _7, _8, _9, _1, _2, _3, _4],
            [_2, _3, _4, _5, _6, _7, _8, _9, _1],
        ],
        dtype=np.uint16,
    )

    # Validity check should return false
    assert not game._is_valid()


def test_invalid_column():
    """Test the validity of the board with an invalid column"""
    game = sudoku.Sudoku(debug=False)

    # Set the grid to have two invalid columns
    game.SUDOKU_GRID = np.array(
        [
            [_1, _2, _3, _4, _5, _6, _7, _8, _9],
            [_7, _8, _9, _1, _2, _3, _4, _5, _6],
            [_5, _4, _6, _7, _8, _9, _1, _2, _3],  # invalid cols 0, 1 (0-index)
            [_9, _1, _2, _3, _4, _5, _6, _7, _8],
            [_6, _7, _8, _9, _1, _2, _3, _4, _5],
            [_3, _4, _5, _6, _7, _8, _9, _1, _2],
            [_8, _9, _1, _2, _3, _4, _5, _6, _7],
            [_5, _6, _7, _8, _9, _1, _2, _3, _4],
            [_2, _3, _4, _5, _6, _7, _8, _9, _1],
        ],
        dtype=np.uint16,
    )

    # Validity check should return false
    assert not game._is_valid()


def test_invalid_subgrid():
    """Test the validity of the board with an invalid subgrid"""
    game = sudoku.Sudoku(debug=False)

    # Set the grid to have an invalid subgrid
    game.SUDOKU_GRID = np.array(
        [
            [_1, _2, _3, _4, _5, _6, _7, _8, _9],
            [_7, _8, _9, _1, _2, _3, _4, _5, _6],
            [_4, _5, _6, _7, _8, _9, _1, _2, _3],
            # ------------------------------------------------------------
            # Following subgrids are invalid, each subgrid has pattern:
            # [. . x]
            # [. . .]
            # [x . .]
            # where "x" are the duplicates, thus invalidating the subgrids
            [_9, _1, _2, _3, _4, _5, _6, _7, _8],
            [_6, _7, _8, _9, _1, _2, _3, _4, _5],
            [_2, _3, _4, _5, _6, _7, _8, _9, _1],
            [_3, _4, _5, _6, _7, _8, _9, _1, _2],
            [_8, _9, _1, _2, _3, _4, _5, _6, _7],
            [_5, _6, _7, _8, _9, _1, _2, _3, _4],
        ],
        dtype=np.uint16,
    )

    # Validity check should return false
    assert not game._is_valid()
