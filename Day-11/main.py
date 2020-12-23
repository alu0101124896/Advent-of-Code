def main():
  seatLayout = open(input("\nInput file: "), 'r').read().split("\n")

  if seatLayout[len(seatLayout) - 1] == '':
    seatLayout.pop()

  seatLayout = list(map(lambda row: list(row), seatLayout))

  filledSeatLayout = list()
  for row in seatLayout:
    filledSeatLayout.append(row[:])

  fillFerry(filledSeatLayout)
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


main()
