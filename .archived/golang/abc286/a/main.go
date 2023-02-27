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
	ln1 := mapAtoi(readline())
	A := strings.Fields(readline())

	P, Q, R, S := ln1[1], ln1[2], ln1[3], ln1[4]

	a0 := A[:P-1]
	a1 := A[R-1 : S]
	a2 := A[Q : R-1]
	a3 := A[P-1 : Q]
	a4 := A[S:]

	ans := make([]string, 0)
	ans = append(ans, a0...)
	ans = append(ans, a1...)
	ans = append(ans, a2...)
	ans = append(ans, a3...)
	ans = append(ans, a4...)
	fmt.Println(strings.Join(ans, " "))
}
