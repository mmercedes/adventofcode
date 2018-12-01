package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func day1(argv []string) int {

	if len(argv) == 0 {
		fmt.Fprintln(os.Stderr, "Missing required filename param")
		return 1
	}

	parsedArgs := chronalParser(argv[0])

	if len(parsedArgs) == 0 {
		fmt.Fprintf(os.Stderr, "Failed to parse input file %s\n", argv[0])
		return 1
	}

	result := chronalCalibration(parsedArgs)

	fmt.Printf("Part 1 Result : %d\n", result)

	result = chronalCalibrationPart2(parsedArgs)
	fmt.Printf("Part 2 Result : %d\n", result)

	return 0
}

func chronalParser(filename string) []int {
	file, err := os.Open(filename)
	if err != nil {
		fmt.Fprintln(os.Stderr, err)
		return []int{}
	}
	defer file.Close()

	args := []int{}
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		arg, err := strconv.Atoi(scanner.Text())
		if err != nil {
			fmt.Fprintln(os.Stderr, "Failed to parse arg in file")
			fmt.Fprintln(os.Stderr, err)
			return []int{}
		}
		args = append(args, arg)
	}

	if err := scanner.Err(); err != nil {
		fmt.Fprintln(os.Stderr, err)
		return []int{}
	}

	return args
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
