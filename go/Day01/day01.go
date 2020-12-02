package main

import (
	"bufio"
	"errors"
	"fmt"
	"log"
	"os"
	"strconv"
)

func readLines(path string) ([]int, error) {
	file, err := os.Open(path)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	var lines []int
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		i1, err := strconv.Atoi(line)
		if err == nil {
			lines = append(lines, i1)
		}
	}
	return lines, scanner.Err()
}

func part1(arr []int) (int, error) {
	for i, val1 := range arr {
		for _, val2 := range arr[i+1:] {
			if val1+val2 == 2020 {
				return val1 * val2, nil
			}
		}
	}
	return 0, errors.New("No pair of numbers found to add to 2020")
}

func part2(arr []int) (int, error) {
	for i, val1 := range arr {
		for j, val2 := range arr[i+1:] {
			for _, val3 := range arr[j+1:] {
				if val1+val2+val3 == 2020 {
					return val1 * val2 * val3, nil
				}
			}
		}
	}
	return 0, errors.New("No triplet of numbers found to add to 2020")
}

func main() {

	// taking an array
	arr, err := readLines("./input.txt")
	if err != nil {
		log.Fatalf("readLines: %s", err)
	}
	// run parts
	result1, err := part1(arr)
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Printf("Answer to part1: %v\n", result1)

	result2, err := part2(arr)
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Printf("Answer to part2: %v\n", result2)

}
