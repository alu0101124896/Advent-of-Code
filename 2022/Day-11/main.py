"""
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: December 2022
Description: This program implements my solution to the Advent of Code
 challenge.
"""

import re


def main():
    """Main function to resolve the challenge."""

    monkey_notes = parse_data()

    print("\nPart one:")

    play_game(monkey_notes, rounds=20)
    part_one_solution = get_monkey_business_level(monkey_notes)

    print("  The monkey business level after 20 rounds is:", part_one_solution)


def parse_data():
    """Function to parse the input data of the challenge."""

    input_file = input("\nInput file: ")

    with open(input_file, 'r', encoding="utf-8") as infile:
        raw_data = infile.read().split("\n\n")

    if raw_data[-1] == "":
        raw_data.pop()

    monkey_notes = []
    for monkey_block in raw_data:
        monkey = monkey_block.split("\n")
        monkey_notes.append({
            "items": [int(number) for number in re.findall(r"\d+", monkey[1])],
            "operation": {
                "operand": re.findall(r"[+*]", monkey[2])[0],
                "operator": re.findall(r"\d+|old", monkey[2])[1],
            },
            "test": {
                "condition": int(re.findall(r"\d+", monkey[3])[0]),
                "true_case": int(re.findall(r"\d+", monkey[4])[0]),
                "false_case": int(re.findall(r"\d+", monkey[5])[0]),
            },
            "inspections": 0,
        })

    return monkey_notes


def play_game(monkey_notes, rounds):
    """Function to let the monkeys play its game the given number of rounds."""

    for _ in range(rounds):
        for monkey in monkey_notes:
            for item_worry_level in monkey["items"]:
                new_worry_level = get_new_worry_level(
                    item_worry_level,
                    monkey["operation"]
                ) // 3

                if (new_worry_level % monkey["test"]["condition"]) == 0:
                    monkey_notes[monkey["test"]["true_case"]]["items"].append(
                        new_worry_level)
                else:
                    monkey_notes[monkey["test"]["false_case"]]["items"].append(
                        new_worry_level)

            monkey["inspections"] += len(monkey["items"])
            monkey["items"].clear()


def get_new_worry_level(item_worry_level, operation):
    """Function to get the new worry level of the given item."""

    operator = (
        item_worry_level
        if operation["operator"] == "old"
        else int(operation["operator"])
    )

    if operation["operand"] == "+":
        return item_worry_level + operator
    elif operation["operand"] == "*":
        return item_worry_level * operator

    else:
        raise ValueError("Error: unknown operand")


def get_monkey_business_level(monkey_notes):
    """Function to get the monkey business level from the given notes."""

    monkey_inspections = [monkey["inspections"] for monkey in monkey_notes]
    monkey_inspections.sort()
    return monkey_inspections[-1] * monkey_inspections[-2]


if __name__ == "__main__":
    main()
