def rulesToDict(rules):
    ruleDict = {}
    for rule in rules:
        rule = rule.replace('bags', '').replace('bag', '').replace('.', '').strip()
        ruleParts = rule.split(' contain ')

        containsDict = {}
        for contains in ruleParts[1].split(', '):
            containsParts = contains.split(' ', 1)
            if containsParts[0].isdigit():
                containsDict[containsParts[1].strip()] = int(containsParts[0])
        
        ruleDict[ruleParts[0].strip()] = containsDict

    return ruleDict

def findColor(rules, color):
    baseColors = []
    for k, v in rules.items():
        if color in v.keys():
            baseColors.append(k)

    return list(set(baseColors))


def part1(rules):
    rulesDict = rulesToDict(rules)
    colors = findColor(rulesDict, "shiny gold")

    lastLen = 0
    while len(colors) != lastLen:
        lastLen = len(colors)
        for color in colors:
            newColors = findColor(rulesDict, color)
            colors.extend(newColors)

        colors = list(set(colors))
    
    return len(colors)


def getNumBags(rules, color):
    
    totalBags = 0
    for k, v in rules[color].items():
        totalBags += v
        totalBags += v*getNumBags(rules, k)

    return totalBags


def part2(rules):
    rulesDict = rulesToDict(rules)
    totalBags = getNumBags(rulesDict, 'shiny gold') 

    return totalBags


def main():
    with open("./python/Day07/input.txt", "r") as inputFile:
        inputData = inputFile.readlines()

    result1 = part1(inputData)
    print(f"Part 1 solution: {result1}")

    result2 = part2(inputData)
    print(f"Part 2 solution: {result2}")


if __name__ == "__main__":
    main()