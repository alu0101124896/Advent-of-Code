import math

boardingCodes = open(input("\nInput file: "), 'r').read().split("\n")

if boardingCodes[len(boardingCodes) - 1] == "":
  boardingCodes.pop()


def getRow(boardingCode):
  firstRow = 0
  lastRow = 127
  return getRowBinarySearch(boardingCode, firstRow, lastRow)


def getRowBinarySearch(boardingCode, lowestIndex, highestIndex):
  if len(boardingCode) == 0:
    if lowestIndex == highestIndex:
      return lowestIndex
    else:
      print("Error: indices diferentes.")
      return -1
  else:
    if boardingCode[0] == "F":
      return getRowBinarySearch(
          boardingCode[1:], lowestIndex, lowestIndex + math.floor(
              (highestIndex - lowestIndex) / 2))
    elif boardingCode[0] == "B":
      return getRowBinarySearch(
          boardingCode[1:], lowestIndex + math.ceil(
              (highestIndex - lowestIndex) / 2), highestIndex)
    else:
      print("Error: Código inválido.")
      return -1


def getColumt(boardingCode):
  firstColumn = 0
  lastColumn = 7
  return getColumnBinarySearch(boardingCode, firstColumn, lastColumn)


def getColumnBinarySearch(boardingCode, lowestIndex, highestIndex):
  if len(boardingCode) == 0:
    if lowestIndex == highestIndex:
      return lowestIndex
    else:
      print("Error: indices diferentes.")
      return -1
  else:
    if boardingCode[0] == "L":
      return getColumnBinarySearch(
          boardingCode[1:], lowestIndex, lowestIndex + math.floor(
              (highestIndex - lowestIndex) / 2))
    elif boardingCode[0] == "R":
      return getColumnBinarySearch(
          boardingCode[1:], lowestIndex + math.ceil(
              (highestIndex - lowestIndex) / 2), highestIndex)
    else:
      print("Error: Código inválido.")
      return -1


boardingCodes = list(
    map(
        lambda boardingCode: dict({
            "Code": boardingCode,
            "Row": getRow(boardingCode[:7]),
            "Column": getColumt(boardingCode[-3:])
        }), boardingCodes))

for currentBoardingCode in boardingCodes:
  currentBoardingCode.update({
      "Seat ID":
          currentBoardingCode.get("Row") * 8 + currentBoardingCode.get("Column")
  })

boardingCodes.sort(
    reverse=True,
    key=lambda currentBoardingCode: currentBoardingCode.get("Seat ID"))

print("\nThe highest seat ID is:", boardingCodes[0].get("Seat ID"))

for actualSeatID in range(boardingCodes[-1].get("Seat ID"),
                          boardingCodes[0].get("Seat ID")):
  if actualSeatID not in list(
      map(lambda boardingCode: boardingCode.get("Seat ID"), boardingCodes)):
    print("\nMy seat ID is:", actualSeatID)
