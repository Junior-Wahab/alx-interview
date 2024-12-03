#!/usr/bin/python3
"""
Module for calculating the perimeter of an island described in a grid.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the grid.

    Args:
        grid (list of list of ints): The grid representation of the island.
            0 represents water, 1 represents land.

    Returns:
        int: The perimeter of the island.
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Add 4 for the land cell
                perimeter += 4
                # Subtract 1 for each adjacent land cell
                if i > 0 and grid[i - 1][j] == 1:  # Check top
                    perimeter -= 1
                if i < rows - 1 and grid[i + 1][j] == 1:  # Check bottom
                    perimeter -= 1
                if j > 0 and grid[i][j - 1] == 1:  # Check left
                    perimeter -= 1
                if j < cols - 1 and grid[i][j + 1] == 1:  # Check right
                    perimeter -= 1

    return perimeter
