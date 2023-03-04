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
	NM := readline()
	N, M := mapAtoi(NM)[0], mapAtoi(NM)[1]
	S := make([]string, N)
	for i := 0; i < N; i++ {
		S[i] = readline()
	}

	ans := 0
	for i := 0; i < N-1; i++ {
		for j := i + 1; j < N; j++ {
			tmp := true
			for k := 0; k < M; k++ {
				if S[i][k] == 'x' && S[j][k] == 'x' {
					tmp = false
					break
				}
			}
			if tmp {
				ans++
			}
		}
	}
	fmt.Println(ans)
}
