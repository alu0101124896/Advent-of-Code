def main():
  startingNumbers = parseData()

  finalTurn = 2020
  finalNumber = playGame(startingNumbers, finalTurn)

  print(f"\nThe {finalTurn}th number spoken is {finalNumber}")


def parseData():
  inputFile = input("\nInput file: ")
  data = open(inputFile, 'r').read().split("\n")[0].split(",")

  startingNumbers = list(map(lambda number: int(number), data))

  return startingNumbers


def playGame(startingNumbers, finalTurn):
  currentTurn = 1

  numbersHistory = dict()
  for number in startingNumbers:
    numbersHistory.update({
      number: {
        "ultimatePosition": currentTurn,
        "penultimatePosition": None
      }
    })
    currentTurn += 1

  lastNumber = startingNumbers[-1]

  while (currentTurn <= finalTurn):
    if numbersHistory.get(lastNumber).get("penultimatePosition") is None:
      lastNumber = 0
    else:
      lastNumber = (currentTurn - 1) - \
        numbersHistory.get(lastNumber).get("penultimatePosition")

    if lastNumber in numbersHistory:
      numbersHistory.update({
        lastNumber: {
          "ultimatePosition": currentTurn,
          "penultimatePosition":
            numbersHistory.get(lastNumber).get("ultimatePosition")
        }
      })
    else:
      numbersHistory.update({
        lastNumber: {
          "ultimatePosition": currentTurn,
          "penultimatePosition": None
        }
      })
    currentTurn += 1

  return lastNumber


main()
