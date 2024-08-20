"""
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: August 2024
Description: This program implements my solution to the Advent of Code challenge.
"""


def main():
    """Main function to resolve the challenge."""

    pipe_map, starting_pos = parse_data()

    # Part one

    pipe_loop_length = get_pipe_loop_length(pipe_map, starting_pos)

    print(
        "The number of steps along the loop to be in the farthest point "
        + "from the starting position is:",
        pipe_loop_length // 2,
    )

    # Part two

    pipe_loop_enclosed_tiles = get_pipe_loop_enclosed_tiles(pipe_map)

    print("The number of tiles enclosed by the pipe loop is:", pipe_loop_enclosed_tiles)


def parse_data() -> tuple[list[list[dict]], tuple[int, int]]:
    """Function to parse the input data of the challenge."""

    input_file = input("\nInput file: ")

    with open(input_file, "r", encoding="utf-8") as infile:
        rawdata = infile.read().split("\n")

    if rawdata[-1] == "":
        rawdata.pop(-1)

    pipe_map = []
    starting_row, starting_col = (None, None)

    for row, map_line in enumerate(rawdata):
        current_map_line = []

        for col, map_tile in enumerate(map_line):

            if map_tile == "S":
                starting_row, starting_col = (row, col)

            connections = []
            if map_tile in ["|", "L", "J"]:
                connections.append("UP")
            if map_tile in ["|", "7", "F"]:
                connections.append("DOWN")
            if map_tile in ["-", "J", "7"]:
                connections.append("LEFT")
            if map_tile in ["-", "L", "F"]:
                connections.append("RIGHT")

            current_map_line.append(
                {
                    "type": map_tile,
                    "connections": connections,
                    "is_pipe_loop": False,
                }
            )

        pipe_map.append(current_map_line)

    starting_pos_connections = []
    if "DOWN" in pipe_map[starting_row - 1][starting_col]["connections"]:
        starting_pos_connections.append("UP")
    if "UP" in pipe_map[starting_row + 1][starting_col]["connections"]:
        starting_pos_connections.append("DOWN")
    if "RIGHT" in pipe_map[starting_row][starting_col - 1]["connections"]:
        starting_pos_connections.append("LEFT")
    if "LEFT" in pipe_map[starting_row][starting_col + 1]["connections"]:
        starting_pos_connections.append("RIGHT")
    pipe_map[starting_row][starting_col]["connections"] = starting_pos_connections

    return pipe_map, (starting_row, starting_col)


def get_pipe_loop_length(
    pipe_map: list[list[dict]],
    starting_pos: tuple[int, int],
) -> int:
    """Function to calculate the length of the pipe loop."""

    pipe_loop_length = 0
    current_row, current_col = starting_pos
    previous_row, previous_col = starting_pos

    while True:
        current_pipe_segment = pipe_map[current_row][current_col]

        for connection in current_pipe_segment["connections"]:
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
                continue  # Don't go back in your own steps

            else:
                previous_row, previous_col = current_row, current_col
                current_row += row_displacement
                current_col += col_displacement
                break

        else:
            raise ValueError("Pipe is not closed in a loop.")

        pipe_map[previous_row][previous_col]["is_pipe_loop"] = True
        pipe_loop_length += 1

        if pipe_map[current_row][current_col]["type"] == "S":
            break

    return pipe_loop_length


def get_pipe_loop_enclosed_tiles(pipe_map: list[list[dict]]) -> int:
    """Function to count the number of tiles enclosed by the pipe loop."""

    pipe_loop_enclosed_tiles = 0
    current_pipe_segment_connections = []

    for map_line in pipe_map:
        tile_inside_pipe_loop = False

        for map_tile in map_line:
            if not map_tile["is_pipe_loop"]:
                if tile_inside_pipe_loop:
                    pipe_loop_enclosed_tiles += 1

                continue

            current_pipe_segment_connections.extend(map_tile["connections"])

            if (
                "UP" in current_pipe_segment_connections
                and "DOWN" in current_pipe_segment_connections
            ):
                tile_inside_pipe_loop = not tile_inside_pipe_loop

            if (
                current_pipe_segment_connections.count("UP")
                + current_pipe_segment_connections.count("DOWN")
            ) == 2:
                current_pipe_segment_connections.clear()

        if tile_inside_pipe_loop:
            raise ValueError("weird in line", map_line)

    return pipe_loop_enclosed_tiles


if __name__ == "__main__":
    main()
