def main():
  seatLayout = open(input("\nInput file: "), 'r').read().split("\n")

  if seatLayout[len(seatLayout) - 1] == '':
    seatLayout.pop()

  seatLayout = list(map(lambda row: list(row), seatLayout))

  filledSeatLayout = list()
  for row in seatLayout:
    filledSeatLayout.append(row[:])

  # fillFerry(filledSeatLayout)
  fillFerryV2(filledSeatLayout)
  print("\nAt the end,", countOccupiedSeats(filledSeatLayout),
        "seats have beed occupied.")


def fillFerry(seatLayout):
  while True:
    prevSeatLayout = list()
    seatLayoutChanged = False

    for row in seatLayout:
      prevSeatLayout.append(row[:])

    for rowIndex in range(len(seatLayout)):
      for seatIndex in range(len(seatLayout[rowIndex])):
        occupiedSeatsArround = hasOccupiedSeatsArround(rowIndex, seatIndex,
                                                       prevSeatLayout)

        if seatLayout[rowIndex][seatIndex] == 'L' and not occupiedSeatsArround:
          seatLayout[rowIndex][seatIndex] = '#'
          seatLayoutChanged = True

        elif seatLayout[rowIndex][
                         seatIndex] == '#' and occupiedSeatsArround >= 4:
          seatLayout[rowIndex][seatIndex] = 'L'
          seatLayoutChanged = True

    if not seatLayoutChanged:
      break

  return seatLayout


def hasOccupiedSeatsArround(rowIndex, seatIndex, seatLayout):
  occupiedSeats = 0

  firstRow = rowIndex == 0
  lastRow = rowIndex == len(seatLayout) - 1

  firstSeat = seatIndex == 0
  lastSeat = seatIndex == len(seatLayout[rowIndex]) - 1

  if not firstRow and not firstSeat and seatLayout[rowIndex - 1][
                                                seatIndex - 1] == '#' :
    occupiedSeats += 1
  if not firstRow and seatLayout[rowIndex - 1][seatIndex] == '#' :
    occupiedSeats += 1
  if not firstRow and not lastSeat and seatLayout[rowIndex - 1][
                                                seatIndex + 1] == '#' :
    occupiedSeats += 1
  if not firstSeat and seatLayout[rowIndex][seatIndex - 1] == '#'  :
    occupiedSeats += 1
  if not lastSeat and seatLayout[rowIndex][seatIndex + 1] == '#'  :
    occupiedSeats += 1
  if not lastRow and not firstSeat and seatLayout[rowIndex + 1][
                                                seatIndex - 1] == '#'  :
    occupiedSeats += 1
  if not lastRow and seatLayout[rowIndex + 1][seatIndex] == '#'  :
    occupiedSeats += 1
  if not lastRow and not lastSeat and seatLayout[rowIndex + 1][
                                                seatIndex + 1] == '#'  :
    occupiedSeats += 1

  return occupiedSeats


def countOccupiedSeats(seatLayout):
  totalOccupiedSeats = 0

  for row in seatLayout:
    for seat in row:
      if seat == '#':
        totalOccupiedSeats += 1

  return totalOccupiedSeats


def fillFerryV2(seatLayout):
  while True:
    prevSeatLayout = list()
    seatLayoutChanged = False

    for row in seatLayout:
      prevSeatLayout.append(row[:])

    for rowIndex in range(len(seatLayout)):
      for seatIndex in range(len(seatLayout[rowIndex])):
        visualyOccupiedSeatsArround = hasVisualyOccupiedSeatsArround(
            rowIndex, seatIndex, prevSeatLayout)

        if seatLayout[rowIndex][
            seatIndex] == 'L' and not visualyOccupiedSeatsArround:
          seatLayout[rowIndex][seatIndex] = '#'
          seatLayoutChanged = True

        elif seatLayout[rowIndex][
            seatIndex] == '#' and visualyOccupiedSeatsArround >= 5:
          seatLayout[rowIndex][seatIndex] = 'L'
          seatLayoutChanged = True

    if not seatLayoutChanged:
      break

  return seatLayout


def hasVisualyOccupiedSeatsArround(rowIndex, seatIndex, seatLayout):
  occupiedSeats = 0

  upRowIndex = rowIndex
  leftSeatIndex = seatIndex
  rightSeatIndex = seatIndex

  sawnLeftUp = False
  sawnUp = False
  sawnRightUp = False

  while upRowIndex > 0:
    if not sawnLeftUp and leftSeatIndex > 0:
      if seatLayout[upRowIndex - 1][leftSeatIndex - 1] == '#':
        occupiedSeats += 1
        sawnLeftUp = True

      elif seatLayout[upRowIndex - 1][leftSeatIndex - 1] == 'L':
        sawnLeftUp = True

    if not sawnUp:
      if seatLayout[upRowIndex - 1][seatIndex] == '#':
        occupiedSeats += 1
        sawnUp = True

      elif seatLayout[upRowIndex - 1][seatIndex] == 'L':
        sawnUp = True

    if not sawnRightUp and rightSeatIndex < len(seatLayout[rowIndex]) - 1:
      if seatLayout[upRowIndex - 1][rightSeatIndex + 1] == '#':
        occupiedSeats += 1
        sawnRightUp = True

      elif seatLayout[upRowIndex - 1][rightSeatIndex + 1] == 'L':
        sawnRightUp = True

    upRowIndex -= 1
    leftSeatIndex -= 1
    rightSeatIndex += 1

  downRowIndex = rowIndex
  leftSeatIndex = seatIndex
  rightSeatIndex = seatIndex

  sawnLeftDown = False
  sawnDown = False
  sawnRightDown = False

  while downRowIndex < len(seatLayout) - 1:
    if not sawnLeftDown and leftSeatIndex > 0:
      if seatLayout[downRowIndex + 1][leftSeatIndex - 1] == '#':
        occupiedSeats += 1
        sawnLeftDown = True

      elif seatLayout[downRowIndex + 1][leftSeatIndex - 1] == 'L':
        sawnLeftDown = True

    if not sawnDown:
      if seatLayout[downRowIndex + 1][seatIndex] == '#':
        occupiedSeats += 1
        sawnDown = True

      elif seatLayout[downRowIndex + 1][seatIndex] == 'L':
        sawnDown = True

    if not sawnRightDown and rightSeatIndex < len(seatLayout[rowIndex]) - 1:
      if seatLayout[downRowIndex + 1][rightSeatIndex + 1] == '#':
        occupiedSeats += 1
        sawnRightDown = True

      elif seatLayout[downRowIndex + 1][rightSeatIndex + 1] == 'L':
        sawnRightDown = True

    downRowIndex += 1
    leftSeatIndex -= 1
    rightSeatIndex += 1

  leftSeatIndex = seatIndex

  while leftSeatIndex > 0:
    if seatLayout[rowIndex][leftSeatIndex - 1] == '#':
      occupiedSeats += 1
      break

    elif seatLayout[rowIndex][leftSeatIndex - 1] == 'L':
      break

    else:
      leftSeatIndex -= 1

  rightSeatIndex = seatIndex

  while rightSeatIndex < len(seatLayout[rowIndex]) - 1:
    if seatLayout[rowIndex][rightSeatIndex + 1] == '#':
      occupiedSeats += 1
      break

    elif seatLayout[rowIndex][rightSeatIndex + 1] == 'L':
      break

    else:
      rightSeatIndex += 1

  return occupiedSeats


main()
