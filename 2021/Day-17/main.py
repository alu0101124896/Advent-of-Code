'''
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: December 2021
Description: This program implemets my solution to the Advent of Code challenge.
'''


def main():
    '''Main function to resolve the challenge.'''
    target_area = parse_data()

    highest_elevation = get_highest_elevation(target_area)

    print("\nThe highest elevation that can be achieved is:", highest_elevation)


def parse_data() -> tuple[tuple[int, int], tuple[int, int]]:
    '''Funcion to parse the input data of the challenge.'''
    input_file = input("\nInput file: ")
    data = open(input_file, 'r').read().split("\n")

    target_area = data[0].split(": ")[1].split(", ")
    target_area = tuple(
        tuple(int(number) for number in axis.split('=')[1].split(".."))
        for axis in target_area)

    return target_area


def get_highest_elevation(
        target_area: tuple[tuple[int, int], tuple[int, int]]) -> int:
    '''Function to calculate the highest elevation that can be achieved while
    also being within the target after any step. (Calculus made asuming the
    posibility in the x axis displacement)'''
    initial_y_velocity = -target_area[1][0] - 1
    highest_elevation = (initial_y_velocity * (initial_y_velocity + 1)) // 2

    return highest_elevation


if __name__ == "__main__":
    main()
