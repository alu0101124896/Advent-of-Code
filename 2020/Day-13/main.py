def main():
  inputFile = input("\nInput file: ")
  data = open(inputFile, 'r').read().split("\n")

  if data[len(data) - 1] == '':
    data.pop()

  earliestTimestamp = int(data.pop(0))

  busIDs = data[0].split(',')

  earliestBusInfo = earliestBus(earliestTimestamp, busIDs)

  busID = earliestBusInfo.get("busID")
  waitingTime = earliestBusInfo.get("nearestTimestamp") - earliestTimestamp

  print("\nThe earliest bus ID multiplied by the waiting time is:",
        busID * waitingTime)

  # print(earliestOffsetsMatchingListTimestamp(busIDs))
  # print(chineseRemainderTheorem(busIDs))
  print(
      "\nThe earliest timestamp such that all of the listed bus IDs depart " +
      "at offsets matching their positions in the list is:", part_two(busIDs))


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


# Brute force algorithm
# No result given on a reasonable amount of time
def earliestOffsetsMatchingListTimestamp(busIDs):
  currentTimestamp = 0
  while True:
    if offsetsMatchesList(busIDs[1:], currentTimestamp + 1):
      return currentTimestamp
    else:
      currentTimestamp += int(busIDs[0])


def offsetsMatchesList(busIDs, currentTimestamp):
  if len(busIDs) <= 0:
    return True
  else:
    if busIDs[0] == 'x':
      return offsetsMatchesList(busIDs[1:], currentTimestamp + 1)
    else:
      if currentTimestamp % int(busIDs[0]) == 0:
        return offsetsMatchesList(busIDs[1:], currentTimestamp + 1)
      else:
        return False


# Pending for completion
# Errors with the offset
def chineseRemainderTheorem(busIDs):
  """
  x = b1 (mod n1) - 0
  x = b2 (mod n2) - 1
  ...
  x = bi (mod ni) - i
  ...
  x = bn (mod nn) - n
  """

  N = 1
  busesInfo = list()
  for offset, busID in enumerate(busIDs):
    if busID != 'x':
      N *= int(busID)
      busesInfo.append({"bi": offset, "ni": int(busID)})

  x = 0
  for bus in busesInfo:
    Ni = N // bus.get("ni")
    xi = pow(Ni, -1, bus.get("ni"))
    x += bus.get("bi") * Ni * xi

  return x % N


def linear_congruence(a, b, m):
  """
  aX = b (mod m)
  """
  if b == 0:
    return 0

  if a < 0:
    a = -a
    b = -b

  b %= m
  while a > m:
    a -= m

  return (m * linear_congruence(m, -b, a) + b) // a


# Credits to whiplashoo:
#  https://github.com/whiplashoo/advent_of_code_2020/blob/main/day13.py
#
# Not made by me from here to the end
from math import gcd


def part_two(ids):
  buses = []

  for bus in ids:
    if bus != 'x':
      buses.append(int(bus))
    else:
      buses.append('x')

  timestamp = 0
  matched_buses = [buses[0]]

  while True:
    timestamp += compute_lcm(matched_buses)

    for i, bus in enumerate(buses):
      if bus != 'x':
        if (timestamp + i) % bus == 0:
          if bus not in matched_buses:
            matched_buses.append(bus)

    if len(matched_buses) == len(buses) - buses.count('x'):
      break

  return timestamp


def compute_lcm(a):
  lcm = a[0]

  for i in a[1:]:
    lcm = lcm * i // gcd(lcm, i)

  return lcm


main()
