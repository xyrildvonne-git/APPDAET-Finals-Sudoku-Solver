"""Student-implemented recursive backtracking solver.

Required planned functions:
- find_empty_cell(board)
- solve_sudoku(board)
- count_solutions(board, limit=2)  # useful for uniqueness verification

Do not replace the core solver with a third-party Sudoku-solving package.
"""


# solver.py

# Sudoku board size
BOARD_SIZE = 9
BOX_SIZE = 3
EMPTY_CELL = 0


def is_candidate_valid(board, row, col, num):
    """
    Checks whether a number can be placed in a specific cell

    Parameters:
        board (list): The 9x9 Sudoku board
        row (int): The row index of the cell
        col (int): The column index of the cell
        num (int): The number to be checked (1-9)

    """

    # Check if the number already exists in the same row
    for c in range(BOARD_SIZE):
        if board[row][c] == num:
            return False

    # Check if the number already exists in the same column
    for r in range(BOARD_SIZE):
        if board[r][col] == num:
            return False

    # Determine the starting position of the 3x3 box
    box_start_row = (row // BOX_SIZE) * BOX_SIZE
    box_start_col = (col // BOX_SIZE) * BOX_SIZE

    # Check if the number already exists in the 3x3 box
    for r in range(box_start_row, box_start_row + BOX_SIZE):
        for c in range(box_start_col, box_start_col + BOX_SIZE):
            if board[r][c] == num:
                return False

    # The number does not violate any Sudoku rules
    return True


def find_empty_cell(board):
    """
    Finds the next empty cell in the Sudoku board

    Parameters:
        board (list): The 9x9 Sudoku board

    Returns:
        tuple: (row, col) if an empty cell is found
        None: If no empty cells remain
    """

    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == EMPTY_CELL:
                return row, col

    return None


def solve_sudoku(board):
    """
    Solves a Sudoku puzzle using recursive backtracking

    Parameters:
        board (list): The 9x9 Sudoku board

    Returns:
        bool: True if the puzzle is solved, otherwise False

    """

    # Find the next empty cell
    empty_cell = find_empty_cell(board)

    # No empty cells left, so the puzzle is solved
    if empty_cell is None:
        return True

    row, col = empty_cell

    # Try numbers from 1 to 9
    for num in range(1, BOARD_SIZE + 1):

        # Check if the number is valid in the current cell
        if is_candidate_valid(board, row, col, num):

            # Place the number in the empty cell
            board[row][col] = num

            # Recursively attempt to solve the remaining puzzle
            if solve_sudoku(board):
                return True

            # Backtrack if the current number leads to no solution
            board[row][col] = EMPTY_CELL

    # No valid number can solve this position
    return False

