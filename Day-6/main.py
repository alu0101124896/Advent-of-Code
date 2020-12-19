allYesAnswers = open(input("\nInput file: "), 'r').read().split("\n\n")

allYesAnswersByGroup = list(
    map(lambda yesAnswersByGroup: yesAnswersByGroup.replace("\n", ""),
        allYesAnswers))

allDistinctYesAnswersByGroup = list(
    map(lambda yesAnswersByGroup: set(yesAnswersByGroup), allYesAnswersByGroup))

numberOfDistinctYesAnswersByGroup = list(
    map(lambda distinctYesAnswersByGroup: len(distinctYesAnswersByGroup),
        allDistinctYesAnswersByGroup))

print(
    "\nThe sum of the number of questions to which anyone answered \"yes\" on each group is:",
    sum(numberOfDistinctYesAnswersByGroup))

allYesAnswersByGroupAndPerson = list(
    map(
        lambda yesAnswersByGroupAndPerson: yesAnswersByGroupAndPerson.split(
            "\n"), allYesAnswers))

if allYesAnswersByGroupAndPerson[len(allYesAnswersByGroupAndPerson) - 1][
    len(allYesAnswersByGroupAndPerson[len(allYesAnswersByGroupAndPerson) - 1]) -
    1] == "":
  allYesAnswersByGroupAndPerson[len(allYesAnswersByGroupAndPerson) - 1].pop()

allYesAnswersByGroupAndPerson = list(
    map(
        lambda yesAnswersByGroupAndPerson: list(
            map(lambda param: set(param), yesAnswersByGroupAndPerson)),
        allYesAnswersByGroupAndPerson))


def commonYesAnswers(yesAnswersByGroupAndPerson):
  commonYesAnswersByGroup = yesAnswersByGroupAndPerson[0]
  for yesAnswersByPerson in yesAnswersByGroupAndPerson:
    commonYesAnswersByGroup = commonYesAnswersByGroup.intersection(
        yesAnswersByPerson)
  return commonYesAnswersByGroup


allCommonYesAnswersByGroup = list(
    map(
        lambda yesAnswersByGroupAndPerson: commonYesAnswers(
            yesAnswersByGroupAndPerson), allYesAnswersByGroupAndPerson))

numberOfCommonYesAnswersByGroup = list(
    map(lambda commonYesAnswersByGroup: len(commonYesAnswersByGroup),
        allCommonYesAnswersByGroup))

print(
    "\nThe sum of the number of questions to which everyone answered \"yes\" on each group is:",
    sum(numberOfCommonYesAnswersByGroup))
