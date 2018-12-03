package main

import (
	"fmt"
	"os"
	"strconv"
)

func day1(args [][]rune) int {

	parsedArgs := chronalParser(args)

	result := chronalCalibration(parsedArgs)

	fmt.Printf("Part 1 Result : %d\n", result)

	result = chronalCalibrationPart2(parsedArgs)
	fmt.Printf("Part 2 Result : %d\n", result)

	return 0
}

func chronalParser(args [][]rune) []int {
	parsed := []int{}
	for _, arg := range args {
		i, err := strconv.Atoi(string(arg))
		if err != nil {
			fmt.Fprintf(os.Stderr, "Failed to convert string arg to int")
			os.Exit(1)
		}
		parsed = append(parsed, i)
	}

	return parsed
}

func chronalCalibration(changes []int) int {
	sum := 0
	for _, change := range changes {
		sum += change
	}

	return sum
}

func chronalCalibrationPart2(changes []int) int {

	seen := make(map[int]bool)

	seen[0] = true
	sum := 0
	// assume it must reach the same frequency twice
	for {
		for _, change := range changes {
			sum += change
			if seen[sum] {
				return sum
			}
			seen[sum] = true
		}
	}
}
