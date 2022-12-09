"""
File: directory_node.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: December 2022
Description: This program implements my solution to the Advent of Code
 challenge.
"""


class DirectoryNode:
    """Class to represent a filesystem directory node, either a directory or a
     file."""

    def __init__(self, name, size, node_type):
        self.name = name
        self.size = size
        self.type = node_type

        self.structure = {}

    def at(self, subdirectory_name):
        """Function to get the directory or file with the given name."""

        return self.structure[subdirectory_name]

    def add(self, node):
        """Function to add the given directory or file under this one."""

        self.structure[node.name] = node

    def get_all_directories(self):
        """Function to get a list of all directories under this one."""

        if self.type == "file":
            return []

        directories = [self]
        for item in self.structure.values():
            directories.extend(item.get_all_directories())

        return directories

    def get_total_size(self):
        """Function to get the total size of this directory or file with all
        its content."""

        total_size = self.size
        for item in self.structure.values():
            total_size += item.get_total_size()

        return total_size
