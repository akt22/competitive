package main

import (
	"fmt"
	"math"
)

const INF = 10000

const V = 4
const E = 5
const r = 0

var s = []int{0, 0, 1, 2, 1}
var t = []int{1, 2, 2, 3, 3}
var d = []int{1, 4, 2, 1, 5}

var G = map[int]map[int]int{}

var cost = []int{}
var used = []bool{}

func min(nums ...int) int {
	if len(nums) == 0 {
		panic("funciton min() requires at least one argument.")
	}
	res := nums[0]
	for i := 0; i < len(nums); i++ {
		res = int(math.Min(float64(res), float64(nums[i])))
	}
	return res
}

func dijkstra(s int) {

	cost[s] = 0

	for {
		base := -1
		for u := 0; u < V; u++ {
			if !used[u] && (base == -1 || cost[u] < cost[base]) {
				base = u
			}
		}
		if base == -1 {
			break
		}

		for target, _cost := range G[base] {
			cost[target] = min(cost[target], cost[base]+_cost)
		}
		used[base] = true
	}
}

func solve() {
	for i := 0; i < E; i++ {
		start := s[i]
		terminate := t[i]
		distance := d[i]
		_, ok := G[start]
		if !ok {
			G[start] = map[int]int{}
		}
		G[start][terminate] = distance
	}

	for i := 0; i < V; i++ {
		cost = append(cost, INF)
		used = append(used, false)
	}

	dijkstra(0)

	for _, c := range cost {
		fmt.Println(c)
	}
}

func main() {
	solve()
}
