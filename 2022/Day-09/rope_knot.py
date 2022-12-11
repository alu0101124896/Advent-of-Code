"""
File: rope_knot.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: December 2022
Description: This program implements my solution to the Advent of Code
 challenge.
"""


class RopeKnot:
    """Class to represent a rope knot."""

    def __init__(self, start_position=(0, 0)):
        self.x_pos = start_position[0]
        self.y_pos = start_position[1]

        self.history = [(self.x_pos, self.y_pos)]

    def move_towards(self, direction):
        """Function to move a knot towards the given direction."""

        if direction == "U":
            self.y_pos += 1
        elif direction == "R":
            self.x_pos += 1
        elif direction == "D":
            self.y_pos -= 1
        elif direction == "L":
            self.x_pos -= 1

        else:
            raise ValueError("Error: unknown direction")

        self.history.append((self.x_pos, self.y_pos))

    def move_to(self, position):
        """Function to move a knot to the given position."""

        self.x_pos = position[0]
        self.y_pos = position[1]

        self.history.append((self.x_pos, self.y_pos))

    def is_touching(self, other):
        """Function to check if two knots are touching each other."""

        assert isinstance(other, RopeKnot)

        return (
            (abs(self.x_pos - other.x_pos) <= 1)
            and (abs(self.y_pos - other.y_pos) <= 1)
        )

    def prev_location(self):
        """Function to get the previous location of the knot."""

        return self.history[-2]

    def unique_positions(self):
        """Function to get a set with the positions visited at least once."""

        return {*self.history}
