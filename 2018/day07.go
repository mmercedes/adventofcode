package main

import (
	"fmt"
	"sort"
)

type node struct {
	Val      rune
	Children []*node
	Parents  []*node
	Complete bool
}

func day7(args [][]rune) int {

	graph := make(map[rune]*node)

	for _, line := range args {
		// line = 'Step J must be finished before step K can begin.'
		parent, child := rune(line[5]), rune(line[36])
		childNode, parentNode := getOrCreateNode(graph, child), getOrCreateNode(graph, parent)

		addChild(parentNode, childNode)
	}

	steps, time := traverseNodes(graph)
	fmt.Printf("Part 1 : %s\n", steps)
	fmt.Printf("Part 2 : %d\n", time)
	return 0
}

func getOrCreateNode(graph map[rune]*node, val rune) *node {

	if graph[val] == nil {
		n := node{Val: val, Children: []*node{}, Parents: []*node{}, Complete: false}
		graph[val] = &n
	}

	return graph[val]
}

func addChild(parent *node, child *node) {
	parent.Children = append(parent.Children, child)
	child.Parents = append(child.Parents, parent)
}

func traverseNodes(graph map[rune]*node) (string, int) {

	workers := 5
	offset := 60
	queues := make([]int, workers)

	entryPoints := []*node{}

	for _, n := range graph {
		entryPoints = append(entryPoints, n)
	}

	sort.Slice(entryPoints, func(i int, j int) bool {
		return entryPoints[i].Val < entryPoints[j].Val
	})

	path := []rune{}
	notDone := true
	for notDone {
		notDone = false
		spots := workers - 1
		for _, n := range entryPoints {
			if !n.Complete {
				notDone = true
				canComplete := true
				for _, parent := range n.Parents {
					if !parent.Complete {
						canComplete = false
					}
				}
				if canComplete {
					if spots == 0 {
						spots = workers - 1
					}
					queues[spots] += int(n.Val-'A') + 1 + offset
					path = append(path, n.Val)
					n.Complete = true
				}
			}
		}
	}

	max := 0
	for _, time := range queues {
		if time > max {
			max = time
		}
	}
	return string(path), max
}
