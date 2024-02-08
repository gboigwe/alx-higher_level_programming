#!/usr/bin/python3

"""Solves the N-queens puzzle.

Checks all possible ways N could be
No N queen against N queen on chessboard.

N integer must be >= 4.

Attributes:
    chess_field (list): List of lists the chessboard.
    way_possible (list): List of lists containing possibilities.

way_possible are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""


import sys


def chess_init(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    chess_field = []
    [chess_field.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in chess_field]
    return (chess_field)


def chess_rep(chess_field):
    """Return a deepcopy of a chessboard."""
    if isinstance(chess_field, list):
        return list(map(chess_rep, chess_field))
    return (chess_field)


def possible_way(chess_field):
    """Return the list of lists representation of a solved chessboard."""
    solution = []
    for r in range(len(chess_field)):
        for c in range(len(chess_field)):
            if chess_field[r][c] == "Q":
                solution.append([r, c])
                break
    return (solution)


def x_spot(chess_field, row, col):
    """Position spots on a chessboard.

    All spots where non-attacking queens can no
    longer be played are X-ed out.

    Args:
        chess_field (list): The current working chessboard.
        row (int): The row where a queen was last played.
        col (int): The column where a queen was last played.
    """

    for c in range(col + 1, len(chess_field)):
        chess_field[row][c] = "x"
    for c in range(col - 1, -1, -1):
        chess_field[row][c] = "x"
    for r in range(row + 1, len(chess_field)):
        chess_field[r][col] = "x"
    for r in range(row - 1, -1, -1):
        chess_field[r][col] = "x"
    c = col + 1
    for r in range(row + 1, len(chess_field)):
        if c >= len(chess_field):
            break
        chess_field[r][c] = "x"
        c += 1
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        chess_field[r][c]
        c -= 1
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(chess_field):
            break
        chess_field[r][c] = "x"
        c += 1
    c = col - 1
    for r in range(row + 1, len(chess_field)):
        if c < 0:
            break
        chess_field[r][c] = "x"
        c -= 1

def recursve_cal(chess_field, row, queens, way_possible):
    """Recursively solve an N-queens puzzle.

    Args:
        chess_field (list): The current working chessboard.
        row (int): The current working row.
        queens (int): The current number of placed queens.
        way_possible (list): A list of lists of way_possible.
    Returns:
        way_possible
    """

    if queens == len(chess_field):
        way_possible.append(possible_way(chess_field))
        return (way_possible)

    for c in range(len(chess_field)):
        if chess_field[row][c] == " ":
            tmp_board = chess_rep(chess_field)
            tmp_board[row][c] = "Q"
            x_spot(tmp_board, row, c)
            way_possible = recursve_cal(tmp_board, row + 1,
                                        queens + 1, way_possible)
    return (way_possible)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    chess_field = chess_init(int(sys.argv[1]))
    way_possible = recursve_cal(chess_field, 0, 0, [])
    for sol in way_possible:
        print(sol)
