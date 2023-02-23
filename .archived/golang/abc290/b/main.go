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
	nk := strings.Split(readline(), " ")
	K := atoi(nk[1])

	S := readline()

	var ans string
	for _, r := range S {
		c := string(r)
		if c == "o" && K > 0 {
			K--
			ans += "o"
		} else {
			ans += "x"
		}
	}

	fmt.Println(ans)
}
