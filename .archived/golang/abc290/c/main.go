package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
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

	m := make(map[string]bool)
	var AA []int

	for _, a := range A {
		if !m[a] {
			m[a] = true
			AA = append(AA, atoi(a))
		}
	}
	sort.Ints(AA)

	l := len(AA)

	for i := 0; i < K; i++ {
		if l <= i {
			fmt.Println(AA[l-1] + 1)
			os.Exit(0)
		} else if AA[i] != i {
			fmt.Println(i)
			os.Exit(0)
		}
	}

	fmt.Println(K)
}
