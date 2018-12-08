package main

import (
	"fmt"
	"regexp"
	"strconv"
)

func day4(args [][]rune) int {
	r := regexp.MustCompile(`\[[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:([0-9]{2})\] (?:Guard #)?([0-9]+)?(.*)`)
	guards := make(map[int][]int)

	oldguard := 0
	start := -1
	for _, arg := range args {
		matches := r.FindStringSubmatch(string(arg))

		minute, _ := strconv.Atoi(matches[1])
		guard, _ := strconv.Atoi(matches[2])
		action := matches[3]

		// check if guard is set, if not run the make
		if guard > 0 && len(guards[guard]) == 0 {
			guards[guard] = make([]int, 60)
		}

		if action == " begins shift" {
			postShift(guards, oldguard, start, minute-1)
			oldguard = guard
		} else if action == "wakes up" {
			postShift(guards, oldguard, start, minute-1)
			start = -1
		} else if action == "falls asleep" {
			start = minute
		} else {
			fmt.Printf("Failed to parse line '%s', action was '%s'\n", matches[0], action)
			return 1
		}
	}

	guardID, minuteN := whoSleeptMost(guards)
	fmt.Printf("Guard %d sleept the most at minute %d\n", guardID, minuteN)
	guardID, minuteN = whoSleeptMostAtMinute(guards)
	fmt.Printf("Guard %d sleept most freq slept at minute %d\n", guardID, minuteN)
	return 0
}

func postShift(guards map[int][]int, guard int, start int, end int) {
	if guard == 0 || start == -1 {
		return
	}

	for i := start; i < end; i++ {
		guards[guard][i] = guards[guard][i] + 1
	}
}

func whoSleeptMost(guards map[int][]int) (int, int) {

	who := 0
	time := -1
	max := -1

	for guard, shifts := range guards {
		sum, min := guardStats(shifts)

		if sum > max {
			who = guard
			time = min
		}
	}

	return who, time
}

func guardStats(shifts []int) (int, int) {
	sum := 0
	max := -1
	maxmin := -1

	for min, val := range shifts {
		sum += val
		if val > max {
			maxmin = min
		}
	}

	return sum, maxmin
}

func whoSleeptMostAtMinute(guards map[int][]int) (int, int) {

	guardID := 0
	maxmin := -1
	maxval := -1

	for guard, shifts := range guards {

		for min, val := range shifts {
			if val > maxval {
				maxmin = min
				maxval = val
				guardID = guard
			}
		}
	}

	return guardID, maxmin
}
