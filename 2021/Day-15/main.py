'''
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: December 2021
Description: This program implemets my solution to the Advent of Code challenge.
'''

import math
import heapq


class Point:
    '''Class to represent a point on the map with it's coordinates, it's risk,
    and the total risk of the path from the starting point.'''
    x_coord: int
    y_coord: int
    risk: int
    total_risk: int
    visited: bool

    def __init__(self,
                 x_coord: int = None,
                 y_coord: int = None,
                 risk: int = None) -> None:
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.risk = risk
        self.total_risk = math.inf
        self.visited = False

    def __eq__(self, __o: object) -> bool:
        return self.total_risk == __o.total_risk

    def __lt__(self, __o: object) -> bool:
        return self.total_risk < __o.total_risk

    def __le__(self, __o: object) -> bool:
        return self.total_risk <= __o.total_risk

    def __gt__(self, __o: object) -> bool:
        return self.total_risk > __o.total_risk

    def __ge__(self, __o: object) -> bool:
        return self.total_risk >= __o.total_risk

    def __hash__(self) -> int:
        return hash(repr(self))


def main():
    '''Main function to resolve the challenge.'''
    risk_map = parse_data()

    total_risk = lowest_risk_path(risk_map)

    print("\nThe total risk of the lowest risk path is:", total_risk)


def parse_data() -> list[list[Point]]:
    '''Funcion to parse the input data of the challenge.'''
    input_file = input("\nInput file: ")
    data = open(input_file, 'r').read().split("\n")

    if data[len(data) - 1] == '':
        data.pop()

    return [[
        Point(line_index, risk_index, int(risk))
        for risk_index, risk in enumerate(line)
    ] for line_index, line in enumerate(data)]


def lowest_risk_path(risk_map: list[list[Point]]) -> int:
    '''Function to get the total risk of the path with lowest risk.'''
    starting_point = risk_map[0][0]
    starting_point.total_risk = 0

    unvisited_points: list[Point] = []
    heapq.heappush(unvisited_points, starting_point)

    while len(unvisited_points) != 0:
        current_point = heapq.heappop(unvisited_points)
        current_point.visited = True

        for neighbor in get_neighbors(current_point, risk_map):
            if not neighbor.visited:
                alternative_path_total_risk = (current_point.total_risk +
                                               neighbor.risk)
                if alternative_path_total_risk < neighbor.total_risk:
                    neighbor.total_risk = alternative_path_total_risk
                    heapq.heappush(unvisited_points, neighbor)

        heapq.heapify(unvisited_points)

    return risk_map[len(risk_map) - 1][len(risk_map[0]) - 1].total_risk


def get_neighbors(point: Point, risk_map: list[list[Point]]) -> list[Point]:
    '''Function to get the neighbor points.'''
    neighbors = set()
    if point.x_coord - 1 >= 0:
        neighbors.add(risk_map[point.x_coord - 1][point.y_coord])

    if point.y_coord - 1 >= 0:
        neighbors.add(risk_map[point.x_coord][point.y_coord - 1])

    if point.x_coord + 1 <= len(risk_map) - 1:
        neighbors.add(risk_map[point.x_coord + 1][point.y_coord])

    if point.y_coord + 1 <= len(risk_map[0]) - 1:
        neighbors.add(risk_map[point.x_coord][point.y_coord + 1])

    return neighbors


if __name__ == "__main__":
    main()
