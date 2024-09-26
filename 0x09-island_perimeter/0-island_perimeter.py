#!/usr/bin/python3

"""
Function to calculate the perimeter of an island in a grid.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island represented in a 2D grid.

    The grid is a list of lists, where:
    - 0 represents water
    - 1 represents land

    The function calculates the perimeter by iterating over the grid
    and counting the edges that touch water or are at the boundary.

    Args:
        grid (list): A 2D list of integers (0s and 1s) representing the island.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    total_rows = len(grid)
    total_cols = len(grid[0]) if total_rows else 0

    # Iterate through each cell in the grid
    for row in range(total_rows):
        for col in range(total_cols):

            if grid[row][col]:  # If the current cell is land (1)
                # Define the four neighboring cell coordinates
                # (up, left, right, down)
                neighbors = [(row - 1, col), (row, col - 1), (row, col + 1), (
                             row + 1, col)]

                # Check if each neighbor is within the grid boundaries
                is_valid_neighbor = [
                    1 if 0 <= neighbor[0] < total_rows and 0 <= neighbor[1] <
                    total_cols else 0
                    for neighbor in neighbors
                ]

                # Increment perimeter for each side that touches water or is
                # outside the grid
                perimeter += sum(
                    [1 if not valid or not grid[neighbor[0]][neighbor[1]]
                        else 0
                     for valid, neighbor in zip(is_valid_neighbor, neighbors)]
                )

    return perimeter
