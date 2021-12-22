'''
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: December 2021
Description: This program implemets my solution to the Advent of Code challenge.
'''

import math
import json
import copy


class SFN:
    '''Class to represent a snailfish number as a binary tree.'''
    def __init__(self, pair, father=None) -> None:
        left, right = pair
        self.father: SFN = father

        if isinstance(left, list):
            self.left = SFN(left, father=self)
        else:
            self.left = left

        if isinstance(right, list):
            self.right = SFN(right, father=self)
        else:
            self.right = right

    def __str__(self) -> str:
        return '[' + str(self.left) + ',' + str(self.right) + ']'

    def __eq__(self, other):
        return str(self) == str(other)

    def __add__(self, other):
        result = SFN([self, other])
        self.father = result
        other.father = result
        result.reduce()
        return result

    def reduce(self):
        '''Function to reduce this snailfish number.'''
        while True:
            prev_red_state = copy.deepcopy(self)
            prev_exp_state = copy.deepcopy(self)
            self.check4explode()
            if self == prev_exp_state:
                self.check4split()
            if self == prev_red_state:
                break

        return self

    def check4explode(self, depth=0):
        '''Function to check if there's any pair that needs to be exploded.'''
        if (depth >= 4 and isinstance(self.left, int)
                and isinstance(self.right, int)):
            return True

        else:
            if isinstance(self.left, SFN):
                child_exploded = self.left.check4explode(depth + 1)
                if child_exploded:
                    if isinstance(self.right, int):
                        self.right += self.left.right
                    elif isinstance(self.right, SFN):
                        self.right.catch_explosion_down_left(self.left.right)
                    self.father.catch_explosion_up_left(self, self.left.left)
                    self.left = 0

            if isinstance(self.right, SFN):
                child_exploded = self.right.check4explode(depth + 1)
                if child_exploded:
                    if isinstance(self.left, int):
                        self.left += self.right.left
                    elif isinstance(self.left, SFN):
                        self.left.catch_explosion_down_right(self.right.left)
                    self.father.catch_explosion_up_right(self, self.right.right)
                    self.right = 0

            return False

    def catch_explosion_down_right(self, value):
        '''Function to catch the rests of the explosion.'''
        if isinstance(self.right, int):
            self.right += value
        elif isinstance(self.right, SFN):
            self.right.catch_explosion_down_right(value)

    def catch_explosion_down_left(self, value):
        '''Function to catch the rests of the explosion.'''
        if isinstance(self.left, int):
            self.left += value
        elif isinstance(self.left, SFN):
            self.left.catch_explosion_down_left(value)

    def catch_explosion_up_right(self, child, value):
        '''Function to catch the rests of the explosion.'''
        if self.right != child:
            if isinstance(self.right, int):
                self.right += value
            elif isinstance(self.right, SFN):
                self.right.catch_explosion_down_left(value)
        elif self.father is not None:
            self.father.catch_explosion_up_right(self, value)

    def catch_explosion_up_left(self, child, value):
        '''Function to catch the rests of the explosion.'''
        if self.left != child:
            if isinstance(self.left, int):
                self.left += value
            elif isinstance(self.left, SFN):
                self.left.catch_explosion_down_right(value)
        elif self.father is not None:
            self.father.catch_explosion_up_left(self, value)

    def check4split(self):
        '''Function to chekck if any regular number needs to be splitted.'''
        if isinstance(self.left, int):
            if self.left >= 10:
                temp = self.left / 2
                self.left = SFN((math.floor(temp), math.ceil(temp)), self)
                return True
        elif isinstance(self.left, SFN):
            if self.left.check4split():
                return True

        if isinstance(self.right, int):
            if self.right >= 10:
                temp = self.right / 2
                self.right = SFN((math.floor(temp), math.ceil(temp)), self)
                return True
        elif isinstance(self.right, SFN):
            if self.right.check4split():
                return True

        return False

    def get_magnitude(self):
        '''Function to get the magnitude of the snailfish number.'''
        magnitude = 0

        if isinstance(self.left, int):
            magnitude += 3 * self.left
        elif isinstance(self.left, SFN):
            magnitude += 3 * self.left.get_magnitude()

        if isinstance(self.right, int):
            magnitude += 2 * self.right
        elif isinstance(self.right, SFN):
            magnitude += 2 * self.right.get_magnitude()

        return magnitude


def main():
    '''Main function to resolve the challenge.'''
    data = parse_data()

    # final_sum = sum(data[1:], data[0])

    sums = list()
    for i_index, i_value in enumerate(data):
        for _, j_value in enumerate(data[i_index + 1:]):
            sums.append((copy.deepcopy(i_value) +
                         copy.deepcopy(j_value)).get_magnitude())
            sums.append((copy.deepcopy(j_value) +
                         copy.deepcopy(i_value)).get_magnitude())

    # print("\nThe magnitude of the final sum is:", final_sum.get_magnitude())
    print("\nThe largest magnitude of the sum of any pair is:", max(sums))


def parse_data() -> list[SFN]:
    '''Funcion to parse the input data of the challenge.'''
    input_file = input("\nInput file: ")
    data = open(input_file, 'r', encoding="utf-8").read().split("\n")

    if data[len(data) - 1] == '':
        data.pop()

    snailfish_numbers = [SFN(json.loads(line)) for line in data]

    return snailfish_numbers


if __name__ == "__main__":
    main()
