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
	for i := 0; i < len(l); i++ {
		ret = append(ret, atoi(l[i]))
	}
	return ret
}

// ===========================================================================================
// main
// -------------------------------------------------------------------------------------------

var g map[int]int
var m map[int]bool
var ans []string

func rec(i int) {
	if _, visited := m[i]; visited {
		return
	}
	m[i] = true
	if dest, ok := g[i]; ok {
		rec(dest)
	}
	ans = append(ans, strconv.Itoa(i))
}

func main() {
	NM := mapAtoi(readline())
	N := NM[0]

	A := mapAtoi(readline())

	g = make(map[int]int)
	for _, a := range A {
		g[a] = a + 1
	}

	m = make(map[int]bool)
	ans = make([]string, 0)

	for i := 1; i <= N; i++ {
		rec(i)
	}
	fmt.Println(strings.Join(ans, " "))
}
