import math


def main():
  fieldRules, yourTicket, nearbyTickets = parseData()

  validTickets, nonValidValues = validateTickets(nearbyTickets, fieldRules)

  # print(f"\nThe ticket scanning error rate is: {sum(nonValidValues)}")

  fieldsOrder = getFieldsOrder(fieldRules, validTickets)

  print("\nThe result of multiplying the six departure values of my ticket is:",
        math.prod(getDepartureValues(yourTicket, fieldsOrder)))


def parseData():
  inputFile = input("\nInput file: ")
  rawFieldRules, yourTicket, rawNearbyTickets = \
    open(inputFile, 'r').read().split("\n\n")

  fieldRules = {
      key: value
      for (key, value)\
      in [parseFieldRule(fieldRule) for fieldRule in rawFieldRules.split("\n")]
  }

  yourTicket = [int(value) for value in yourTicket.split("\n")[1].split(",")]

  nearbyTickets = rawNearbyTickets.split("\n")[1:]

  if nearbyTickets[len(nearbyTickets) - 1] == '':
    nearbyTickets.pop()

  nearbyTickets = [[int(value) for value in ticket.split(",")]
                   for ticket in nearbyTickets]

  return fieldRules, yourTicket, nearbyTickets


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

  validTickets = [
      ticket for ticket in tickets
      if not any([value in ticket for value in nonValidValues])
  ]

  return validTickets, nonValidValues


def getFieldsOrder(fieldRules: dict, validTickets: list):
  fieldsOrder = dict()
  fieldCandidates = fieldRules.copy()
  fieldValues = [[ticket[index] for ticket in validTickets]
                 for index in range(len(fieldCandidates.items()))]

  while len(fieldsOrder.items()) < len(fieldCandidates.items()):
    for (fieldName, ruleRanges) in fieldCandidates.items():
      posibleMatch = [
          all([
              any([
                  fieldValues[valueIndex][ticketIndex] in range
                  for range in ruleRanges.values()
              ]) for ticketIndex in range(len(fieldValues[valueIndex]))
          ]) for valueIndex in range(len(fieldCandidates.items()))
      ]

      if posibleMatch.count(True) == 1:
        matchIndex = posibleMatch.index(True)

        fieldValues[matchIndex] = [-1]

        fieldsOrder.update({fieldName: matchIndex})
        break

  return fieldsOrder


def getDepartureValues(yourTicket: list, fieldsOrder: dict):
  departureValues = [
      value for value in yourTicket if yourTicket.index(value) in [
          index for (fieldName, index) in fieldsOrder.items()
          if fieldName.startswith("departure")
      ]
  ]

  return departureValues


main()
