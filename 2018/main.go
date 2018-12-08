package main

import (
	"bufio"
	"fmt"
	"os"
)

const (
	// USAGE how to run this
	USAGE = "aoc $day_number $input_file"
)

var dayFuncs = map[string]func([][]rune) int{
	"1": day1,
	"2": day2,
	"3": day3,
	"4": day4,
	//        "5": day5,
	//        "6": day6,
	//        "7": day7,
	//        "8": day8,
	//        "9": day9,
	//        "10": day10,
	//        "11": day11,
	//        "12": day12,
	//        "13": day13,
	//        "14": day14,
	//        "15": day15,
	//        "16": day16,
	//        "17": day17,
	//        "18": day18,
	//        "19": day19,
	//        "20": day20,
	//        "21": day21,
	//        "22": day22,
	//        "23": day23,
	//        "24": day24,
}

func wrapper(f func([][]rune) int, args [][]rune) int {
	return f(args)
}

func main() {
	var (
		day      string
		filename string
	)

	argv := os.Args
	day = argv[1]
	filename = argv[2]

	if day == "" || dayFuncs[day] == nil || filename == "" {
		fmt.Println(USAGE)
		os.Exit(1)
	}

	args := fileParse(filename)

	fmt.Printf("Starting run of main func for day %s\n", day)

	returnCode := wrapper(dayFuncs[day], args)
	os.Exit(returnCode)
}

func fileParse(filename string) [][]rune {
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

	if len(args) == 0 {
		fmt.Fprintf(os.Stderr, "Failed to parse input file %s\n", filename)
		os.Exit(1)
	}

	return args
}
