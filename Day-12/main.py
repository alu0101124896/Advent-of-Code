def main():
  instructions = open(input("\nInput file: "), 'r').read().split("\n")

  if instructions[len(instructions) - 1] == '':
    instructions.pop()

  instructions = list(
      map(lambda instruction: (instruction[0], int(instruction[1:])),
          instructions))

  try:
    origin = [0, 0]
    # destination = follow(instructions, origin)
    destination = followV2(instructions, origin)
    print(manhattanDistance(origin, destination))
  except Exception as error:
    print(error.args[0])


def follow(instructions, origin):
  position = origin[:]
  facingDirection = 0

  for instruction in instructions:
    action = instruction[0]
    units = instruction[1]

    if action == 'E':
      position = move(position, units, 0)
    elif action == 'N':
      position = move(position, units, 90)
    elif action == 'W':
      position = move(position, units, 180)
    elif action == 'S':
      position = move(position, units, 270)

    elif action == 'L':
      facingDirection = (facingDirection + units) % 360
    elif action == 'R':
      facingDirection = (facingDirection - units) % 360

    elif action == 'F':
      position = move(position, units, facingDirection)

    else:
      raise Exception("\nError: Unknown action.")

  return position


def followV2(instructions, origin):
  shipPosition = origin[:]
  waypointPosition = origin[:]

  waypointPosition = move(waypointPosition, 10, 0)
  waypointPosition = move(waypointPosition, 1, 90)

  for instruction in instructions:
    action = instruction[0]
    units = instruction[1]

    if action == 'E':
      waypointPosition = move(waypointPosition, units, 0)
    elif action == 'N':
      waypointPosition = move(waypointPosition, units, 90)
    elif action == 'W':
      waypointPosition = move(waypointPosition, units, 180)
    elif action == 'S':
      waypointPosition = move(waypointPosition, units, 270)

    elif action == 'L':
      waypointPosition = rotate(waypointPosition, units, False)
    elif action == 'R':
      waypointPosition = rotate(waypointPosition, units, True)

    elif action == 'F':
      shipPosition = move(shipPosition, waypointPosition[0] * units, 0)
      shipPosition = move(shipPosition, waypointPosition[1] * units, 90)

    else:
      raise Exception("\nError: Unknown action.")

  return shipPosition


def move(position, units, direction):
  if direction == 0:
    position[0] += units
  elif direction == 90:
    position[1] += units

  elif direction == 180:
    position[0] -= units
  elif direction == 270:
    position[1] -= units

  else:
    raise Exception("\nError: Unknown direction.")

  return position


def rotate(position, units, clockwise):
  rotations = 0
  while True:
    if clockwise:
      position[0] *= -1
    else:
      position[1] *= -1

    position[0], position[1] = position[1], position[0]

    rotations += 1
    if rotations * 90 >= units:
      break

  return position


def manhattanDistance(firstPoint, secondPoint):
  distance = 0

  if len(firstPoint) == len(secondPoint):
    for i in range(len(firstPoint)):
      distance += abs(firstPoint[i] - secondPoint[i])

  else:
    raise Exception("\nError: Diferent dimensional points.")

  return distance

main()
