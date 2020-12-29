def main():
  instructions = open(input("\nInput file: "), 'r').read().split("\n")

  if instructions[len(instructions) - 1] == '':
    instructions.pop()

  instructions = list(
      map(lambda instruction: (instruction[0], int(instruction[1:])),
          instructions))

  try:
    origin = [0, 0]
    destination = follow(instructions, origin)
    print(manhattanDistance(origin, destination))
  except Exception as error:
    print(error.args[0])


def follow(instructions, origin):
  position = origin[:]
  facingDirection = 0

  for instruction in instructions:
    action = instruction[0]
    value = instruction[1]

    if action == 'E':
      position = move(position, value, 0)
    elif action == 'N':
      position = move(position, value, 90)
    elif action == 'W':
      position = move(position, value, 180)
    elif action == 'S':
      position = move(position, value, 270)

    elif action == 'L':
      facingDirection = (facingDirection + value) % 360
    elif action == 'R':
      facingDirection = (facingDirection - value) % 360

    elif action == 'F':
      position = move(position, value, facingDirection)

    else:
      raise Exception("\nError: Unknown action.")

  return position


def move(position, value, direction):
  if direction == 0:
    position[0] += value
  elif direction == 90:
    position[1] += value

  elif direction == 180:
    position[0] -= value
  elif direction == 270:
    position[1] -= value

  else:
    raise Exception("\nError: Unknown direction.")

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
