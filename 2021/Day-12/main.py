'''
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: December 2021
Description: This program implemets my solution to the Advent of Code challenge.
'''


def main():
    '''Main function to resolve the challenge.'''
    cave_connections = parse_data()

    posible_paths = find_posible_paths(cave_connections)

    print("\nThe number of posible paths is:", len(posible_paths))


def parse_data():
    '''Funcion to parse the input data of the challenge.'''
    input_file = input("\nInput file: ")
    data = open(input_file, 'r').read().split("\n")

    if data[len(data) - 1] == '':
        data.pop()

    return [set(line.split("-")) for line in data]


def find_posible_paths(cave_connections, current_cave=None, history=None):
    '''Function to find all posible paths to go from the starting cave to the
    ending one.'''
    if current_cave is None:
        current_cave = "start"
    if history is None:
        history = dict()

    if current_cave == "end":
        return {current_cave}
    else:
        if current_cave != "start" and current_cave.islower():
            history.update({current_cave: history.get(current_cave, 0) + 1})

        paths = set()
        for connection in get_connected_caves({current_cave}, cave_connections):
            if (connection.isupper()
                    or ((connection != "start") and
                        # (history.get(connection, 0) == 0))):
                        (list(history.values()).count(2) <= 1) and
                        (list(history.values()).count(3) == 0))):
                paths.update(
                    find_posible_paths(cave_connections, connection,
                                       history.copy()))

        posible_paths = set()
        for path in paths:
            posible_paths.add(current_cave + ',' + path)

        return posible_paths


def get_connected_caves(current_cave, cave_connections):
    '''Function to get all the caves connected to the current one.'''
    connected_caves = []

    for connection in cave_connections:
        if current_cave.issubset(connection):
            connected_caves.append(connection.difference(current_cave).pop())

    return connected_caves


if __name__ == "__main__":
    main()
