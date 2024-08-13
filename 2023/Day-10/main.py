"""
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: August 2024
Description: This program implements my solution to the Advent of Code challenge.
"""


def main():
    """Main function to resolve the challenge."""

    pipe_map, starting_pos = parse_data()

    pipe_loop_length = get_pipe_loop_length(pipe_map, starting_pos)

    print(
        "The number of steps along the loop to be in the farthest point "
        + "from the starting position is: ",
        pipe_loop_length // 2,
    )


def parse_data() -> tuple[list[list[str]], tuple[int, int]]:
    """Function to parse the input data of the challenge."""

    input_file = input("\nInput file: ")

    with open(input_file, "r", encoding="utf-8") as infile:
        rawdata = infile.read().split("\n")

    if rawdata[-1] == "":
        rawdata.pop(-1)

    pipe_map = []
    starting_pos = None

    for row, line in enumerate(rawdata):
        pipe_map.append(list(line))

        try:
            col = line.index("S")
            starting_pos = (row, col)

        except ValueError:
            pass

    return pipe_map, starting_pos


def get_pipe_loop_length(
    pipe_map: list[list[str]],
    starting_pos: tuple[int, int],
) -> int:
    """Function to calculate the length of the pipe loop."""

    current_row, current_col = starting_pos

    if pipe_map[current_row - 1][current_col] in ["|", "7", "F"]:
        current_row -= 1
    elif pipe_map[current_row + 1][current_col] in ["|", "L", "J"]:
        current_row += 1
    elif pipe_map[current_row][current_col - 1] in ["-", "L", "F"]:
        current_col -= 1
    elif pipe_map[current_row][current_col + 1] in ["-", "J", "7"]:
        current_col += 1
    else:
        print(starting_pos)
        raise ValueError("Starting point is not connected to the pipe loop.")

    pipe_loop_length = 1
    previous_row, previous_col = starting_pos

    while (current_pipe_segment := pipe_map[current_row][current_col]) != "S":
        connections = []
        if current_pipe_segment in ["|", "L", "J"]:
            connections.append("UP")
        if current_pipe_segment in ["|", "7", "F"]:
            connections.append("DOWN")
        if current_pipe_segment in ["-", "J", "7"]:
            connections.append("LEFT")
        if current_pipe_segment in ["-", "L", "F"]:
            connections.append("RIGHT")

        for connection in connections:
            row_displacement, col_displacement = 0, 0
            if connection == "UP":
                row_displacement = -1
            elif connection == "DOWN":
                row_displacement = 1
            elif connection == "LEFT":
                col_displacement = -1
            elif connection == "RIGHT":
                col_displacement = 1

            if (previous_row == current_row + row_displacement) and (
                previous_col == current_col + col_displacement
            ):
                continue

            else:
                previous_row, previous_col = current_row, current_col
                current_row += row_displacement
                current_col += col_displacement
                break

        else:
            raise ValueError("Pipe is not closed in a loop.")

        pipe_loop_length += 1

    return pipe_loop_length


if __name__ == "__main__":
    main()
