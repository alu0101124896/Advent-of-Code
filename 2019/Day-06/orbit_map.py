'''
File: orbit_map.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: October 2022
Description: This program implemets my solution to the Advent of Code challenge.
'''

from typing import Optional
from orbital_object import OrbitalObject


class OrbitMap:
    '''Class to represent an orbit map for the Advent of Code challenge.'''

    def __init__(self, orbits: list[list[str]]) -> None:

        self.my_location = None
        self.santa_location = None

        self.com = OrbitalObject("COM", None)  # Universal Center of Mass
        next_orbital_objects = [self.com]

        remaining_orbits = orbits.copy()

        while len(next_orbital_objects) > 0:
            current_orbital_object = next_orbital_objects.pop(0)

            while len(remaining_orbits) > 0:
                look_up_table = list(zip(*remaining_orbits))

                try:
                    orbit_id = look_up_table[0].index(
                        current_orbital_object.name)
                except ValueError:
                    break

                _, child_name = remaining_orbits.pop(orbit_id)
                new_child = OrbitalObject(child_name, current_orbital_object)
                current_orbital_object.childs.append(new_child)
                next_orbital_objects.append(new_child)

                if child_name == "YOU":
                    self.my_location = new_child

                elif child_name == "SAN":
                    self.santa_location = new_child

    def get_orbital_weight(self):
        '''Function to get the total number of direct and indirect orbits on the
        orbit map.'''

        return self.com.get_orbital_weight()

    def get_path_to_santa(self) -> Optional[int]:
        '''Function to get the minimum number of gravitational transfers to
        arrive at Santa's location.'''

        assert self.my_location, OrbitalObject
        assert self.santa_location, OrbitalObject

        my_path = self.my_location.get_path_to_com()
        santa_path = self.santa_location.get_path_to_com()

        for i in range(max(len(my_path), len(santa_path))):
            if my_path[i] != santa_path[i]:
                return len(my_path[i:-1]) + len(santa_path[i:-1])

        return None
