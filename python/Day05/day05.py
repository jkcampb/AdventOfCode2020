
def parseZone(boardingPass):
    strColumn = boardingPass[:-4]

    strColumn = strColumn.replace('B', '1').replace('F', '0')
    column = int(strColumn, 2)

    strRow = boardingPass[-4:]
    strRow = strRow.replace('R', '1').replace('L', '0')
    row = int(strRow, 2)

    return (column, row)


def part1(boardingPasses):
    seatIDs = []
    for boardingPass in boardingPasses:
        result = parseZone(boardingPass)
        seatID = result[0]*8 + result[1]

        seatIDs.append(seatID)

    return max(seatIDs)

def part2(boardingPasses):
    seatIDs = []
    for boardingPass in boardingPasses:
        result = parseZone(boardingPass)
        seatID = result[0]*8 + result[1]

        seatIDs.append(seatID)

    missingSeats = [x for x in range(min(seatIDs), max(seatIDs)+1) if x not in seatIDs]

    return(missingSeats[0])
    

def main():
    with open("./python/Day05/input.txt", "r") as inputFile:
        inputData = inputFile.readlines()


    result1 = part1(inputData)
    print(f"Part 1 solution: {result1}")

    result2 = part2(inputData)
    print(f"Part 2 solution: {result2}")


if __name__ == "__main__":
    main()