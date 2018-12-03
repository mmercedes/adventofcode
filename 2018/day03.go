package main

import (
	"fmt"
	"regexp"
	"strconv"
)

func day3(args [][]rune) int {
	r := regexp.MustCompile("#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)")
	ids := []int{}
	xArr := []int{}
	yArr := []int{}
	hArr := []int{}
	wArr := []int{}

	for _, arg := range args {
		matches := r.FindStringSubmatch(string(arg))

		id, _ := strconv.Atoi(matches[1])
		x, _ := strconv.Atoi(matches[2])
		y, _ := strconv.Atoi(matches[3])
		h, _ := strconv.Atoi(matches[4])
		w, _ := strconv.Atoi(matches[5])

		ids = append(ids, id)
		xArr = append(xArr, x)
		yArr = append(yArr, y)
		hArr = append(hArr, h)
		wArr = append(wArr, w)
	}

	result := quiltClaims(xArr, yArr, hArr, wArr)
	fmt.Printf("Part1 Result : %d\n", result)

	result2 := quiltClaimsPart2(xArr, yArr, hArr, wArr, ids)
	fmt.Printf("Part2 Result : %d\n", result2)

	return 0
}

func quiltClaims(xArr []int, yArr []int, hArr []int, wArr []int) int {
	quilt := make([][]int, 1000)
	for i := 0; i < 1000; i++ {
		quilt[i] = make([]int, 1000)
	}

	// fill the quilt
	for i, x := range xArr {
		y, h, w := yArr[i], hArr[i], wArr[i]

		for j := x; j < x+h; j++ {
			for k := y; k < y+w; k++ {
				quilt[j][k] = quilt[j][k] + 1
			}
		}
	}

	result := 0

	for _, row := range quilt {
		for _, claims := range row {
			if claims > 1 {
				result++
			}
		}
	}

	return result
}

func quiltClaimsPart2(xArr []int, yArr []int, hArr []int, wArr []int, ids []int) int {
	quilt := make([][]int, 1000)
	for i := 0; i < 1000; i++ {
		quilt[i] = make([]int, 1000)
		for j := 0; j < 1000; j++ {
			quilt[i][j] = -1
		}
	}

	didOverlap := map[int]bool{}

	for i, x := range xArr {
		id := ids[i]
		y, h, w := yArr[i], hArr[i], wArr[i]

		for j := x; j < x+h; j++ {
			for k := y; k < y+w; k++ {
				if quilt[j][k] != id && quilt[j][k] != -1 {
					id2 := quilt[j][k]
					didOverlap[id2] = true
					didOverlap[id] = true
				}
				quilt[j][k] = id
			}
		}
	}

	for _, id := range ids {
		if !didOverlap[id] {
			return id
		}
	}

	return -1
}
