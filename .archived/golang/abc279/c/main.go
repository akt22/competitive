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
	H, W := HW[0], HW[1]

	tS := make([][]uint8, W)
	for i := 0; i < W; i++ {
		tS[i] = make([]uint8, H)
	}

	for i := 0; i < H; i++ {
		S := readline()
		for j := 0; j < W; j++ {
			tS[j][i] = S[j]
		}
	}

	tT := make([][]uint8, W)
	for i := 0; i < W; i++ {
		tT[i] = make([]uint8, H)
	}
	for i := 0; i < H; i++ {
		T := readline()
		for j := 0; j < W; j++ {
			tT[j][i] = T[j]
		}
	}

	check := make(map[string]int)
	for _, t := range tT {
		check[string(t)] += 1
	}

	for _, s := range tS {
		s2 := string(s)
		if v, ok := check[s2]; ok && v > 0 {
			check[s2] -= 1
		} else {
			fmt.Println("No")
			os.Exit(0)
		}
	}
	fmt.Println("Yes")
}
