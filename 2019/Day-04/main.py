'''
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: October 2022
Description: This program implemets my solution to the Advent of Code challenge.
'''

PASSWD_LEN = 6


def main():
    '''Main function to resolve the challenge.'''

    lower_bound, upper_bound = parse_data()

    valid_passwords = password_generator(lower_bound, upper_bound)

    print("\nThe number of valid passwords is:",
          len(valid_passwords),
          end="\n\n")


def parse_data():
    '''Funcion to parse the input data of the challenge.'''

    input_file = input("\nInput file: ")

    with open(input_file, 'r', encoding="utf-8") as infile:
        rawdata = infile.read().split()

    lower_bound, upper_bound = rawdata[0].split("-")

    return int(lower_bound), int(upper_bound)


def password_generator(lower_bound, upper_bound):
    '''Function to generate all valid passwords within a given range.'''

    valid_passwords = set()

    for password in range(lower_bound, upper_bound):
        password = str(password)

        if valid_password(password):
            valid_passwords.add(password)

    return valid_passwords


def valid_password(password):
    '''Function to check if a given password meets the imposed criteria.'''

    if len(password) != PASSWD_LEN:
        return False

    adjacent_matching_digits = []
    current_amd = [password[0]]

    for i in range(PASSWD_LEN - 1):
        if password[i] == password[i + 1]:
            current_amd.append(password[i + 1])

        else:
            adjacent_matching_digits.append(current_amd.copy())
            current_amd = [password[i + 1]]

    adjacent_matching_digits.append(current_amd.copy())

    if not any(len(amd) == 2 for amd in adjacent_matching_digits):
        return False

    for i in range(PASSWD_LEN - 1):
        for j in range(i + 1, PASSWD_LEN):
            if password[i] > password[j]:
                return False

    return True


if __name__ == "__main__":
    main()
