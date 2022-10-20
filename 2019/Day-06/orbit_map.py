'''
File: orbit_map.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: October 2022
Description: This program implemets my solution to the Advent of Code challenge.
'''

from orbital_object import OrbitalObject


class OrbitMap:
    '''Class to represent an orbit map for the Advent of Code challenge.'''

    def __init__(self, orbits: list[list[str]]) -> None:

        self.com = OrbitalObject("COM")  # Universal Center of Mass
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
                new_child = OrbitalObject(child_name)
                current_orbital_object.childs.append(new_child)
                next_orbital_objects.append(new_child)

    def get_orbital_weight(self):
        '''Function to get the total number of direct and indirect orbits on the
        orbit map.'''

        return self.com.get_orbital_weight()
