'''
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: December 2021
Description: This program implemets my solution to the Advent of Code challenge.
'''


def main():
    '''Main function to resolve the challenge.'''
    called_numbers, boards = parse_data()

    score = play_bingo(called_numbers, boards)

    print("\nThe final score of the first winnning board is:", score)


def parse_data():
    '''Funcion to parse the input data of the challenge.'''
    input_file = input("\nInput file: ")
    data = open(input_file, 'r').read().split("\n\n")

    called_numbers = {int(number): False for number in data[0].split(",")}
    boards = [[[int(number) for number in row.split()]
               for row in board.split("\n")] for board in data[1:]]

    if boards[len(boards) - 1][len(boards[len(boards) - 1]) - 1] == []:
        boards[len(boards) - 1].pop()

    return called_numbers, boards


def play_bingo(called_numbers, boards):
    '''Function to play bingo and get the score of the winning board.'''
    for called_number in called_numbers.keys():
        called_numbers[called_number] = True
        for board in boards:
            board_t = list(zip(*board))
            if check_marked_inline(called_numbers, board) or \
               check_marked_inline(called_numbers, board_t):
                return calculate_score(board, called_numbers, called_number)


def check_marked_inline(called_numbers, board):
    '''Function to check if there is any row with all marked numbers.'''
    for row in board:
        points_on_row = 0
        for number in row:
            if called_numbers[number]:
                points_on_row += 1
        if points_on_row == 5:
            return True
    return False


def calculate_score(board, called_numbers, last_called_number):
    '''Function to calculate the score of the given board'''
    score = 0
    for row in board:
        for number in row:
            if not called_numbers[number]:
                score += number
    return score * last_called_number


if __name__ == "__main__":
    main()
