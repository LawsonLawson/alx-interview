#!/usr/bin/python3
"""
N-Queens Problem Solver

This script solves the N-Queens problem, where N queens must be placed on
an NxN chessboard such that no two queens threaten each other. The solution
is printed as a list of coordinates, where each coordinate represents the
position of a queen on the board.
"""

import sys

# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

# Check if the argument is a digit
if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

# Ensure the board size is at least 4x4
board_size = int(sys.argv[1])
if board_size < 4:
    print("N must be at least 4")
    exit(1)


def find_queen_positions(board_size, row=0, columns=[], diagonals1=[],
                         diagonals2=[]):
    """Recursively find all valid queen positions on the board.

    Args:
        board_size (int): The size of the board (N).
        row (int): The current row being processed.
        columns (list): List of columns occupied by queens.
        diagonals1 (list): List of occupied primary diagonals (row + column).
        diagonals2 (list): List of occupied secondary diagonals (row - column).

    Yields:
        list: A list representing the column positions of queens in each row.
    """
    if row < board_size:
        for col in range(board_size):
            if col not in columns and (row + col) not in diagonals1 and\
                    (row - col) not in diagonals2:
                yield from find_queen_positions(board_size, row + 1,
                                                columns + [col], diagonals1 +
                                                [row + col], diagonals2 +
                                                [row - col])
    else:
        yield columns


def solve_n_queens(board_size):
    """
    Solve the N-Queens problem and print all solutions.

    Args:
        board_size (int): The size of the board (N).
    """
    for solution in find_queen_positions(board_size):
        queen_positions = [[row, col] for row, col in enumerate(solution)]
        print(queen_positions)


# Solve the N-Queens problem for the given board size
solve_n_queens(board_size)
