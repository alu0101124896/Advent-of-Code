'''
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: December 2021
Description: This program implemets my solution to the Advent of Code challenge.
'''


def main():
    '''Main function to resolve the challenge.'''
    notes = parse_data()

    # result = count_1_4_7_or_8_ocurrences(notes)
    result = decode(notes)

    # print("\nThe number of times that '1', '4', '7', or '8' appear is:", result)
    print("\nThe sum of all decoded output values is:", result)


def parse_data():
    '''Funcion to parse the input data of the challenge.'''
    input_file = input("\nInput file: ")
    data = open(input_file, 'r').read().split("\n")

    if data[len(data) - 1] == '':
        data.pop()

    return [[[{char
               for char in pattern} for pattern in part.split()]
             for part in line.split(" | ")] for line in data]


def count_1_4_7_or_8_ocurrences(notes):
    '''Function to count how many times '1', '4', '7', or '8' appear in the
    output values.'''
    return sum([
        len(pattern) == 2 or \
        len(pattern) == 3 or \
        len(pattern) == 4 or \
        len(pattern) == 7 \
        for line in notes
        for pattern in line[1]
    ])


def decode(notes):
    '''Function to decode the seven-segment displays values.'''
    result = 0
    for line in notes:
        code = get_code(line[0])

        decoded_output_value = ""
        for coded_output_digit in line[1]:
            for decoded_digit, coded_digit in code.items():
                if coded_output_digit == coded_digit:
                    decoded_output_value += decoded_digit

        result += int(decoded_output_value)

    return result


def get_code(unique_signal_patterns):
    '''Function to obtain the codification of each seven-segment display.'''
    code = dict()

    for pattern in unique_signal_patterns:
        if len(pattern) == 2:
            code.update({"1": pattern})
        if len(pattern) == 4:
            code.update({"4": pattern})
        if len(pattern) == 3:
            code.update({"7": pattern})
        if len(pattern) == 7:
            code.update({"8": pattern})

    for pattern in unique_signal_patterns:
        if len(pattern) == 5 and code.get("7").issubset(pattern):
            code.update({"3": pattern})
        if len(pattern) == 6 and code.get("4").issubset(pattern):
            code.update({"9": pattern})

    for pattern in unique_signal_patterns:
        if len(pattern) == 5 and code.get("9").issuperset(pattern) \
                    and not code.get("7").issubset(pattern):
            code.update({"5": pattern})
        if len(pattern) == 5 and not code.get("9").issuperset(pattern) \
                    and not code.get("7").issubset(pattern):
            code.update({"2": pattern})

    for pattern in unique_signal_patterns:
        if len(pattern) == 6 and code.get("5").issubset(pattern) \
                    and not code.get("4").issubset(pattern):
            code.update({"6": pattern})
        if len(pattern) == 6 and not code.get("5").issubset(pattern) \
                    and not code.get("4").issubset(pattern):
            code.update({"0": pattern})

    return code


if __name__ == "__main__":
    main()
