package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)
var sc = bufio.NewScanner(os.Stdin)
func input() (int) {
	sc.Scan()
	ans, _ := strconv.Atoi(sc.Text())
	return ans
}

func main() {
	sc.Split(bufio.ScanWords)
	R := input()
	C := input()
	sy := input()
	sx := input()
	gy := input()
	gx := input()
	c := make([]string, R)
	MAP := make([][]int, R)
	for i := 0; i < R; i++ {
		sc.Scan()
		c[i] = sc.Text()
	}
	for i := 0; i < R; i++ {
		MAP[i] = make([]int, C)
		for j := 0; j < C; j++ {
			MAP[i][j] = -1
		}
	}
	inf := 100000
	for i := 0; i < R; i++ {
		for j := 0;j < C; j++ {
			if c[i][j] == '#' {
				MAP[i][j] = inf	
			}
		}
	}
	MAP[sx-1][sy-1] = 0
	var queue []int
	var x, y int
	queue = append(queue, sx-1, sy-1)
	for {
		if len(queue) == 0 {break}
		x = queue[0]
		y = queue[1]
		queue = queue[2:]
		if MAP[x-1][y] == -1{

		}
	}
}