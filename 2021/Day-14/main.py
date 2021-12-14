'''
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: December 2021
Description: This program implemets my solution to the Advent of Code challenge.
'''


def main():
    '''Main function to resolve the challenge.'''
    polymer_template, pair_insertion_rules = parse_data()

    polymer_score = find_polymer_score(polymer_template, pair_insertion_rules)

    print("\nThe score is:", polymer_score)


def parse_data():
    '''Funcion to parse the input data of the challenge.'''
    input_file = input("\nInput file: ")
    data = open(input_file, 'r').read().split("\n\n")

    pair_insertion_rules = dict()
    for line in data[1].split("\n"):
        if line != '':
            rule = line.split(" -> ")
            pair_insertion_rules.update({rule[0]: rule[1]})

    return data[0], pair_insertion_rules


def find_polymer_score(polymer, pair_insertion_rules):
    '''Function to get the polymer score after some polymerization steps.'''
    polymer_pairs = dict()
    for pair in zip(polymer[:-1], polymer[1:]):
        polymer_pairs.update({
            ''.join(pair):
            polymer_pairs.get(''.join(pair), 0) + 1,
        })

    for _ in range(10):
        new_polymer_pairs = dict()
        for pair, times_repeted in polymer_pairs.items():
            new_element = pair_insertion_rules[''.join(pair)]

            new_polymer_pairs.update({
                pair[0] + new_element:
                new_polymer_pairs.get(pair[0] + new_element, 0) + times_repeted,
                new_element + pair[1]:
                new_polymer_pairs.get(new_element + pair[1], 0) + times_repeted,
            })

        polymer_pairs = new_polymer_pairs

    polymer_elements = dict({polymer[0]: 1})
    for pair, times_repeted in polymer_pairs.items():
        polymer_elements.update({
            pair[1]:
            polymer_elements.get(pair[1], 0) + times_repeted,
        })

    polymer_score = (max(polymer_elements.values()) -
                     min(polymer_elements.values()))
    return polymer_score


if __name__ == "__main__":
    main()
