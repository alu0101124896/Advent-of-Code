'''
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: December 2021
Description: This program implemets my solution to the Advent of Code challenge.
'''


def main():
    '''Main function to resolve the challenge.'''
    days_to_give_birth = parse_data()

    result = calculate_lanternfish_population(days_to_give_birth)

    print("\nThe number lanternfishes after 80 days is:", result)


def parse_data():
    '''Funcion to parse the input data of the challenge.'''
    input_file = input("\nInput file: ")
    data = open(input_file, 'r').read().split("\n")

    days_to_give_birth = dict()
    for number in data[0].split(","):
        days_to_give_birth.update({
            int(number):
            days_to_give_birth.get(int(number), 0) + 1,
        })

    return days_to_give_birth


def calculate_lanternfish_population(days_to_give_birth):
    '''Function to calculate the population of lanternfishes.'''
    for _ in range(80):
        next_day = dict()
        for time, quantity in days_to_give_birth.items():
            if time == 0:
                next_day.update({
                    6: quantity + next_day.get(6, 0),
                    8: quantity + next_day.get(8, 0),
                })
            else:
                next_day.update({
                    time - 1: quantity + next_day.get(time - 1, 0),
                })
        days_to_give_birth = next_day.copy()

    return sum(days_to_give_birth.values())


if __name__ == "__main__":
    main()
