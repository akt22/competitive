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

var g map[int][]int
var visited map[int]bool
var edge int

func rec(i int) {
	e := len(g[i])
	if e != 1 && e != 2 {
		fmt.Println("No")
		os.Exit(0)
	}
	if e == 1 {
		if edge >= 2 {
			fmt.Println("No")
		} else {
			edge++
		}
	}
	visited[i] = true
	for _, v := range g[i] {
		if !visited[v] {
			rec(v)
		}
	}
}

func main() {
	NM := mapAtoi(readline())
	N, M := NM[0], NM[1]
	g = make(map[int][]int)
	for i := 0; i < M; i++ {
		ab := mapAtoi(readline())
		a, b := ab[0], ab[1]
		g[a] = append(g[a], b)
		g[b] = append(g[b], a)
	}

	visited = make(map[int]bool)
	edge = 0
	rec(1)
	if edge != 2 {
		fmt.Println("No")
		os.Exit(0)
	}
	for i := 1; i <= N; i++ {
		if !visited[i] {
			fmt.Println("No")
			os.Exit(0)
		}
	}
	fmt.Println("Yes")
}
