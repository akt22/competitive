package main

import (
	"fmt"
	"math"
)

// var D = 5
// var G = 25000
// var p = []int{20, 40, 50, 30, 1}
// var c = []int{1000, 1000, 1000, 1000, 1000}

var D = 2
var G = 2000
var p = []int{3, 5}
var c = []int{500, 800}

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

func main() {
	cnt := 0
	for _, v := range p {
		cnt += v
	}

	var bit uint
	ans := 1000000
	num := 0
	for bit = 0; bit < (1 << D); bit++ {
		point := 0
		num = 0
		unresolved := []int{}
		for i := 0; i < D; i++ {
			if (bit>>i)&1 == 1 {
				// 全問回答できた
				point += 100*p[i]*(i+1) + c[i]
				num += p[i]
			} else {
				// 全問回答できなかった
				unresolved = append(unresolved, i)
			}
		}
		if point >= G {
			ans = min(ans, num)
			fmt.Printf("(bit, ans, num, point): (%d, %d, %d, %d)\n", bit, ans, num, point)
		} else {
			fmt.Printf("(bit, point, num, unresolved): (%d, %d, %d, %v)\n", bit, point, num, unresolved)

			for i := len(unresolved) - 1; i >= 0; i-- {
				for j := 0; j < p[unresolved[i]]-1; j++ {
					point += 100 * (unresolved[i] + 1)
					num++
					if point >= G {
						fmt.Printf("(bit, ans, num, point): (%d, %d, %d, %d)\n", bit, ans, num, point)
						ans = min(ans, num)
						break
					}
				}
			}
		}
	}
	fmt.Println(ans)
}
