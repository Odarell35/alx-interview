#!/usr/bin/python3
"""Island perimeter Module"""


def island_perimeter(grid):
    """Function
    takes grid as
    """
    perimeter = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if ni < 0 or ni >= len(grid) or nj < 0 or nj >= len(grid[0]) or grid[ni][nj] == 0:
                        perimeter += 1

    return perimeter
