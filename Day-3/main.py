import numpy

file_name = input("\nInput file: ")

f = open(file_name, 'r')
trees_map = f.read().split("\n")

if trees_map[len(trees_map) - 1] == '':
  trees_map.pop()

# print("\nSlope:")
# horizontal_displacement = int(input("Horizontal displacement: "))
# vertical_displacement = int(input("Vertical displacement: "))
slopes_list = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

# print("\nInitial position:")
# x_coordinate = int(input("X coordinate: "))
# y_coordinate = int(input("Y coordinate: "))
x_coordinate = 0
y_coordinate = 0


def slideDownhill(trees_map,
                  x_coordinate,
                  y_coordinate,
                  horizontal_displacement,
                  vertical_displacement,
                  number_of_trees=0):
  x_coordinate += horizontal_displacement
  y_coordinate += vertical_displacement
  if y_coordinate >= len(trees_map):
    return number_of_trees
  else:
    if x_coordinate >= len(trees_map[y_coordinate]):
      x_coordinate %= len(trees_map[y_coordinate])
    if trees_map[y_coordinate][x_coordinate] == "#":
      number_of_trees += 1
    return slideDownhill(trees_map, x_coordinate, y_coordinate,
                         horizontal_displacement, vertical_displacement,
                         number_of_trees)


def slideDownhillForEachSlope(slope):
  return slideDownhill(trees_map, x_coordinate, y_coordinate, slope[0],
                       slope[1])


# number_of_trees = slideDownhill(trees_map, x_coordinate, y_coordinate,
#                                 horizontal_displacement, vertical_displacement)
number_of_trees_list = list(map(slideDownhillForEachSlope, slopes_list))

# print("\nNumber of trees encountered:", number_of_trees)
print("\nMultiplication of all trees encountered on every slope checked:",
      numpy.prod(number_of_trees_list))
