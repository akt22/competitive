package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

// ===========================================================================================
// init
// -------------------------------------------------------------------------------------------
const BUFSIZE = 10000000

var rdr *bufio.Reader = bufio.NewReaderSize(os.Stdin, BUFSIZE)

// ===========================================================================================
// utilities
// -------------------------------------------------------------------------------------------
func atoi(s string) int {
	i, err := strconv.Atoi(s)
	if err != nil {
		panic(err)
	}
	return i
}

func readline() string {
	line, _, err := rdr.ReadLine()
	if err != nil {
		panic(err)
	}
	return string(line)
}

func mapAtoi(s string) []int {
	ret := make([]int, 0)
	if s == "" {
		return ret
	}

	l := strings.Fields(s)
	for _, elem := range l {
		ret = append(ret, atoi(elem))
	}
	return ret
}

// ===========================================================================================
// main
// -------------------------------------------------------------------------------------------
func main() {
	NM := mapAtoi(readline())
	N, M := NM[0], NM[1]

	g := make(map[int][]int)

	for i := 0; i < M; i++ {
		ab := mapAtoi(readline())
		a, b := ab[0], ab[1]
		g[a] = append(g[a], b)
		g[b] = append(g[b], a)
	}

	visited := make(map[int]bool)
	var queue []int
	ans := 0

	for i := 1; i <= N; i++ {
		if visited[i] {
			continue
		}
		ans++
		visited[i] = true
		queue = append(queue, i)

		for len(queue) > 0 {
			v := queue[0]
			queue = queue[1:]
			for _, w := range g[v] {
				if visited[w] {
					continue
				}
				visited[w] = true
				queue = append(queue, w)
			}
		}
	}
	fmt.Println(ans)
}
