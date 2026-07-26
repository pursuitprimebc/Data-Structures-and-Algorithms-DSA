''' PROBLEM - 463. Island Perimeter
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more 
connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular,
width and height don't exceed 100. Determine the perimeter of the island.
'''


class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        row =len(grid)
        clmn = len(grid[0])
        perimeter = 0
        for r in range(row):
            for c in range(clmn):
                if grid[r][c] == 1:
                    #up
                    if r == 0 or grid[r-1][c] == 0:
                        perimeter += 1
                    # down
                    if r == row -1 or grid[r+1][c] == 0:
                        perimeter += 1
                    # left
                    if c==0 or grid[r][c-1]==0:
                        perimeter += 1
                    # right
                    if c==clmn-1  or grid[r][c+1]==0:
                        perimeter += 1
        return perimeter