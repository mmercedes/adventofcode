package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strings"
)

func day2(argv []string) int {

	if len(argv) == 0 {
		fmt.Fprintln(os.Stderr, "Missing required filename param")
		return 1
	}

	parsedArgs := inventoryParser(argv[0])

	if len(parsedArgs) == 0 {
		fmt.Fprintf(os.Stderr, "Failed to parse input file %s\n", argv[0])
		return 1
	}

	result := inventoryChecksum(parsedArgs)
	fmt.Printf("Part1 Result : %d\n", result)

	result2 := inventoryPart2(parsedArgs)
	fmt.Printf("Part2 Result : %s\n", result2)
	return 0
}

func inventoryParser(filename string) [][]rune {
	file, err := os.Open(filename)
	if err != nil {
		fmt.Fprintln(os.Stderr, err)
		return [][]rune{}
	}
	defer file.Close()

	args := [][]rune{}
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		args = append(args, []rune(scanner.Text()))
	}

	if err := scanner.Err(); err != nil {
		fmt.Fprintln(os.Stderr, err)
		return [][]rune{}
	}

	return args
}

func inventoryChecksum(args [][]rune) int {
	twoCount, threeCount := 0, 0

	for _, arg := range args {
		two, three := inventoryChecksumHelper(arg)
		twoCount += two
		threeCount += three
	}

	return twoCount * threeCount
}

func inventoryChecksumHelper(arg []rune) (int, int) {
	str := make([]rune, len(arg))
	copy(str, arg)

	sort.Slice(str, func(i, j int) bool {
		return str[i] < str[j]
	})

	seen, twoCount, threeCount := 0, 0, 0

	for i, r := range str {
		seen++
		if i+1 == len(str) || r != str[i+1] {
			if seen == 2 {
				twoCount = 1
			}
			if seen == 3 {
				threeCount = 1
			}
			if twoCount == 1 && threeCount == 1 {
				break
			}
			seen = 0
		}
	}

	return twoCount, threeCount
}

func inventoryPart2(args [][]rune) string {
	seen := make(map[string]bool)

	for _, arg := range args {
		result := inventoryPart2Helper(arg, seen)
		if result != "" {
			return result
		}
	}
	fmt.Fprintf(os.Stderr, "Didnt find an answer!\n")
	return ""
}

func inventoryPart2Helper(str []rune, seen map[string]bool) string {

	for i := range str {
		tmp := make([]rune, len(str))
		copy(tmp, str)
		tmp[i] = '.'
		if seen[string(tmp)] {
			return strings.Replace(string(tmp), ".", "", 1)
		}
		seen[string(tmp)] = true
	}

	return ""
}
