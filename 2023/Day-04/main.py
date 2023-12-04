"""
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: December 2023
Description: This program implements my solution to the Advent of Code challenge.
"""


def main():
    """Main function to resolve the challenge."""

    scratchcards_info = parse_data()

    # Part 1

    scratchcards_values = [
        get_scratchcard_value(scratchcard)
        for scratchcard in scratchcards_info.values()
    ]

    print(f"The Elf's pile of scratchcards is worth {sum(scratchcards_values)} points")

    # Part 2

    process_scratchcards(scratchcards_info)

    print(
        "After processing the Elf's pile of scratchcards, it is composed of",
        count_scratchcards(scratchcards_info),
        "scratchcards"
    )


def parse_data():
    """Function to parse the input data of the challenge."""

    input_file = input("\nInput file: ")

    with open(input_file, 'r', encoding="utf-8") as infile:
        rawdata = infile.read().split("\n")

    if rawdata[-1] == "":
        rawdata.pop()

    scratchcards_info = {
        int(card.split(": ")[0].split()[1]): {
            "instances": 1,
            "winning_numbers": [
                int(number)
                for number in card.split(": ")[1].split(" | ")[0].split()
            ],
            "card_numbers": [
                int(number)
                for number in card.split(": ")[1].split(" | ")[1].split()
            ],
        }
        for card in rawdata
    }

    return scratchcards_info


def get_scratchcard_value(scratchcard):
    """Function to get the value of a given scratchcard. For the first prized number,
    the value is 1, then each prized number doubles the value of the scratchcard; that
    is the same as two to the power of one less than the number of prized numbers."""

    prized_numbers = get_prized_numbers(scratchcard)

    if len(prized_numbers) == 0:
        return 0

    else:
        return 2 ** (len(prized_numbers) - 1)


def get_prized_numbers(scratchcard):
    """Function to get the prized numbers of a given scratchcard. The prized numbers are
    the numbers that appears in both sets of numbers of the given scratchcard."""

    return [
        number
        for number in scratchcard["card_numbers"]
        if number in scratchcard["winning_numbers"]
    ]


def process_scratchcards(scratchcards_info):
    """Function to process the scratchcards. The prize of a scratchcard is as many
    scratchcards as prized numbers it has. The new scratchcards received are copies of
    the following scratchcards from the original pile."""

    for current_index, scratchcard_info in scratchcards_info.items():
        for idx in range(
                current_index + 1,
                current_index + len(get_prized_numbers(scratchcard_info)) + 1
        ):
            scratchcards_info[idx]["instances"] += scratchcards_info[current_index]["instances"]


def count_scratchcards(scratchcards_info):
    """Function to count the total number of scratchcards in the given pile."""

    return sum(
        scratchcard_info["instances"]
        for scratchcard_info in scratchcards_info.values()
    )


if __name__ == "__main__":
    main()
