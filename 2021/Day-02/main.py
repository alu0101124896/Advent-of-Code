'''
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: December 2021
Description: This program implemets my solution to the Advent of Code challenge.
'''


def main():
    '''Main function to resolve the challenge.'''
    planned_course = parse_data()

    horizontal_position, depth = move_submarine(planned_course)

    print("\nThe result of multiplying the final horizontal position by the",
          "final depth is:", horizontal_position * depth)


def parse_data():
    '''Funcion to parse the input data of the challenge.'''
    input_file = input("\nInput file: ")
    data = open(input_file, 'r').read().split("\n")

    if data[len(data) - 1] == '':
        data.pop()

    data = [command.split() for command in data]

    return data


def move_submarine(course, horizontal_position=0, depth=0):
    '''Function to calculate the horizontal position and depth of the submarine
    after following the given course.
    '''
    for movement, units in course:
        if movement == "forward":
            horizontal_position += int(units)
        elif movement == "down":
            depth += int(units)
        elif movement == "up":
            depth -= int(units)
        else:
            raise ValueError("Error: Unknown movement '" + movement + "'.")

    return horizontal_position, depth


if __name__ == "__main__":
    main()
