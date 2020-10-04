package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)


var sc = bufio.NewScanner(os.Stdin)
var	u [][]int
var d = []int{}
var f = []int{}
var cnt = 1

func dfs(idx int, nodes []int) {
	for _, _node := range nodes {
		node := _node - 1
		if node < 0 {
			break
		}
		if d[node] == 0 {
			d[node] = cnt
			cnt++
			dfs(node, u[node])
		}
	}
	f[idx] = cnt
	cnt++
}


func solve() {
	for i := 0; i < len(d); i++ {
		if d[i] == 0 {
			d[i] = cnt
			cnt++
			dfs(i, u[i])
		}
	}
	for idx, elem := range d {
		fmt.Printf("%d %d %d\n", idx+1, elem, f[idx])
	}
}

func main() {
	var n int
	if sc.Scan() {
		var err error
		n, err = strconv.Atoi(sc.Text())
		if err != nil {
			fmt.Println(err)
		}
	}

	u = make([][]int, n)

	for i := 0; i < n; i++ {
		if sc.Scan() {
			in := sc.Text()
			_l := strings.Split(in, " ")[1:]
			l := []int{}
			for _, elem := range _l[1:] {
				v, err := strconv.Atoi(elem)
				if err != nil {
					fmt.Println(err)
				}
				l = append(l, v)
			}
			sort.Ints(l)
			u[i] = l
			d = append(d, 0)
			f = append(f, 0)
		}
	}

	solve()
}
