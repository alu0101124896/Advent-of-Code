import networkx as nx

bagRules = open(input("\nInput file: "), 'r').read().split("\n")

if bagRules[len(bagRules) - 1] == '':
  bagRules.pop()

bagRulesDict = dict()
for bagRulesIndex in range(len(bagRules)):
  bagRules[bagRulesIndex] = bagRules[bagRulesIndex].split(" bags contain ")
  bagRules[bagRulesIndex][1] = bagRules[bagRulesIndex][1].split(", ")

  if bagRules[bagRulesIndex][1] != ['no other bags.']:

    contentDict = dict()
    for contentIndex in range(len(bagRules[bagRulesIndex][1])):
      bagRules[bagRulesIndex][1][contentIndex] = bagRules[bagRulesIndex][1][
          contentIndex].split(" ")
      bagRules[bagRulesIndex][1][contentIndex].pop()

      contentDict.update({
          bagRules[bagRulesIndex][1][contentIndex][1] + " " + bagRules[bagRulesIndex][1][contentIndex][2]:
              {
                  "weight": int(bagRules[bagRulesIndex][1][contentIndex][0])
              }
      })

    bagRuleDict = {bagRules[bagRulesIndex][0]: contentDict}
  bagRulesDict.update(bagRuleDict)

bagRulesGraph = nx.DiGraph(bagRulesDict)


def outermostBags(bag, outermostSet=set()):
  for predecesor in bagRulesGraph.predecessors(bag):
    predecesorSet = {predecesor}
    if not predecesorSet.issubset(outermostSet):
      outermostSet.add(predecesor)
      outermostSet.update(outermostBags(predecesor, outermostSet))
  return outermostSet


print(
    "\nThe number of bag colors that can eventually containt at least one shiny gold bag is:",
    len(outermostBags("shiny gold")))
