package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
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
	A := mapAtoi(readline())
	B := mapAtoi(readline())

	am := make(map[int]int)
	bm := make(map[int]int)

	for i, a := range A {
		am[a] = i
	}
	for i, b := range B {
		bm[b] = i
	}

	s := append(A, B...)
	sort.Ints(s)
	aans := make([]string, N)
	bans := make([]string, M)
	for i, s := range s {
		if _, ok := am[s]; ok {
			aans[am[s]] = fmt.Sprintf("%d", i+1)
		}
		if _, ok := bm[s]; ok {
			bans[bm[s]] = fmt.Sprintf("%d", i+1)
		}
	}
	fmt.Println(strings.Join(aans, " "))
	fmt.Println(strings.Join(bans, " "))
}
