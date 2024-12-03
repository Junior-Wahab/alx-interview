#!/usr/bin/python3
"""
This module defines a function to calculate the perimeter of an island
represented by a 2D grid.
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of the island in the given grid.

    Args:
        grid (list[list[int]]): A rectangular grid of integers where
            0 represents water and 1 represents land.

    Returns:
        int: The perimeter of the island in the grid.
    """

    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4  # Add 4 for all potential edges

                # Check for adjacent land and subtract shared edges
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2

    return perimeter
