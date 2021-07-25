def main():
  fieldRules, nearbyTickets = parseData()

  nonValidValues = validateTickets(nearbyTickets, fieldRules)

  print(f"\nThe ticket scanning error rate is: {sum(nonValidValues)}")


def parseData():
  inputFile = input("\nInput file: ")
  rawFieldRules, _, rawNearbyTickets = open(inputFile, 'r').read().split("\n\n")

  fieldRules = {
      key: value
      for (key, value)\
      in [parseFieldRule(fieldRule) for fieldRule in rawFieldRules.split("\n")]
  }

  nearbyTickets = rawNearbyTickets.split("\n")[1:]

  if nearbyTickets[len(nearbyTickets) - 1] == '':
    nearbyTickets.pop()

  nearbyTickets = [[int(value) for value in ticket.split(",")]
                   for ticket in nearbyTickets]

  return fieldRules, nearbyTickets


def parseFieldRule(fieldRule: str):
  type, rawRuleRanges = fieldRule.split(": ")

  rangeValues = [[int(value) for value in ruleRange.split("-")]
                 for ruleRange in rawRuleRanges.split(" or ")]

  ruleRanges = [
      range(ruleRange[0], ruleRange[1] + 1) for ruleRange in rangeValues
  ]

  return type, {"firstRange": ruleRanges[0], "secondRange": ruleRanges[1]}


def validateTickets(tickets: list, fieldRules: dict):
  allTicketValues = [
      ticketValue for ticket in tickets for ticketValue in ticket
  ]

  valueRanges = [
      valueRange for ruleRanges in fieldRules.values()
      for valueRange in ruleRanges.values()
  ]

  nonValidValues = [
      ticketValue for ticketValue in allTicketValues
      if not any([ticketValue in valueRange for valueRange in valueRanges])
  ]

  return nonValidValues


main()
