#!/usr/bin/python3

"""
Rotate 2D Matrix Algorithm.

This module provides a function to rotate an n x n 2D matrix
90 degrees clockwise in place.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a given n x n 2D matrix 90 degrees clockwise in place.

    The function rotates the matrix by moving values in four sets of positions,
    effectively rotating each layer of the matrix starting from the outermost
    layer and moving inward.

    Args:
        matrix (list of list of int): The 2D matrix to rotate.

    Example:
        Given matrix:
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

        After rotation:
        [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ]
    """
    n = len(matrix)  # Size of the matrix (n x n)

    # Traverse the matrix in layers from outermost to innermost
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer

        for i in range(first, last):
            offset = i - first

            # Save the top element
            top = matrix[first][i]

            # Move elements from left to top
            matrix[first][i] = matrix[last - offset][first]

            # Move elements from bottom to left
            matrix[last - offset][first] = matrix[last][last - offset]

            # Move elements from right to bottom
            matrix[last][last - offset] = matrix[i][last]

            # Assign saved top element to right
            matrix[i][last] = top
