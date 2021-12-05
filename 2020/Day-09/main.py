from functools import reduce


def main():
  encryptedData = open(input("\nInput file: "), 'r').read().split("\n")
  preambleLength = int(input("\nPreamble length: "))

  if encryptedData[len(encryptedData) - 1] == '':
    encryptedData.pop()

  encryptedData = list(map(int, encryptedData))

  try:
    securityFailure = firstSecurityFailure(encryptedData, preambleLength,
                                           preambleLength)
    print("\nThe first encryption security failure is:", securityFailure)
    print("\nThe encryption weakness is:",
          encryptionWeakness(encryptedData, securityFailure))
  except Exception as error:
    print(error.args[0])


def firstSecurityFailure(encryptedData, preambleLength, encryptedDataIndex):
  if encryptedDataIndex >= len(encryptedData):
    raise Exception("\nNo security failure detected.")

  else:
    if not validEncryption(encryptedData, encryptedDataIndex, preambleLength,
                           encryptedDataIndex - preambleLength):
      return encryptedData[encryptedDataIndex]

    else:
      return firstSecurityFailure(encryptedData, preambleLength,
                                  encryptedDataIndex + 1)


def validEncryption(encryptedData, encryptedDataIndex, preambleLength,
                    firstBufferIndex):
  if firstBufferIndex < encryptedDataIndex:
    if checkEncryptionChecksum(encryptedData, encryptedDataIndex,
                               firstBufferIndex, firstBufferIndex + 1):
      return True
    else:
      return validEncryption(encryptedData, encryptedDataIndex, preambleLength,
                             firstBufferIndex + 1)
  return False


def checkEncryptionChecksum(encryptedData, encryptedDataIndex, firstBufferIndex,
                            secondBufferIndex):
  if secondBufferIndex < encryptedDataIndex:
    if encryptedData[encryptedDataIndex] == encryptedData[
        firstBufferIndex] + encryptedData[secondBufferIndex]:
      return True
    else:
      return checkEncryptionChecksum(encryptedData, encryptedDataIndex,
                                     firstBufferIndex, secondBufferIndex + 1)
  else:
    return False


def encryptionWeakness(encryptedData, securityFailure):
  try:
    foundSet = contiguousSetRecursive(encryptedData, securityFailure)
  except RecursionError as error:
    print("\nError:", error.args[0] + ", proceeding iteratively...")
    foundSet = contiguousSetIterative(encryptedData, securityFailure)
  foundSet.sort()
  return foundSet[0] + foundSet[-1]


def contiguousSetRecursive(encryptedData, securityFailure, firstSetIndex=0):
  if firstSetIndex < len(encryptedData):
    contiguousSetFound, currentSet = checkSetSum(encryptedData, securityFailure,
                                                 firstSetIndex,
                                                 firstSetIndex + 1)
    if contiguousSetFound:
      return currentSet
    else:
      return contiguousSetRecursive(encryptedData, securityFailure,
                                    firstSetIndex + 1)
  else:
    raise Exception("\nNo encryption weakness detected.")


def checkSetSum(encryptedData, securityFailure, firstSetIndex, secondSetIndex):
  if secondSetIndex < len(encryptedData):
    currentSet = encryptedData[firstSetIndex:secondSetIndex]
    if reduce(lambda a, b: a + b, currentSet) == securityFailure:
      return True, currentSet
    else:
      return checkSetSum(encryptedData, securityFailure, firstSetIndex,
                         secondSetIndex + 1)
  return False, list()


def contiguousSetIterative(encryptedData, securityFailure):
  for firstSetIndex in range(len(encryptedData)):
    for secondSetIndex in range(firstSetIndex + 1, len(encryptedData)):
      currentSet = encryptedData[firstSetIndex:secondSetIndex]
      if reduce(lambda a, b: a + b, currentSet) == securityFailure:
        return currentSet


main()
