import re


def parsePassports(bigString):
    passportStrings = bigString.split('\n\n')
    passportStrings = [x.replace('\n', ' ') for x in passportStrings]

    return passportStrings

def passportHash(passportString):
    passport = {}
    for field in passportString.split(' '):
        if field != '':
            bits = field.split(':')
            passport[bits[0]] = bits[1]

    return passport

def part1(input):
    valids = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
    passports = parsePassports(input)

    countValid = 0
    for passport in passports:
        validPass = True
        for valid in valids:
            if f"{valid}:" not in passport:
                validPass = False
                break
        if validPass:
            countValid += 1
        
    return countValid


def part2Check(passport):
    if (passport.get('byr') is None) or not (1920 <= int(passport.get('byr')) <= 2002):
        return False

    if (passport.get('iyr') is None) or not (2010 <= int(passport.get('iyr')) <= 2020):
        return False

    if (passport.get('eyr') is None) or not (2020 <= int(passport.get('eyr')) <= 2030):
        return False

    if (passport.get('hgt') is None):
        return False
    elif "cm" in passport.get('hgt'):
        height = int(passport['hgt'].replace('cm', ''))
        if not (150 <= height <= 193):
            return False
    elif "in" in passport.get('hgt'):
        height = int(passport['hgt'].replace('in', ''))
        if not (59 <= height <= 76):
            return False
    elif ("cm" not in passport.get('hgt')) or ("in" not in passport.get('hgt')):
        return False

    regHcl = r"#[0-9a-f]{6}"
    if (passport.get('hcl') is None) or (re.match(regHcl, passport.get('hcl')) is None):
        return False

    if (passport.get('ecl') is None) or not (passport.get('ecl') in ['amb','blu','brn','gry','grn','hzl','oth']):
        return False

    regPid = r"^[0-9]{9}$"
    if (passport.get('pid') is None) or (re.match(regPid, passport.get('pid')) is None):
        return False

    return True


def part2(input):
    passportStrings = parsePassports(input)
    passports = [passportHash(x) for x in passportStrings]

    validCount = 0

    checkList = []
    for passport in passports:
        if part2Check(passport):
            checkList.append(passport['pid'])
            validCount += 1        

    return validCount


def main():
    with open("./python/Day04/input.txt", "r") as inputFile:
        inputData = inputFile.read()

    result1 = part1(inputData)
    print(f"Part 1 solution: {result1}")

    result2 = part2(inputData)
    print(f"Part 2 solution: {result2}")


if __name__ == "__main__":
    main()