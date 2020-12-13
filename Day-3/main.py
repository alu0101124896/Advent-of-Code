file_name = input("\nInput file: ")

f = open(file_name, 'r')
trees_map = f.read().split("\n")

if trees_map[len(trees_map) - 1] == '':
  trees_map.pop()

print("\nSlope:")
horizontal_displacement = int(input("Horizontal displacement: "))
vertical_displacement = int(input("Vertical displacement: "))

print("\nInitial position:")
x_coordinate = int(input("X coordinate: "))
y_coordinate = int(input("Y coordinate: "))


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


number_of_trees = slideDownhill(trees_map, x_coordinate, y_coordinate,
                                horizontal_displacement, vertical_displacement)

print("\nNumber of trees encountered:", number_of_trees)
