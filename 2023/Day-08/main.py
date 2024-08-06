"""
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: August 2024
Description: This program implements my solution to the Advent of Code challenge.
"""

from typing import Generator


def main():
    """Main function to resolve the challenge."""

    instructions, nodes_info = parse_data()

    # Part one

    num_steps = traverse_map(instructions, nodes_info)

    print("The number of steps required to reach 'ZZZ' is", num_steps)

    # Part two

    num_steps = traverse_ghost_map(instructions, nodes_info)

    print(
        "The number of steps required to be only on nodes that end with 'Z' is",
        num_steps,
    )


def parse_data() -> tuple[str, dict[str, dict[str, str]]]:
    """Function to parse the input data of the challenge."""

    input_file = input("\nInput file: ")

    with open(input_file, "r", encoding="utf-8") as infile:
        rawdata = infile.read().split("\n\n")

    instructions = rawdata[0]

    nodes_info = {}
    for node_raw_info in rawdata[1].split("\n"):
        if node_raw_info == "":
            continue

        node_name, node_destinations = node_raw_info.split(" = ")
        left_destination, right_destination = node_destinations[1:-1].split(", ")

        nodes_info.update(
            {
                node_name: {
                    "L": left_destination,
                    "R": right_destination,
                }
            }
        )

    return instructions, nodes_info


def traverse_map(
    instructions: str,
    nodes_info: dict[str, dict[str, str]],
    start: str = "AAA",
    end: str = "ZZZ",
) -> int:
    """
    Function to calculate the number of steps needed to traverse a map between the given
     starting and ending points.
    """

    num_steps = 0
    current_location = start

    while not current_location.endswith(end):

        current_step_direction = instructions[num_steps % len(instructions)]
        current_location = nodes_info[current_location][current_step_direction]

        num_steps += 1

    return num_steps


def traverse_ghost_map(
    instructions: str,
    nodes_info: dict[str, dict[str, str]],
    start_ending_char: str = "A",
    end_ending_char: str = "Z",
) -> int:
    """
    Function to calculate the number of steps needed to traverse a map as a ghost
     between the given starting and ending points simultaneously.
    """

    starting_locations = set()
    ending_locations = set()

    for node_name in nodes_info.keys():
        if node_name[-1] == start_ending_char:
            starting_locations.add(node_name)
        elif node_name[-1] == end_ending_char:
            ending_locations.add(node_name)

    individual_steps = [
        traverse_map(instructions, nodes_info, starting_location, end_ending_char)
        for starting_location in starting_locations
    ]

    return least_common_multiple(individual_steps)


def least_common_multiple(numbers_list) -> int:
    """Function to calculate the Least Common Multiple number of the given numbers."""

    lcm_factors = {}
    for number in numbers_list:
        for prime_factor, factor_repetitions in factorize(number).items():
            if (
                prime_factor not in lcm_factors
                or lcm_factors[prime_factor] < factor_repetitions
            ):
                lcm_factors.update({prime_factor: factor_repetitions})

    lcm = 1
    for prime_factor, factor_repetitions in lcm_factors.items():
        lcm *= prime_factor * factor_repetitions

    return lcm


def factorize(number: int) -> dict[int, int]:
    """Function to calculate the prime factors of a given number."""

    current_number = number
    prime_factors = {}
    prime_numbers = prime_numbers_gen()
    current_prime_number = next(prime_numbers)

    while current_number != 1:
        quotient, remainder = divmod(current_number, current_prime_number)

        if remainder == 0:
            try:
                prime_factors[current_prime_number] += 1
            except KeyError:
                prime_factors.update({current_prime_number: 1})

            current_number = quotient

        else:
            current_prime_number = next(prime_numbers)

    return prime_factors


def prime_numbers_gen() -> Generator:
    """Python generator to get the prime numbers on demand, starting from '2'."""

    prime_candidate = 2
    while True:

        for divisor in range(2, ((prime_candidate + 1) // 2)):
            if prime_candidate % divisor == 0:
                break

        else:
            yield prime_candidate

        prime_candidate += 1


if __name__ == "__main__":
    main()
