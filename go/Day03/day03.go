package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
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

func linesToMap(lines []string) [][]byte {
	var resultMap [][]byte
	for _, line := range lines {
		line = strings.TrimSuffix(line, "\n")
		resultMap = append(resultMap, []byte(line))
	}

	return resultMap
}

func countTrees(treeMap [][]byte, x int, y int) int {
	treeCount := 0

	xPos := 0
	yPos := 0

	for yPos+y < len(treeMap) {
		xPos += x
		xPos = xPos % len(treeMap[0])
		yPos += y

		if treeMap[yPos][xPos] == []byte("#")[0] {
			treeCount += 1
		}

	}

	return treeCount
}

func part1(treeMap [][]byte) int {
	return countTrees(treeMap, 3, 1)
}

func part2(treeMap [][]byte) int {
	return countTrees(treeMap, 1, 1) * countTrees(treeMap, 3, 1) * countTrees(treeMap, 5, 1) * countTrees(treeMap, 7, 1) * countTrees(treeMap, 1, 2)
}

func main() {

	// taking an array
	arr, err := readLines("./input.txt")
	if err != nil {
		log.Fatalf("readLines: %s", err)
	}
	treeMap := linesToMap(arr)

	result1 := part1(treeMap)
	fmt.Printf("Answer to part1: %v\n", result1)

	result2 := part2(treeMap)
	fmt.Printf("Answer to part2: %v\n", result2)
}
