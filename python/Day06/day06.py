
def parseGroup1(group):
    group = group.replace('\n','')

    allQs = [x for x in group]

    return list(set(allQs))


def splitGroups(allGroups):
    return allGroups.split('\n\n')


def part1(inputData):
    groups = splitGroups(inputData)

    totalCount = 0
    for group in groups:
        totalYes = len(parseGroup1(group))

        totalCount += totalYes
    
    return totalCount


def parseGroup2(group):
    people = group.split('\n')

    intersect = set(people[0])

    for person in people[1:]:
        intersect = intersect & set([x for x in person])

    return intersect


def part2(inputData):
    groups = splitGroups(inputData)

    totalCount = 0
    for group in groups:
        totalYes = len(parseGroup2(group))

        totalCount += totalYes
    
    return totalCount

def main():
    with open("./python/Day06/input.txt", "r") as inputFile:
        inputData = inputFile.read()


    result1 = part1(inputData)
    print(f"Part 1 solution: {result1}")

    result2 = part2(inputData)
    print(f"Part 2 solution: {result2}")


if __name__ == "__main__":
    main()