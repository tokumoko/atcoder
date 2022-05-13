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
func min(x, y int) (float64) {
	if x < y {return x}
	return y
}
func max(x, y int) (float64) {
	if x < y {return y}
	return x
}

func main() {
	sc.Split(bufio.ScanWords)
	var i, mod, ans, cnt float64
	mod = 1000000007
	x := input()
	y := input()
	ans = 1
	cnt = 1
	for i = float64(x+y); i > max(x, y); i-- {
		ans *= i
		ans /= cnt
		cnt += 1
		
	}
	fmt.Println(ans)
}