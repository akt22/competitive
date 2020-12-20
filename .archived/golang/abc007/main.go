package main

import (
	"bytes"
	"fmt"
	"time"
)

const row = 7
const col = 8
const INF = 0

var dx = []int{1, 0, -1, 0}
var dy = []int{0, 1, 0, -1}

type P struct {
	x int
	y int
}

var sy = 2 - 1
var sx = 2 - 1
var gy = 4 - 1
var gx = 5 - 1

var c = [][]string{
	{"#", "#", "#", "#", "#", "#", "#", "#"},
	{"#", ".", ".", ".", ".", ".", ".", "#"},
	{"#", ".", "#", "#", "#", "#", "#", "#"},
	{"#", ".", ".", "#", ".", ".", ".", "#"},
	{"#", ".", ".", "#", "#", ".", ".", "#"},
	{"#", "#", ".", ".", ".", ".", ".", "#"},
	{"#", "#", "#", "#", "#", "#", "#", "#"},
}

var d = [row][col]int{}

func pp(x, y int) string {
	var buf bytes.Buffer
	for i := 0; i < row; i++ {
		for j := 0; j < col; j++ {
			if i == sy && j == sx {
				buf.WriteString("s")
			} else if i == gy && j == gx {
				buf.WriteString("g")
			} else if i == x && j == y {
				buf.WriteString("+")
			} else if c[i][j] != "#" {
				buf.WriteString(fmt.Sprintf("%d", d[i][j]))
			} else {
				buf.WriteString(c[i][j])
			}
		}
		buf.WriteString("\n")
	}
	return buf.String()
}

func solve() {
	fmt.Println(pp(0, 0))

	for idx, row := range d {
		for idx2 := range row {
			d[idx][idx2] = INF
		}
	}

	q := make([]P, 0)
	q = append(q, P{sx, sy})
	for len(q) > 0 {
		p := q[0]
		q = q[1:]

		if p.x == gy && p.y == gx {
			fmt.Println("success")
			break
		}
		for i := 0; i < 4; i++ {
			nx := p.x + dx[i]
			ny := p.y + dy[i]
			time.Sleep(time.Millisecond * 100)
			fmt.Println(pp(nx, ny))

			if (0 <= nx && nx < col) && (0 <= ny && ny < row) && (d[nx][ny] == INF) && c[nx][ny] != "#" {
				q = append(q, P{nx, ny})
				d[nx][ny] = d[p.x][p.y] + 1
			}
		}
	}

	fmt.Println(d[gy][gx])
}

func main() {
	solve()
}
