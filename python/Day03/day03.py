import numpy as np


def countTrees(treeMap, x, y):
    xPos, yPos = 0, 0

    treeCount = 0

    while yPos + y < treeMap.shape[0]:
        xPos += x
        xPos = xPos % treeMap.shape[1]
        yPos += y

        if treeMap[yPos][xPos] == "#":
            treeCount += 1
        
    return treeCount


def part1(treeMap):
    return countTrees(treeMap, 3, 1)


def part2(treeMap):
    return countTrees(treeMap, 1, 1) * countTrees(treeMap, 3, 1) * countTrees(treeMap, 5, 1) * countTrees(treeMap, 7, 1) * countTrees(treeMap, 1, 2)


def main():
    with open("./python/Day03/input.txt", "r") as input:
        lines = input.readlines()

    treeMap = np.array([[char for char in line.strip()] for line in lines])

    result1 = part1(treeMap)
    print(f"Part 1 solution: {result1}")

    result2 = part2(treeMap)
    print(f"Part 2 solution: {result2}")


if __name__ == "__main__":
    main()