package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var (
	sc = bufio.NewScanner(os.Stdin)

	change int
	payment = 1000
	coins = []int{500, 100, 50, 10, 5, 1}
	ans = 0
)

func solve() {
	for _, coin := range coins {
		t := change / coin
		change -= t * coin
		ans += t
	}
	fmt.Println(ans)
}

func main() {
	for true {
		ans = 0
		if sc.Scan() {
			if sc.Text() == "0" {
				return
			}

			s := sc.Text()
			i, err := strconv.Atoi(s)
			if err != nil {
				fmt.Println(err)
			}
			change = payment - i
			solve()
		}
	}
}
