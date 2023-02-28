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

func pow(n uint64, m int) uint64 {
	if m == 0 {
		return 1
	}
	result := n
	for i := 2; i <= m; i++ {
		result *= n
	}
	return result
}

// ===========================================================================================
// main
// -------------------------------------------------------------------------------------------
func main() {
	S := readline()
	var ans uint64
	for i, c := range S {
		ans += pow(26, len(S)-i-1) * uint64(int(c)-64)
	}
	fmt.Println(ans)
}
