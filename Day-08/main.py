instructions = open(input("\nInput file: "), 'r').read().split("\n")

if instructions[len(instructions) - 1] == '':
  instructions.pop()

instructions = list(
    map(lambda instruction: instruction.split(" "), instructions))

instructions = list(
    map(
        lambda instruction: {
            "operation": instruction[0],
            "argument": instruction[1],
            "executed": False
        }, instructions))


def detectInfiniteLoop(instructions, instructionIndex=0, accumulator=0):
  if instructionIndex >= len(instructions):
    return accumulator, False

  if instructions[instructionIndex].get("executed") == True:
    return accumulator, True

  else:
    instructions[instructionIndex].update({"executed": True})

    currentOperation = instructions[instructionIndex].get("operation")
    currentArgument = instructions[instructionIndex].get("argument")

    if currentOperation == 'acc':
      accumulator += int(currentArgument)
      instructionIndex += 1

    elif currentOperation == 'jmp':
      instructionIndex += int(currentArgument)

    elif currentOperation == 'nop':
      instructionIndex += 1

    else:
      raise Exception(
          f"Unknown operation '{currentOperation} {currentArgument}' at line {instructionIndex + 1}"
      )

    return detectInfiniteLoop(instructions, instructionIndex, accumulator)


def copyOf(instructions):
  return list(map(lambda instruction: instruction.copy(), instructions))


try:
  print("\nThe value in the accumulator before starting the infinite loop is:",
        detectInfiniteLoop(copyOf(instructions))[0])
except Exception as error:
  print("Error:", error.args[0])
  raise


def swapOperation(instructions, instructionIndex, currentOperation):
  if currentOperation == 'nop':
    instructions[instructionIndex].update({"operation": 'jmp'})
  elif currentOperation == 'jmp':
    instructions[instructionIndex].update({"operation": 'nop'})


def fixCorruptedInstruction(instructions, instructionIndex=0):
  if instructionIndex >= len(instructions):
    raise Exception("\nNo corruption detected")

  else:
    swapOperation(instructions, instructionIndex,
                  instructions[instructionIndex].get("operation"))
    accumulator, infiniteLoopDetected = detectInfiniteLoop(copyOf(instructions))

    if not infiniteLoopDetected:
      return accumulator

    else:
      swapOperation(instructions, instructionIndex,
                    instructions[instructionIndex].get("operation"))
      return fixCorruptedInstruction(instructions, instructionIndex + 1)


try:
  print("\nThe value of the accumulator after the program terminates is:",
        fixCorruptedInstruction(copyOf(instructions)))
except Exception as error:
  print(error.args[0])
