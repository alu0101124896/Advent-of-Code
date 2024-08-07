"""
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: August 2024
Description: This program implements my solution to the Advent of Code challenge.
"""


def main():
    """Main function to resolve the challenge."""

    seeds_ids, maps_data, inverse_maps_data = parse_data()

    # Part 1

    seed_locations = [seed_location(seed_id, maps_data) for seed_id in seeds_ids]

    print(
        "The lowest location number of any of the initial seed numbers is",
        min(seed_locations),
    )

    # Part 2

    seeds_ranges = [
        range(range_start, (range_start + range_length))
        for range_start, range_length in zip(seeds_ids[:-1:2], seeds_ids[1::2])
    ]

    current_seed_location = 0
    lowest_seed_location = None

    while lowest_seed_location is None:
        current_seed_id = seed_location_inverted(
            current_seed_location,
            inverse_maps_data,
        )

        for seed_range in seeds_ranges:
            if current_seed_id in seed_range:
                lowest_seed_location = current_seed_location
                break

        current_seed_location += 1

    print(
        "The lowest location number of any of the initial seed ranges is",
        lowest_seed_location,
    )


def parse_data():
    """Function to parse the input data of the challenge."""

    input_file = input("\nInput file: ")

    with open(input_file, "r", encoding="utf-8") as infile:
        rawdata = infile.read()

    data_groups = rawdata.split("\n\n")

    seeds_ids = [int(seed_id) for seed_id in data_groups[0].split(": ")[1].split()]

    maps_data = {}
    inverse_maps_data = {}
    for map_data in data_groups[1:]:
        map_name, map_info = map_data.split(" map:\n")
        map_source, map_destination = map_name.split("-to-")

        map_mappings = [
            [int(mapping_number) for mapping_number in mapping_line.split(" ")]
            for mapping_line in map_info.split("\n")
            if mapping_line != ""
        ]

        maps_data.update(
            {
                map_source: {
                    "map_destination": map_destination,
                    "map_mappings": map_mappings,
                }
            }
        )

        inverse_maps_data.update(
            {
                map_destination: {
                    "map_source": map_source,
                    "map_mappings": map_mappings,
                }
            }
        )

    return seeds_ids, maps_data, inverse_maps_data


def seed_location(seed_id, maps_data):
    """Function to get the required location id for the given seed id."""

    current_id = seed_id
    current_id_name = "seed"

    while current_id_name != "location":
        current_map_data = maps_data[current_id_name]

        for (
            destination_start,
            source_start,
            mapping_range,
        ) in current_map_data["map_mappings"]:
            source_end = source_start + mapping_range

            if source_start <= current_id < source_end:
                id_offset = current_id - source_start
                current_id = destination_start + id_offset
                break

        current_id_name = current_map_data["map_destination"]

    return current_id


def seed_location_inverted(location_id, inverse_maps_data):
    """Function to get the corresponding seed id for the given location id."""

    current_id = location_id
    current_id_name = "location"

    while current_id_name != "seed":
        current_map_data = inverse_maps_data[current_id_name]

        for (
            destination_start,
            source_start,
            mapping_range,
        ) in current_map_data["map_mappings"]:
            destination_end = destination_start + mapping_range

            if destination_start <= current_id < destination_end:
                id_offset = current_id - destination_start
                current_id = source_start + id_offset
                break

        current_id_name = current_map_data["map_source"]

    return current_id


if __name__ == "__main__":
    main()
