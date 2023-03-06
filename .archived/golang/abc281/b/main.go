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
	S := readline()

	if len(S) != 8 {
		fmt.Println("No")
		os.Exit(0)
	}

	s := S[1 : len(S)-1]

	i, err := strconv.Atoi(s)
	if err != nil {
		fmt.Println("No")
		os.Exit(0)
	}

	var flg bool
	if i >= 100000 && i <= 999999 {
		flg = true
	} else {
		flg = false
	}

	if (S[0] >= 'A' && S[0] <= 'Z') && (S[len(S)-1] >= 'A' && S[len(S)-1] <= 'Z') && flg {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}

}
