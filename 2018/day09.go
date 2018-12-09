package main

import (
	"container/ring"
	"fmt"
	"regexp"
	"strconv"
)

func day9(args [][]rune) int {
	// 410 players; last marble is worth 72059 points
	r := regexp.MustCompile(`([0-9]+) players; last marble is worth ([0-9]+) points`)
	matches := r.FindStringSubmatch(string(args[0]))
	playerCount, _ := strconv.Atoi(matches[1])
	lastMarble, _ := strconv.Atoi(matches[2])

	highScore := marbleGame(playerCount, lastMarble)
	fmt.Printf("P1: %d\n", highScore)
	highScore2 := marbleGame(playerCount, lastMarble*100)
	fmt.Printf("P2: %d\n", highScore2)
	return 0
}

func marbleGame(playerCount int, lastMarble int) int {

	scores := make([]int, playerCount)
	marbles := &ring.Ring{Value: 0}

	for turn := 1; turn <= lastMarble; turn++ {
		if turn%23 == 0 {
			player := turn % playerCount
			scores[player] = scores[player] + turn

			marbles = marbles.Move(-8)
			scores[player] = scores[player] + (marbles.Unlink(1)).Value.(int)
			marbles = marbles.Move(1)
		} else {
			marble := &ring.Ring{Value: turn}

			marbles = marbles.Move(1)
			marbles = marbles.Link(marble)
			marbles = marbles.Move(-1)
		}
	}

	highScore := -1
	for _, score := range scores {
		if score > highScore {
			highScore = score
		}
	}

	return highScore
}
