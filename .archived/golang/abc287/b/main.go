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
	S := make([]string, N)
	for i := 0; i < N; i++ {
		s := readline()
		S[i] = s[len(s)-3:]
	}

	T := make(map[string]bool)
	for i := 0; i < M; i++ {
		T[readline()] = true
	}

	ans := 0
	for _, s := range S {
		if _, ok := T[s]; ok {
			ans++
		}
	}
	fmt.Println(ans)
}
