package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
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
	MAP := make([][]int64, R+2)
	for i := 0; i < R; i++ {
		sc.Scan()
		c[i] = sc.Text()
	}
	for i = 0; i < R+2; i++ {
		MAP[i] = make([]int64, C+2)
		for j := 0; j < C+2; j++ {
			MAP[i][j] = -1
		}
	}
	var queue string
	var x int
	for i = 0; i < R; i++ {
		queue = strings.Split(c[i])[]
		for j = 0; j < C; j++ {
			x = pop
		}
	}
	fmt.Println(MAP)
	fmt.Println(sy, sx, gy, gx)
}