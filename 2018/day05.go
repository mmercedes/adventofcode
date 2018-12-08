package main

import (
	"fmt"
	"unicode"
)

func day5(args [][]rune) int {

	// only check the first line
	result := alchemy(args[0])
	fmt.Printf("%d units\n", len(result))
	result2 := bestAlchemy(args[0])
	fmt.Printf("%d units part 2\n", result2)
	return 0
}

func alchemy(units []rune) []rune {
	reducable, index := canReduce(units)

	if !reducable {
		return units
	}

	copy := []rune{}

	for i, r := range units {
		if i == index || i == index+1 {
			continue
		}
		copy = append(copy, r)
	}

	return alchemy(copy)
}

func canReduce(units []rune) (bool, int) {
	for i, r := range units {
		if i+1 == len(units) {
			break
		}
		if unicode.ToUpper(r) == unicode.ToUpper(units[i+1]) {
			if r != units[i+1] {
				return true, i
			}
		}

	}
	return false, -1
}

func removeType(units []rune, unit rune) []rune {

	copy := []rune{}

	for _, r := range units {
		if unicode.ToUpper(r) == unicode.ToUpper(unit) {
			continue
		}

		copy = append(copy, r)
	}

	return copy
}

func bestAlchemy(units []rune) int {

	types := make(map[rune]bool)

	for _, unit := range units {
		types[unicode.ToUpper(unit)] = true
	}

	best := -1
	for unit := range types {
		copy := removeType(units, unit)
		result := alchemy(copy)
		if len(result) < best || best == -1 {
			best = len(result)
		}
	}

	return best
}
