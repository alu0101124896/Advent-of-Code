"""
File: directory_tree.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: December 2022
Description: This program implements my solution to the Advent of Code
 challenge.
"""

from directory_node import DirectoryNode


class DirectoryTree:
    """Class to represent a filesystem directory tree."""

    def __init__(self, terminal_output):
        self.structure = DirectoryNode(name="/", size=0, node_type="dir")
        self.current_working_directory = []

        for line in terminal_output:
            if line[0] == "$":
                if line[1] == "cd":
                    self.change_directory(line[2])

                elif line[1] == "ls":
                    continue

                else:
                    raise ValueError("Error: command unknown")

            elif line[0] == "dir":
                self.add_to_cwd("dir", name=line[1])

            else:  # Should be a file
                self.add_to_cwd("file", name=line[1], size=int(line[0]))

    def change_directory(self, destiny="/"):
        """Function to change the current working directory to the given
        one."""

        if destiny == "/":
            self.current_working_directory = []
        elif destiny == "..":
            if len(self.current_working_directory) > 0:
                self.current_working_directory.pop()
        else:
            self.current_working_directory.append(destiny)

    def add_to_cwd(self, node_type, name, size=0):
        """Function to add a directory or file under the current working
        directory."""

        destination_directory = self.structure
        for subdirectory in self.current_working_directory:
            destination_directory = destination_directory.at(subdirectory)

        destination_directory.add(DirectoryNode(name, size, node_type))

    def get_all_directories(self):
        """Function to get a list of all directories on the filesystem."""

        return self.structure.get_all_directories()

    def get_total_size(self):
        """Function to get the total size of the filesystem."""

        return self.structure.get_total_size()
