'''
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: October 2022
Description: This program implemets my solution to the Advent of Code challenge.
'''

from operator import add, mul


def main():
    '''Main function to resolve the challenge.'''

    intcode = parse_data()

    print()

    run_intcode(intcode)

    print()


def parse_data() -> list[int]:
    '''Funcion to parse the input data of the challenge.'''

    input_file = input("\nInput file: ")

    with open(input_file, 'r', encoding="utf-8") as infile:
        rawdata = infile.read().split()

    intcode = [int(code) for code in rawdata[0].split(',')]

    return intcode


def run_intcode(intcode: list[int]):
    '''Function to run the given intcode program.'''

    instruction_pointer = 0

    while True:
        param_modes_and_opcode = str(intcode[instruction_pointer] + 100000)
        param_modes = param_modes_and_opcode[:-2]
        opcode = param_modes_and_opcode[-2:]

        if opcode == "01":
            instruction_offset = 4

        elif opcode == "02":
            instruction_offset = 4

        elif opcode == "03":
            instruction_offset = 2

        elif opcode == "04":
            instruction_offset = 2

        elif opcode == "99":
            break

        else:
            raise ValueError(f"Unknown opcode '{opcode}'.")

        params = [
            instruction_pointer +
            i if param_modes[-i] == '1' else intcode[instruction_pointer + i]
            for i in range(1, instruction_offset)
        ]

        if opcode == "01":
            intcode[params[2]] = add(intcode[params[0]], intcode[params[1]])

        elif opcode == "02":
            intcode[params[2]] = mul(intcode[params[0]], intcode[params[1]])

        elif opcode == "03":
            intcode[params[0]] = int(input("Input value: "))

        elif opcode == "04":
            print("Output value:", intcode[params[0]])

        else:
            raise ValueError("Unknown opcode.")

        instruction_pointer += instruction_offset

    # print(intcode)


if __name__ == "__main__":
    main()
