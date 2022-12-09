"""
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: December 2022
Description: This program implements my solution to the Advent of Code
 challenge.
"""

from copy import deepcopy


def main():
    """Main function to resolve the challenge."""

    stacks_initial_state, move_steps = parse_data()

    print("\nPart one:")

    stacks_final_state = get_final_state_v1(stacks_initial_state, move_steps)
    part_one_solution = get_top_crates(stacks_final_state)

    print("  The final message is:", part_one_solution)

    print("\nPart two:")

    stacks_final_state = get_final_state_v2(stacks_initial_state, move_steps)
    part_two_solution = get_top_crates(stacks_final_state)

    print("  The final message is:", part_two_solution)


def parse_data():
    """Function to parse the input data of the challenge."""

    input_file = input("\nInput file: ")

    with open(input_file, 'r', encoding="utf-8") as infile:
        raw_data = infile.read().split("\n\n")

    *initial_state, stack_number = raw_data[0].split("\n")

    stacks_state = []
    for i in range(len(stack_number)):
        if stack_number[i] == " ":
            continue

        current_stack = []
        for j in range(len(initial_state) - 1, -1, -1):
            try:
                current_crate = initial_state[j][i]
            except IndexError:
                break

            if current_crate != " ":
                current_stack.append(current_crate)
        stacks_state.append(current_stack)

    raw_move_steps = raw_data[1].split("\n")

    if raw_move_steps[-1] == "":
        raw_move_steps.pop()

    move_steps = [[int(num) for num in line.split(" ")[1::2]]
                  for line in raw_move_steps]

    return stacks_state, move_steps


def get_final_state_v1(initial_stacks_state, move_steps):
    """Function to get the final state of the stacks after moving the crates
    following the given move steps. Version 1 moves the crates one by one."""

    stacks_state = deepcopy(initial_stacks_state)

    for crates_to_move, origin, destiny in move_steps:
        for _ in range(crates_to_move):
            stacks_state[destiny-1].append(stacks_state[origin-1].pop())

    return stacks_state


def get_final_state_v2(initial_stacks_state, move_steps):
    """Function to get the final state of the stacks after moving the crates
    following the given move steps. Version 2 moves the groups of crates all
    together at the same time."""

    stacks_state = deepcopy(initial_stacks_state)

    for crates_to_move, origin, destiny in move_steps:
        stacks_state[destiny-1].extend(
            stacks_state[origin-1][-crates_to_move:])
        stacks_state[origin-1] = stacks_state[origin-1][:-crates_to_move]

    return stacks_state


def get_top_crates(stacks_state):
    """Function to get the crates on top of each of the given stacks."""

    return "".join((stack[-1] for stack in stacks_state))


if __name__ == "__main__":
    main()
