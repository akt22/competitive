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

	l := strings.Split(s, " ")
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

	length := 0
	visited := make(map[int]bool)
	for dep := 1; dep <= N; dep++ {
		if visited[dep] {
			continue
		}
		length++
		queue := make([]int, 0)
		queue = append(queue, dep)
		for len(queue) > 0 {
			cur := queue[0]
			queue = queue[1:]
			for _, next := range g[cur] {
				if visited[next] {
					continue
				}
				visited[next] = true
				queue = append(queue, next)
			}

		}
	}
	fmt.Println(M - N + length)
}
