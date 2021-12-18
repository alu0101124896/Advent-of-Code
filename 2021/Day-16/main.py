'''
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: December 2021
Description: This program implemets my solution to the Advent of Code challenge.
'''


def main():
    '''Main function to resolve the challenge.'''
    code = parse_data()

    total_packet_version, _ = evaluate(code)

    print("\nThe sum of all packet version numbers is:", total_packet_version)


def parse_data():
    '''Funcion to parse the input data of the challenge.'''
    input_file = input("\nInput file: ")
    data = open(input_file, 'r').read().split("\n")

    return hex2bin(data[0])


def hex2bin(hex_number):
    '''Function to convert the hexadecimal representation of a number into it's
    binary form.'''
    bin_number = ""
    for char in hex_number:
        if char == '0':
            bin_number += '0000'
        elif char == '1':
            bin_number += '0001'
        elif char == '2':
            bin_number += '0010'
        elif char == '3':
            bin_number += '0011'
        elif char == '4':
            bin_number += '0100'
        elif char == '5':
            bin_number += '0101'
        elif char == '6':
            bin_number += '0110'
        elif char == '7':
            bin_number += '0111'
        elif char == '8':
            bin_number += '1000'
        elif char == '9':
            bin_number += '1001'
        elif char == 'A':
            bin_number += '1010'
        elif char == 'B':
            bin_number += '1011'
        elif char == 'C':
            bin_number += '1100'
        elif char == 'D':
            bin_number += '1101'
        elif char == 'E':
            bin_number += '1110'
        elif char == 'F':
            bin_number += '1111'
    return bin_number


def evaluate(code):
    '''Function to evaluate the BITS transmission code.'''
    packet_version = int(code[:3], 2)
    packet_type_id = int(code[3:6], 2)
    packet_content_left = code[6:]

    if packet_type_id == 4:
        binary_value = ""
        last = False
        while not last:
            if packet_content_left[0] == '0':
                last = True
            binary_value += packet_content_left[1:5]
            packet_content_left = packet_content_left[5:]
        literal_value = int(binary_value, 2)

    else:
        length_type_id = int(packet_content_left[0])
        packet_content_left = packet_content_left[1:]

        if length_type_id == 0:
            sub_packets_content_length = int(packet_content_left[:15], 2)
            packet_content_left = packet_content_left[15:]
            packet_content_length = len(packet_content_left)
            consumed_sub_packets_content_length = 0
            while (consumed_sub_packets_content_length <
                   sub_packets_content_length):
                sub_packet_version, packet_content_left = \
                        evaluate(packet_content_left)
                packet_version += sub_packet_version
                consumed_sub_packets_content_length = (packet_content_length -
                                                       len(packet_content_left))
        else:
            num_of_sub_packets = int(packet_content_left[:11], 2)
            packet_content_left = packet_content_left[11:]
            for _ in range(num_of_sub_packets):
                sub_packet_version, packet_content_left = \
                        evaluate(packet_content_left)
                packet_version += sub_packet_version

    return packet_version, packet_content_left


if __name__ == "__main__":
    main()
