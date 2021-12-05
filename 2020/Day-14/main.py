def main():
  program, maskLength = parseData()

  # totalSum = getDockingParam(program, maskLength)
  totalSum = getDockingParamV2(program, maskLength)

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
      resultValue = ""
      currentValue = format(int(instruction[2]), 'b').zfill(maskLength)

      for position in range(maskLength):
        if currentMask[position] == "X":
          resultValue += currentValue[position]

        else:
          resultValue += currentMask[position]

      memoryAddresses.update({instruction[1]: resultValue})

  totalSum = 0
  for memoryAddress in memoryAddresses.items():
    totalSum += int(memoryAddress[1], 2)

  return totalSum


def getDockingParamV2(program, maskLength):
  memoryAddresses = dict()
  currentMask = "X" * maskLength

  for instruction in program:
    if instruction[0] == "mask":
      currentMask = instruction[2]

    else:
      resultMemoryAddress = ""
      currentAddress = format(int(instruction[1]), 'b').zfill(maskLength)

      for position in range(maskLength):
        if currentMask[position] == "0":
          resultMemoryAddress += currentAddress[position]

        elif currentMask[position] == "1":
          resultMemoryAddress += "1"

        else:
          resultMemoryAddress += "X"

      memoryAddresses = saveTo(memoryAddresses, list(resultMemoryAddress),
                               instruction[2], maskLength)

  totalSum = 0
  for memoryAddress in memoryAddresses.items():
    totalSum += memoryAddress[1]

  return totalSum


def saveTo(memoryAddresses, memoryAddress, value, maskLength, charIndex=0):
  if charIndex >= maskLength:
    memoryAddress = int("".join(memoryAddress), 2)
    memoryAddresses.update({memoryAddress: value})
    return memoryAddresses

  else:
    if memoryAddress[charIndex] != "X":
      return saveTo(memoryAddresses, memoryAddress, value, maskLength,
                    charIndex + 1)

    else:
      mem0 = memoryAddress[:]
      mem0[charIndex] = "0"
      memoryAddresses = saveTo(memoryAddresses, mem0, value, maskLength,
                               charIndex + 1)

      mem1 = memoryAddress[:]
      mem1[charIndex] = "1"
      return saveTo(memoryAddresses, mem1, value, maskLength, charIndex + 1)


main()
