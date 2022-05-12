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
	a := int64(input())
	b := input()
	ans := int64(1)
	mod := int64(1000000007)
	for b > 0 {
		if b % 2 == 1{
			ans *= a
			ans %= mod
		}
		b >>= 1
		a *= a
		a %= mod
	}
	fmt.Println(ans)
}