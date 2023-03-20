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
	HW := mapAtoi(readline())
	H, _ := HW[0], HW[1]
	matrix := make([][]int, H)
	for i := 0; i < H; i++ {
		matrix[i] = mapAtoi(readline())
	}

	ans := make([]string, H)

	for i, r := range matrix {
		for _, c := range r {
			if c == 0 {
				ans[i] += "."
			} else {
				ans[i] += string('A' - 1 + c)
			}
		}
	}
	for _, r := range ans {
		fmt.Println(r)
	}
}
