package main

import (
	"fmt"
	"os"
)

const (
	// USAGE how to run this
	USAGE = "aoc $day_number $args"
)

var dayFuncs = map[string]func([]string) int{
	"1": day1,
	//        "2": day2,
	//        "3": day3,
	//        "4": day4,
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

func wrapper(f func([]string) int, argv []string) int {
	return f(argv)
}

func main() {
	var (
		day string
	)

	argv := os.Args
	day = argv[1]

	if day == "" || dayFuncs[day] == nil {
		fmt.Println(USAGE)
		os.Exit(1)
	}

	fmt.Printf("Starting run of main func for day %s\n", day)

	returnCode := wrapper(dayFuncs[day], argv[2:])
	os.Exit(returnCode)
}
