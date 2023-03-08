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
	NQ := mapAtoi(readline())
	N, Q := NQ[0], NQ[1]

	events := make([][]int, Q)
	for i := 0; i < Q; i++ {
		events[i] = mapAtoi(readline())
	}

	members := make(map[int]int, N)
	for _, event := range events {
		t, x := event[0], event[1]
		if t == 1 {
			members[x] += 1
		} else if t == 2 {
			members[x] += 2
		} else {
			if members[x] >= 2 {
				fmt.Println("Yes")
			} else {
				fmt.Println("No")
			}
		}
	}
}
