ACCUMULATOR = 0

def processInstruction(i, instruction):
    global ACCUMULATOR

    parts = instruction.strip().split(' ')

    if parts[0] == 'jmp':
        return i + int(parts[1])
    elif parts[0] == 'acc':
        ACCUMULATOR += int(parts[1])

    return i + 1


def part1(inputData):
    runInstructions(inputData)

    return


def part2(inputData):
    global ACCUMULATOR

    jmpIndices = [i for i, val in enumerate(inputData) if "jmp" in val]

    for swapIndex in jmpIndices:
        newInput = inputData.copy()
        newInput[swapIndex] = newInput[swapIndex].replace('jmp','nop')

        ACCUMULATOR = 0

        result = runInstructions(newInput)

        if result == "Completed":
            return

    nopIndices = [i for i, val in enumerate(inputData) if "nop" in val]

    for swapIndex in nopIndices:
        newInput = inputData.copy()
        newInput[swapIndex] = newInput[swapIndex].replace('nop','jmp')

        ACCUMULATOR = 0

        result = runInstructions(newInput)

        if result == "Completed":
            return


def runInstructions(instructions):
    executedInstructions = []

    i = 0
    while i not in executedInstructions:
        executedInstructions.append(i)
        i = processInstruction(i, instructions[i])

        if i >= len(instructions):
            return "Completed"

    return "Looped"


def main():
    with open("./python/Day08/input.txt", "r") as inputFile:
        inputData = inputFile.readlines()

    part1(inputData)
    print(f"Part 1 solution: {ACCUMULATOR}")


    part2(inputData)
    print(f"Part 2 solution: {ACCUMULATOR}")


if __name__ == "__main__":
    main()