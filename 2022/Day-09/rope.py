"""
File: rope.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: December 2022
Description: This program implements my solution to the Advent of Code
 challenge.
"""

from knot import Knot


class Rope:
    """Class to represent a rope."""

    def __init__(self, length):
        self.length = length
        self.knots = [Knot() for _ in range(self.length)]

        self.head = self.knots[0]
        self.tail = self.knots[-1]

    def follow(self, directions):
        """Function to move the rope following the given directions."""

        for direction, n_steps in directions:
            for _ in range(n_steps):
                self.head.move(direction)
                self.head.save_current_position()

                for i in range(1, self.length):
                    self.knots[i].follow(self.knots[i - 1])
