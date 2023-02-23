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
// utilties
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
	readline()
	A := strings.Split(readline(), " ")
	B := strings.Split(readline(), " ")

	var ans int
	for _, b := range B {
		ans += atoi(A[atoi(b)-1])
	}

	fmt.Println(ans)
}
