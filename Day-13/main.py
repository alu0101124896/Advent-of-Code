def main():
  data = open(input("\nInput file: "), 'r').read().split("\n")

  if data[len(data) - 1] == '':
    data.pop()

  earliestTimestamp = int(data.pop(0))

  busIDs = data[0].split(',')

  earliestBusInfo = earliestBus(earliestTimestamp, busIDs)

  busID = earliestBusInfo.get("busID")
  waitingTime = earliestBusInfo.get("nearestTimestamp") - earliestTimestamp

  print("\nThe earliest bus ID multiplied by the waiting time is:",
        busID * waitingTime)


def earliestBus(earliestTimestamp, busIDs):
  busesInfo = list()

  for busID in busIDs:
    if busID != 'x':
      busesInfo.append({
          "busID":
          int(busID),
          "nearestTimestamp":
          nearestTimestamp(earliestTimestamp, int(busID))
      })

  busesInfo.sort(key=lambda bus: bus.get("nearestTimestamp"))

  return busesInfo[0]


def nearestTimestamp(earliestTimestamp, busID):
  nearestTimestamp = busID
  while True:
    if nearestTimestamp >= earliestTimestamp:
      return nearestTimestamp
    else:
      nearestTimestamp += busID


main()
