"""
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: December 2022
Description: This program implements my solution to the Advent of Code
 challenge.
"""

from functools import reduce
import re

REG_EXP = re.compile(r"""
    (?P<LB>\[)     # Left bracket
    |(?P<RB>])     # Right bracket    
    |(?P<COM>,)    # Comma
    |(?P<NUM>\d+)  # Number
""", re.VERBOSE)


def main():
    """Main function to resolve the challenge."""

    packet_pairs = parse_data()

    print("\nPart one:")

    part_one_solution = sum(get_correct_packet_indices(packet_pairs))

    print("  The sum of indices of correct packets is:", part_one_solution)

    print("\nPart two:")

    all_received_packets = []
    for packet_pair in packet_pairs:
        all_received_packets.extend(packet_pair)

    divider_packets = [[[2]], [[6]]]

    sorted_packets = sort_packets(all_received_packets + divider_packets)

    part_two_solution = reduce(
        lambda x, y: x * y,
        (sorted_packets.index(divider_packet) + 1
         for divider_packet in divider_packets)
    )

    print("  The sum of indices of correct packets is:", part_two_solution)


def parse_data():
    """Function to parse the input data of the challenge."""

    input_file = input("\nInput file: ")

    with open(input_file, 'r', encoding="utf-8") as infile:
        raw_data = infile.read().split("\n\n")

    packet_pairs = [[parse_exp(raw_packet)[0]
                     for raw_packet in line.split("\n")[:2]]
                    for line in raw_data]

    return packet_pairs


def parse_exp(raw_packet):
    """Function to parse the contents of a given packet."""

    current_match = re.match(REG_EXP, raw_packet)

    if (current_match.group("RB") is not None
            or current_match.group("COM") is not None):
        raise ValueError

    remaining_packet = raw_packet[current_match.end():]

    if current_match.group("NUM") is not None:
        parsed_exp = int(current_match.group("NUM"))
    elif current_match.group("LB") is not None:
        parsed_exp, remaining_packet = parse_enum(remaining_packet)
    else:
        raise ValueError

    return parsed_exp, remaining_packet


def parse_enum(raw_packet):
    """Function to parse the enumeration of items inside a list."""

    current_enum = []
    current_match = re.match(REG_EXP, raw_packet)

    if current_match.group("RB") is not None:
        return current_enum, raw_packet[current_match.end():]

    parsed_exp, remaining_packet = parse_exp(raw_packet)
    current_enum.append(parsed_exp)

    while True:
        current_match = re.match(REG_EXP, remaining_packet)
        remaining_packet = remaining_packet[current_match.end():]

        if current_match.group("RB") is not None:
            break

        if current_match.group("COM") is None:
            raise ValueError("Error: comma expected")

        parsed_exp, remaining_packet = parse_exp(remaining_packet)
        current_enum.append(parsed_exp)

    return current_enum, remaining_packet


def get_correct_packet_indices(packet_pairs):
    """Function to get the indices of all correct pairs from the given list."""

    return [
        i + 1
        for i, (left_packet, right_packet) in enumerate(packet_pairs)
        if compare(left_packet, right_packet) == 1
    ]


def compare(left, right):
    """Function to check if the two given packets are in the correct order."""

    if isinstance(left, int) and isinstance(right, int):
        if left == right:
            return 0
        elif left < right:
            return 1
        else:
            return -1

    left = left if isinstance(left, list) else [left]
    right = right if isinstance(right, list) else [right]

    current_index = 0
    while True:
        try:
            comparison_result = compare(left[current_index],
                                        right[current_index])
        except IndexError:
            return compare(len(left), len(right))

        if comparison_result != 0:
            return comparison_result

        current_index += 1


def sort_packets(packets):
    """Function to sort all packets (cocktail shaker sort implementation)."""

    begin_idx = 0
    end_idx = len(packets) - 1

    while begin_idx <= end_idx:
        new_begin_idx = end_idx
        new_end_idx = begin_idx

        for i in range(begin_idx, end_idx):
            if compare(packets[i], packets[i + 1]) != 1:
                packets[i + 1], packets[i] = packets[i:(i + 2)]
                new_end_idx = i + 1
        end_idx = new_end_idx - 1

        for i in range(end_idx, begin_idx, -1):
            if compare(packets[i - 1], packets[i]) != 1:
                packets[i], packets[i - 1] = packets[(i - 1):(i + 1)]
                new_begin_idx = i - 1
        begin_idx = new_begin_idx + 1

    return packets


if __name__ == "__main__":
    main()
