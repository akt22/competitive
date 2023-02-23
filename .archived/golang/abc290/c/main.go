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

// ===========================================================================================
// main
// -------------------------------------------------------------------------------------------
func main() {
	nk := strings.Split(readline(), " ")
	_, K := atoi(nk[0]), atoi(nk[1])

	A := strings.Split(readline(), " ")

	m := make(map[int]bool)
	for _, a := range A {
		m[atoi(a)] = true
	}

	for i := 0; i < K; i++ {
		if !m[i] {
			fmt.Println(i)
			os.Exit(0)
		}
	}

	fmt.Println(K)
}
