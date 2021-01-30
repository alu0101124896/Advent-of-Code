def main():
  program, maskLength = parseData()

  totalSum = getDockingParam(program, maskLength)

  print("\nThe sum of all values left in memory after the program execution",
        "is:", totalSum)


def parseData():
  inputFile = input("\nInput file: ")
  data = open(inputFile, 'r').read().split("\n")

  if data[len(data) - 1] == '':
    data.pop()

  program = []

  for instruction in data:
    operation, value = list(instruction.split(" = ", 1))

    address = 0
    if operation != "mask":
      operation, address = operation.strip("]").split("[")

      address = int(address)
      value = int(value)

    program.append([operation, address, value])

  maskLength = len(program[0][2])

  return program, maskLength


def getDockingParam(program, maskLength):
  memoryAddresses = dict()
  currentMask = "X" * maskLength

  for instruction in program:
    if instruction[0] == "mask":
      currentMask = instruction[2]

    else:
      result = ""
      currentValue = format(int(instruction[2]), 'b').zfill(maskLength)

      for position in range(maskLength):
        if currentMask[position] == "X":
          result += currentValue[position]

        else:
          result += currentMask[position]

      memoryAddresses.update({instruction[1]: result})

  totalSum = 0
  for memoryAddress in memoryAddresses.items():
    totalSum += int(memoryAddress[1], 2)

  return totalSum


main()
