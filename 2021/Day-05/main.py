'''
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: December 2021
Description: This program implemets my solution to the Advent of Code challenge.
'''


def main():
    '''Main function to resolve the challenge.'''
    hydrotermal_vent_lines = parse_data()

    result = get_dangerous_areas(hydrotermal_vent_lines)

    print("\nThe number of dangerous areas is:", result)


def parse_data():
    '''Funcion to parse the input data of the challenge.'''
    input_file = input("\nInput file: ")
    data = open(input_file, 'r').read().split("\n")

    if data[len(data) - 1] == '':
        data.pop()

    lines = list()
    for line in data:
        start, end = line.split(" -> ")

        x_start, y_start = start.split(",")
        x_end, y_end = end.split(",")

        lines.append({
            "x_start": int(x_start),
            "y_start": int(y_start),
            "x_end": int(x_end),
            "y_end": int(y_end),
        })

    return lines


def get_dangerous_areas(hydrotermal_vent_lines):
    '''Function to get the number of points where at least two lines overlap.'''
    dangerous_areas = dict()
    for line in hydrotermal_vent_lines:
        if line["x_start"] < line["x_end"]:
            x_slope_inc = 1
        elif line["x_start"] == line["x_end"]:
            x_slope_inc = 0
        else:
            x_slope_inc = -1

        if line["y_start"] < line["y_end"]:
            y_slope_inc = 1
        elif line["y_start"] == line["y_end"]:
            y_slope_inc = 0
        else:
            y_slope_inc = -1

        x_index = line["x_start"]
        y_index = line["y_start"]
        while True:
            current_point = f'{x_index},{y_index}'
            dangerous_areas.update(
                {current_point: dangerous_areas.get(current_point, 0) + 1})
            if x_index == line["x_end"] and y_index == line["y_end"]:
                break
            else:
                x_index += x_slope_inc
                y_index += y_slope_inc


    return sum(value >= 2 for value in dangerous_areas.values())


if __name__ == "__main__":
    main()
