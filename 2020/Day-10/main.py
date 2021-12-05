def main():
  adaptersList = open(input("\nInput file: "), 'r').read().split("\n")

  if adaptersList[len(adaptersList) - 1] == '':
    adaptersList.pop()

  adaptersList = list(map(int, adaptersList))

  adaptersList.append(0)
  adaptersList.sort()
  adaptersList.append(adaptersList[-1] + 3)

  diferencesList = ratingDiferences(adaptersList)

  print("\nThe result is:", diferencesList.count(1) * diferencesList.count(3))
  print("\nThe total number of distinct arrangements for the adapters is:",
        distinctArrangements(diferencesList))


def ratingDiferences(adaptersList):
  diferencesList = list()

  for adaptersListIndex in range(1, len(adaptersList)):
    diferencesList.append(adaptersList[adaptersListIndex] -
                          adaptersList[adaptersListIndex - 1])

  return diferencesList


def distinctArrangements(diferencesList):
  diferencesList = "".join(map(str, diferencesList)).split("3")
  totalCombinations = 1

  for adapt in diferencesList:
    numberOfAdapter = len(adapt)

    if numberOfAdapter > 1:
      totalCombinations *= combination(numberOfAdapter - 1)

  return totalCombinations


def combination(numberOfAdapter):
  if numberOfAdapter < 3:
    return 2**numberOfAdapter

  elif numberOfAdapter == 3:
    return (2**numberOfAdapter) - 1

  else:
    return combination(numberOfAdapter - 1) - 1


main()
