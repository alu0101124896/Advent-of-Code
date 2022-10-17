'''
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: October 2022
Description: This program implemets my solution to the Advent of Code challenge.
'''

from operator import add, mul


def main():
    '''Main function to resolve the challenge.'''

    original_intcode = parse_data()

    intcode = initialize_memory(original_intcode.copy(), 12, 2)
    intcode = run_intcode(intcode)

    print("\nThe value left at position 0 is:", intcode[0], end="\n\n")


def parse_data() -> list[int]:
    '''Funcion to parse the input data of the challenge.'''

    input_file = input("\nInput file: ")

    with open(input_file, 'r', encoding="utf-8") as infile:
        rawdata = infile.read().split()

    intcode = [int(code) for code in rawdata[0].split(",")]

    return intcode


def initialize_memory(intcode: list[int], first_value: int,
                      second_value: int) -> list[int]:
    '''Function to set the initial state of the intcode computer's memory'''

    intcode[1] = first_value
    intcode[2] = second_value

    return intcode


def run_intcode(intcode: list[int]) -> list[int]:
    '''Function to run the given intcode program.'''

    instruction_pointer = 0

    while True:
        opcode = intcode[instruction_pointer]

        if opcode == 1:
            operator = add

        elif opcode == 2:
            operator = mul

        elif opcode == 99:
            break

        op_1_pos = intcode[instruction_pointer + 1]
        op_2_pos = intcode[instruction_pointer + 2]
        result_pos = intcode[instruction_pointer + 3]

        intcode[result_pos] = operator(intcode[op_1_pos], intcode[op_2_pos])

        instruction_pointer += 4

    return intcode


if __name__ == "__main__":
    main()
