"""
File: cell.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: December 2022
Description: This program implements my solution to the Advent of Code
 challenge.
"""

from math import inf

HEIGHT_ORDER = "SabcdefghijklmnopqrstuvwxyzE"


class Cell:
    def __init__(self, position, height):
        self.x = position[0]
        self.y = position[1]
        self.height = HEIGHT_ORDER.index(height)

        self.distance = inf
        self.previous_cell = None

    def location(self):
        """Function to get the grid's location of this cell."""

        return self.x, self.y

    def get_neighbors(self, grid):
        """Function to get the accessible neighbors of this cell."""

        neighbors = []

        for i, j in [
            (self.x - 1, self.y),
            (self.x + 1, self.y),
            (self.x, self.y - 1),
            (self.x, self.y + 1),
        ]:
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]):
                continue

            neighbor = grid[i][j]
            if neighbor.height <= self.height + 1:
                neighbors.append(neighbor)

        return neighbors
