package main

import (
	"bufio"
	"fmt"
	"math"
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
	N := input()
	h := make([]int, N)
	for i := 0; i < N; i++ {
		h[i] = input()
	}
	dp := make([]int, N)
	dp[0] = 0
	dp[1] = int(math.Abs(float64(h[1] - h[0])))
	for i := 2; i < N; i++ {
		dp[i] = int(math.Min(
			math.Abs(float64(h[i] - h[i-1])) + 
			float64(dp[i-1]), 
			math.Abs(float64(h[i] - h[i-2])) +
			float64(dp[i-2])))
	}
	fmt.Println(dp[N-1])
}