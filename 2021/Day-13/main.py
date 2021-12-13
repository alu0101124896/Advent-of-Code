'''
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: December 2021
Description: This program implemets my solution to the Advent of Code challenge.
'''


def main():
    '''Main function to resolve the challenge.'''
    transparent_paper, fold_instructions = parse_data()

    # print_as_matrix(transparent_paper)
    folded_paper = fold_paper(transparent_paper, fold_instructions)

    # print("\nThe number of points after first fold is:", len(folded_paper))
    print("\nThe activation code is:")
    print_as_matrix(folded_paper)


def parse_data():
    '''Funcion to parse the input data of the challenge.'''
    input_file = input("\nInput file: ")
    data = open(input_file, 'r').read().split("\n\n")

    transparent_paper = dict()
    for line in data[0].split("\n"):
        number = line.split(',')
        transparent_paper.update({line: [int(number[0]), int(number[1])]})

    fold_instructions = list()
    for line in data[1].split("\n"):
        if line != '':
            axis, index = tuple(line.split()[2].split("="))
            fold_instructions.append((0 if axis == 'x' else 1, int(index)))

    return transparent_paper, fold_instructions


def fold_paper(transparent_paper, fold_instructions):
    '''Function to fold the transparen paper.'''
    # fold_axis, fold_index = fold_instructions[0]
    for fold_axis, fold_index in fold_instructions:
        non_fold_axis = 1 - fold_axis

        folded_paper = dict()
        for point_key, point_value in transparent_paper.items():
            if point_value[fold_axis] < fold_index:
                folded_paper.update({point_key: point_value})
            else:
                new_point_value = [None, None]

                new_point_value[fold_axis] = (fold_index -
                                            (point_value[fold_axis] - fold_index))
                new_point_value[non_fold_axis] = point_value[non_fold_axis]

                new_point_key = f"{new_point_value[0]},{new_point_value[1]}"

                folded_paper.update({new_point_key: new_point_value})

        transparent_paper = folded_paper

    return folded_paper


def print_as_matrix(transparent_paper):
    '''Function to print the paper.'''
    paper_limit = {
        axis: max([point[axis] for point in transparent_paper.values()])
        for axis in [0, 1]
    }

    matrix = [[
        '#' if f"{x},{y}" in transparent_paper else '.'
        for x in range(paper_limit[0] + 1)
    ] for y in range(paper_limit[1] + 1)]

    print()
    for line in matrix:
        print(''.join(line))


if __name__ == "__main__":
    main()
