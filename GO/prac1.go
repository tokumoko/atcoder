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
	N := input()
	M := input()
	T := make([]int, N)
	for i := 0; i < N; i++ {
		T[i] = 0
	}
	var a, b, ans int
	for i := 0;i < M;i++ {
		a = input()
		b = input()
		if a < b {
			T[b-1] += 1
		}else{
			T[a-1] += 1
		}
	}
	for _, j := range T {
		if j == 1 {
			ans += 1
		}
	}
	fmt.Println(ans)
}