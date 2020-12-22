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


def ratingDiferences(adaptersList):
  diferencesList = list()
  for adaptersListIndex in range(1, len(adaptersList)):
    diferencesList.append(adaptersList[adaptersListIndex] -
                          adaptersList[adaptersListIndex - 1])
  return diferencesList


main()
