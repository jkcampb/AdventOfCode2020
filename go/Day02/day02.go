package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func readLines(path string) ([]string, error) {
	file, err := os.Open(path)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		lines = append(lines, line)
	}
	return lines, scanner.Err()
}

func parseLines(line string) (password string, character string, min int, max int, err error) {
	var re = regexp.MustCompile(`(?m)(\d+)-(\d+) (.): (.+)`)

	found := re.FindStringSubmatch(line)

	if found == nil {
		fmt.Printf("no match found\n")
	}
	// found[0] is the whole string match, which we can ditch
	password = found[4]
	character = found[3]
	max, err = strconv.Atoi(found[2])

	// why does returning nil, nil, nil, nil, err no longer work??
	if err != nil {
		return "", "", 0, 0, err
	}
	min, err = strconv.Atoi(found[1])
	if err != nil {
		return "", "", 0, 0, err
	}
	return password, character, min, max, nil
}

func checkPassword1(password string, character string, min int, max int) (result bool) {
	charCount := strings.Count(password, character)

	return (charCount >= min) && (charCount <= max)
}

func part1(arr []string) (countPassed int, err error) {
	countPassed = 0
	for _, line := range arr {
		password, character, min, max, err := parseLines(line)
		if err != nil {
			return 0, err
		}
		result := checkPassword1(password, character, min, max)
		if result {
			countPassed += 1
		}
	}
	return countPassed, nil
}

func checkPassword2(password string, character string, min int, max int) (result bool) {
	// Check character at each position (index zero'd)
	pos1 := (password[min-1] == []byte(character)[0])
	pos2 := (password[max-1] == []byte(character)[0])

	// Return the XOR (character has to be at 1 position, but not the other)
	return pos1 != pos2
}

func part2(arr []string) (countPassed int, err error) {
	countPassed = 0
	for _, line := range arr {
		password, character, min, max, err := parseLines(line)
		if err != nil {
			return 0, err
		}
		result := checkPassword2(password, character, min, max)
		if result {
			countPassed += 1
		}
	}
	return countPassed, nil
}

func main() {

	// taking an array
	arr, err := readLines("./input.txt")
	if err != nil {
		log.Fatalf("readLines: %s", err)
	}

	result1, err := part1(arr)
	if err != nil {
		log.Fatalf("Part1: %s", err)
	}
	fmt.Printf("Answer to part1: %v\n", result1)

	result2, err := part2(arr)
	if err != nil {
		log.Fatalf("Part2: %s", err)
	}
	fmt.Printf("Answer to part2: %v\n", result2)
}
