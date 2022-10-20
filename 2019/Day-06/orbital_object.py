'''
File: orbital_object.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: October 2022
Description: This program implemets my solution to the Advent of Code challenge.
'''


class OrbitalObject:
    '''Class to represent an orbital object for the Advent of Code challenge.'''

    def __init__(self, name: str, childs: list = None) -> None:

        self.name = name

        if childs is None:
            self.childs = []
        else:
            self.childs = childs

    def get_orbital_weight(self, depth: int = 0) -> int:
        '''Function to get the total number of direct and indirect orbits on the
        orbit map recursively.'''

        total_weight = depth

        for child in self.childs:
            total_weight += child.get_orbital_weight(depth + 1)

        return total_weight
