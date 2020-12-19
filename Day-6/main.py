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
