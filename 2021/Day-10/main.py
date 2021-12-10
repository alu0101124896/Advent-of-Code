'''
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: December 2021
Description: This program implemets my solution to the Advent of Code challenge.
'''


def main():
    '''Main function to resolve the challenge.'''
    navigation_subsystem_code = parse_data()

    syntax_error_score = corrupted_data(navigation_subsystem_code)

    print("\nThe total syntax error score is:", syntax_error_score)


def parse_data():
    '''Funcion to parse the input data of the challenge.'''
    input_file = input("\nInput file: ")
    data = open(input_file, 'r').read().split("\n")

    if data[len(data) - 1] == '':
        data.pop()

    return [[char for char in line] for line in data]


def corrupted_data(code):
    '''Function to calculate the syntax error score of the navigation subsystem
    code.'''
    syntax_error_score = 0
    for line in code:
        open_brackets = []
        for char in line:
            if char in ['(', '[', '{', '<']:
                open_brackets.append(char)
            elif char in [')', ']', '}', '>']:
                if char == ')' and open_brackets[-1] != '(':
                    syntax_error_score += 3
                    break
                elif char == ']' and open_brackets[-1] != '[':
                    syntax_error_score += 57
                    break
                elif char == '}' and open_brackets[-1] != '{':
                    syntax_error_score += 1197
                    break
                elif char == '>' and open_brackets[-1] != '<':
                    syntax_error_score += 25137
                    break
                else:
                    open_brackets.pop()
            else:
                raise SyntaxError("Error: expected any kind of bracket," +
                                  f" but found '{char}' instead")

    return syntax_error_score


if __name__ == "__main__":
    main()
