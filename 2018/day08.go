package main

import (
	"fmt"
	"strconv"
	"strings"
)

func day8(args [][]rune) int {

	a := strings.Split(string(args[0]), " ")
	tree := make([]int, len(a))
	for i, str := range a {
		tree[i], _ = strconv.Atoi(str)
	}

	_, sum := metaTree(tree)
	fmt.Printf("P1 : %d\n", sum)
	_, sum2 := metaMetaTree(tree)
	fmt.Printf("P2 : %d\n", sum2)
	return 0
}

func metaTree(tree []int) (int, int) {
	childCount := tree[0]
	metaCount := tree[1]
	skip := 2
	sum := 0

	for i := 0; i < childCount; i++ {
		childSkip, childSum := metaTree(tree[skip:])
		skip += childSkip
		sum += childSum
	}
	for i := 0; i < metaCount; i++ {
		sum += tree[i+skip]
	}
	skip += metaCount

	return skip, sum
}

func metaMetaTree(tree []int) (int, int) {
	childCount := tree[0]
	metaCount := tree[1]
	skip := 2
	sum := 0

	childSums := make([]int, childCount)

	for i := 0; i < childCount; i++ {
		childSkip, childSum := metaMetaTree(tree[skip:])
		skip += childSkip
		childSums[i] = childSum
	}

	if childCount == 0 {
		for i := 0; i < metaCount; i++ {
			sum += tree[i+skip]
		}
	} else {
		for i := 0; i < metaCount; i++ {
			metaVal := tree[i+skip]
			if metaVal > 0 && metaVal <= childCount {
				sum += childSums[metaVal-1]
			}
		}

	}

	skip += metaCount

	return skip, sum

}
