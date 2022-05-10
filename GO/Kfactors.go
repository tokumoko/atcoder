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
	K := input()
	ans := 0
	a := make([]int, N+1)
	for i := 2; i <= N; i++ {
		if a[i] == 0 {
			for j := i; j <= N; j+=i {
				a[j]++
			}
		}
		if a[i] >= K{
			ans++
		}
	}
	fmt.Println(ans)
}