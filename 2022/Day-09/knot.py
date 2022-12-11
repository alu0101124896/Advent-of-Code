"""
File: knot.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: December 2022
Description: This program implements my solution to the Advent of Code
 challenge.
"""


class Knot:
    """Class to represent a rope knot."""

    def __init__(self, start_position=(0, 0)):
        self.x_pos = start_position[0]
        self.y_pos = start_position[1]

        self.history = []
        self.save_current_position()

    def save_current_position(self):
        """Function to save the current position to the history."""

        self.history.append((self.x_pos, self.y_pos))

    def move(self, direction):
        """Function to move a knot towards the given direction."""

        if direction is None:
            return

        elif direction == "U":
            self.y_pos += 1
        elif direction == "R":
            self.x_pos += 1
        elif direction == "D":
            self.y_pos -= 1
        elif direction == "L":
            self.x_pos -= 1

        else:
            raise ValueError("Error: unknown direction")

    def follow(self, other):
        """Function to move a knot to be touching the other knot."""

        if self.is_touching(other):
            return

        x_dir, y_dir = self.get_direction(other)

        self.move(x_dir)
        self.move(y_dir)

        self.save_current_position()

    def is_touching(self, other):
        """Function to check if two knots are touching each other."""

        assert isinstance(other, Knot)

        return (
            (abs(self.x_pos - other.x_pos) <= 1)
            and (abs(self.y_pos - other.y_pos) <= 1)
        )

    def get_direction(self, other):
        """Function to get the relative direction of two knots."""

        if (other.x_pos - self.x_pos) == 0:
            x_dir = None
        elif (other.x_pos - self.x_pos) > 0:
            x_dir = "R"
        else:
            x_dir = "L"

        if (other.y_pos - self.y_pos) == 0:
            y_dir = None
        elif (other.y_pos - self.y_pos) > 0:
            y_dir = "U"
        else:
            y_dir = "D"

        return x_dir, y_dir

    def prev_location(self):
        """Function to get the previous location of the knot."""

        return self.history[-2]

    def unique_positions(self):
        """Function to get a set with the positions visited at least once."""

        return {*self.history}
