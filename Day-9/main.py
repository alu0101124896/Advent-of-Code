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


def firstSecurityFailure(encryptedData, preambleLength, encryptedDataIndex):
  if encryptedDataIndex >= len(encryptedData):
    raise Exception("\nNo security failure detected")

  else:
    if not validEncryption(encryptedData, encryptedDataIndex, preambleLength,
                           encryptedDataIndex - preambleLength):
      return encryptedData[encryptedDataIndex]

    else:
      return firstSecurityFailure(encryptedData, preambleLength,
                                  encryptedDataIndex + 1)


def main():
  encryptedData = open(input("\nInput file: "), 'r').read().split("\n")
  preambleLength = int(input("\nPreamble length: "))

  if encryptedData[len(encryptedData) - 1] == '':
    encryptedData.pop()

  encryptedData = list(map(int, encryptedData))

  try:
    print("\nThe first encryption security failure is:",
          firstSecurityFailure(encryptedData, preambleLength, preambleLength))
  except Exception as error:
    print(error.args[0])


main()
