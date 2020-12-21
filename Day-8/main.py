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
  if instructions[instructionIndex].get("executed") == True:
    return accumulator

  else:
    instructions[instructionIndex].update({"executed": True})

    operation = instructions[instructionIndex].get("operation")
    argument = int(instructions[instructionIndex].get("argument"))

    if operation == 'acc':
      accumulator += argument
      instructionIndex += 1

    elif operation == 'jmp':
      instructionIndex += argument

    elif operation == 'nop':
      instructionIndex += 1

    else:
      print("Error: unknown operation")
      return -1

    return detectInfiniteLoop(instructions, instructionIndex, accumulator)


print("\nThe value in the accumulator before starting the infinite loop is:",
      detectInfiniteLoop(instructions))
