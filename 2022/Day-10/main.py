"""
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: December 2022
Description: This program implements my solution to the Advent of Code
 challenge.
"""


def main():
    """Main function to resolve the challenge."""

    program = parse_data()

    signal_strengths, crt_image = execute(program)

    print("\nPart one:")

    part_one_solution = sum(signal_strengths)

    print("  The sum of the signal strengths is:", part_one_solution)

    print("\nPart two:")

    print("  The CRT image produced is shown below:", end="\n\n")

    for line in crt_image:
        print(line)


def parse_data():
    """Function to parse the input data of the challenge."""

    input_file = input("\nInput file: ")

    with open(input_file, 'r', encoding="utf-8") as infile:
        raw_data = infile.read().split("\n")

    if raw_data[-1] == "":
        raw_data.pop()

    program = [instruction.split(" ") for instruction in raw_data]

    return program


def execute(program):
    """Function to execute the program and get the signal strengths at some
    specific clock cycles."""

    x_var = 1
    cycle_counter = 0
    signal_strengths = []
    current_instruction = None
    process_lock_timeout = 0
    sprite_position = move_sprite(x_var)
    current_crt_row = ""
    crt_image = []

    while len(program) > 0:
        cycle_counter += 1

        if (cycle_counter + 20) % 40 == 0:
            signal_strengths.append(cycle_counter * x_var)

        current_crt_col = (cycle_counter % 40) - 1
        current_crt_row += sprite_position[current_crt_col]

        if len(current_crt_row) == 40:
            crt_image.append(current_crt_row)
            current_crt_row = ""

        if process_lock_timeout == 0:
            current_instruction = program.pop(0)

            if current_instruction[0] == "noop":
                process_lock_timeout = 1
            elif current_instruction[0] == "addx":
                process_lock_timeout = 2

        if current_instruction[0] == "addx" and process_lock_timeout == 1:
            x_var += int(current_instruction[1])
            sprite_position = move_sprite(x_var)

        process_lock_timeout -= 1

    return signal_strengths, crt_image


def move_sprite(position):
    return [
        "#" if abs(position - i) <= 1 else "."
        for i in range(40)
    ]


if __name__ == "__main__":
    main()
