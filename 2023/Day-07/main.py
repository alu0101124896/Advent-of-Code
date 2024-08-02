"""
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: August 2024
Description: This program implements my solution to the Advent of Code challenge.
"""


def main():
    """Main function to resolve the challenge."""

    hands_data, jokerized_hands_data = parse_data()

    # Part 1

    hands_data.sort(key=lambda hand_data: hand_data["value"])

    total_winnings = get_total_winnings(hands_data)

    print("The solution", total_winnings)

    # Part 2

    jokerized_hands_data.sort(key=lambda hand_data: hand_data["value"])

    total_jokerized_winnings = get_total_winnings(jokerized_hands_data)

    print("The solution", total_jokerized_winnings)


def parse_data() -> tuple[list[dict], list[dict]]:
    """Function to parse the input data of the challenge."""

    input_file = input("\nInput file: ")

    with open(input_file, "r", encoding="utf-8") as infile:
        rawdata = infile.read().split("\n")

    if rawdata[-1] == "":
        rawdata.pop()

    hands_data = []
    jokerized_hands_data = []
    for hand_raw_data in rawdata:
        cards, bid = hand_raw_data.split()

        hands_data.append(
            {
                "cards": cards,
                "bid": int(bid),
                "value": get_hand_value([get_card_value(card) for card in cards]),
            }
        )

        jokerized_hands_data.append(
            {
                "cards": cards,
                "bid": int(bid),
                "value": get_hand_value(
                    [get_card_value(card, jokerized=True) for card in cards],
                    jokerized=True,
                ),
            }
        )

    return hands_data, jokerized_hands_data


def get_card_value(card: str, jokerized: bool = False) -> int:
    """Function to get the value of the given card."""

    if jokerized:
        value_order = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]
    else:
        value_order = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

    return value_order.index(card)


def get_hand_value(cards_values: list[int], jokerized: bool = False) -> int:
    """Function to get the value of the given hand."""

    hand_value = 0
    jokers = []
    cards_values.reverse()
    for card_id, card_value in enumerate(cards_values):
        hand_value += card_value * (10 ** (card_id * 2))

        if jokerized and card_value == 0:  # Value of a Joker
            jokers.append(card_id)

    jokers.reverse()
    for joker in jokers:
        cards_values.pop(joker)

    cards_count = [cards_values.count(card) for card in set(cards_values)]

    if len(cards_count) > 0:
        cards_count[cards_count.index(max(cards_count))] += len(jokers)
    else:
        cards_count.append(5)

    if 5 in cards_count:
        type_value = 6  # Five of a kind
    elif 4 in cards_count:
        type_value = 5  # Four of a kind
    elif 3 in cards_count and 2 in cards_count:
        type_value = 4  # Full house
    elif 3 in cards_count:
        type_value = 3  # Three of a kind
    elif cards_count.count(2) == 2:
        type_value = 2  # Two pair
    elif 2 in cards_count:
        type_value = 1  # One pair
    else:
        type_value = 0  # High card

    hand_value += type_value * (10**10)

    return hand_value


def get_total_winnings(hands_data):
    """Function to calculate the total winnings of a Camel Cards game's play."""

    total_winnings = 0
    for hand_id, hand_data in enumerate(hands_data):
        total_winnings += (hand_id + 1) * hand_data["bid"]

    return total_winnings


if __name__ == "__main__":
    main()
