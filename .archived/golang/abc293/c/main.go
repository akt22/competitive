package main

import (
	"fmt"
)

type StackElement struct {
	i, j int
	path []int
}

var H, W int
var grid [][]int

func hasDuplicate(slice []int) bool {
	seen := map[int]bool{}

	for _, num := range slice {
		if seen[num] {
			return true
		}
		seen[num] = true
	}

	return false
}

func dfsWithStack() int {
	stack := []StackElement{{0, 0, []int{grid[0][0]}}}
	count := 0

	for len(stack) > 0 {
		cur := stack[len(stack)-1]
		stack = stack[:len(stack)-1]

		i, j := cur.i, cur.j
		path := cur.path

		if i == H-1 && j == W-1 {
			if !hasDuplicate(path) {
				count++
			}
			continue
		}

		if i+1 < H && grid[i][j] != grid[i+1][j] {
			newPath := make([]int, len(path))
			copy(newPath, path)
			newPath = append(newPath, grid[i+1][j])
			stack = append(stack, StackElement{i + 1, j, newPath})
		}

		if j+1 < W && grid[i][j] != grid[i][j+1] {
			newPath := make([]int, len(path))
			copy(newPath, path)
			newPath = append(newPath, grid[i][j+1])
			stack = append(stack, StackElement{i, j + 1, newPath})
		}
	}

	return count
}

func main() {
	fmt.Scan(&H, &W)

	grid = make([][]int, H)

	for i := 0; i < H; i++ {
		grid[i] = make([]int, W)
		for j := 0; j < W; j++ {
			fmt.Scan(&grid[i][j])
		}
	}

	fmt.Println(dfsWithStack())
}
