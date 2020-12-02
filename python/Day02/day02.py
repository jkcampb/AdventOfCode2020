def parseLine(line):
    parts1 = line.strip().split(': ')
    password = parts1[1]

    parts2 = parts1[0].split(' ')

    character = parts2[1]

    minmax = parts2[0].split('-')
    charMin = int(minmax[0])
    charMax = int(minmax[1])

    return password, character, charMin, charMax


def checkPassword1(password, character, charMin, charMax):
    charCount = password.count(character)

    return (charCount >= charMin) and (charCount <= charMax)

def part1(passwords):
    countValid = 0

    for passwordLine in passwords:
        password, character, charMin, charMax = parseLine(passwordLine)

        valid = checkPassword1(password, character, charMin, charMax)
        if valid:
            countValid += 1

    return countValid


def checkPassword2(password, character, charMin, charMax):
    return (password[charMin-1] == character) !=  (password[charMax-1] == character)

def part2(passwords):
    countValid = 0

    for passwordLine in passwords:
        password, character, charMin, charMax = parseLine(passwordLine)

        valid = checkPassword2(password, character, charMin, charMax)
        if valid:
            countValid += 1

    return countValid


def main():
    with open("python/Day02/input.txt") as input:
        passwords = input.readlines()

    result1 = part1(passwords)
    print(f"Part 1 solution: {result1}")

    result2 = part2(passwords)
    print(f"Part 2 solution: {result2}")

    
if __name__ == "__main__":
    main()