package main

import (
	"bufio"
	"fmt"
	"math"
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
	NAB := mapAtoi(readline())
	N, A, B := NAB[0], NAB[1], NAB[2]
	S := readline()

	ans := math.Inf(1)
	for i := 0; i < N/2; i++ {
		diff := 0
		for j := 0; j < N/2; j++ {
			if S[j] != S[N-j-1] {
				diff++
			}
		}
		ans = math.Min(float64(i*A+diff*B), ans)
		S = S[1:] + string(S[0])
	}
	fmt.Printf("%.0f\n", ans)
}
