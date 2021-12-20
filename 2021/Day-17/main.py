'''
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: December 2021
Description: This program implemets my solution to the Advent of Code challenge.
'''

import math


def main():
    '''Main function to resolve the challenge.'''
    target_area = parse_data()

    # highest_elevation = get_highest_elevation(target_area)
    num_of_posible_launches = get_all_posibilities(target_area)

    # print("\nThe highest elevation that can be achieved is:",
    #       highest_elevation)
    print("\nThe number of different posibilities of launching the probe is:",
          num_of_posible_launches)


def parse_data() -> tuple[tuple[int, int], tuple[int, int]]:
    '''Funcion to parse the input data of the challenge.'''
    input_file = input("\nInput file: ")
    data = open(input_file, 'r', encoding="utf-8").read().split("\n")

    target_area = data[0].split(": ")[1].split(", ")
    target_area = tuple(
        tuple(int(number) for number in axis.split('=')[1].split(".."))
        for axis in target_area)

    return target_area


def get_highest_elevation(
        target_area: tuple[tuple[int, int], tuple[int, int]]) -> int:
    '''Function to calculate the highest elevation that can be achieved while
    also being within the target after any step. (Calculus made assuming the
    posibility in the x axis displacement)'''
    initial_y_velocity = -target_area[1][0] - 1
    highest_elevation = (initial_y_velocity * (initial_y_velocity + 1)) // 2

    return highest_elevation


def get_all_posibilities(
        target_area: tuple[tuple[int, int], tuple[int, int]]) -> int:
    '''Function to obtain the number of posible initial velocities that makes
    the probe to be within the target after any step. '''
    min_x_init_vel = math.floor(quadratic_eq(1, 1, -2 * target_area[0][0]))
    solutions = set()

    for x_init_vel in range(min_x_init_vel, target_area[0][1] + 1):
        for y_init_vel in range(target_area[1][0], -target_area[1][0]):
            x_pos = 0
            y_pos = 0
            x_curr_vel = x_init_vel
            y_curr_vel = y_init_vel

            while x_pos <= target_area[0][1] and y_pos >= target_area[1][0]:
                if x_pos >= target_area[0][0] and y_pos <= target_area[1][1]:
                    solutions.add((x_init_vel, y_init_vel))
                    break

                else:
                    x_pos += x_curr_vel
                    y_pos += y_curr_vel
                    if x_curr_vel > 0:
                        x_curr_vel -= 1
                    y_curr_vel -= 1

    return len(solutions)


def quadratic_eq(a_val, b_val, c_val):
    '''Function to calculate the positive roots of a quadratic equation.
    (Calculus made assuming that 'temp' is always a real number)'''
    temp = math.sqrt((b_val**2) - (4 * a_val * c_val))

    result1 = (-b_val + temp) / (2 * a_val)
    result2 = (-b_val - temp) / (2 * a_val)

    if result1 > 0:
        return result1
    if result2 > 0:
        return result2


if __name__ == "__main__":
    main()
