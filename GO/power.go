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
	a := float64(input())
	b := float64(input())
	fmt.Println(math.Pow(a, b) % float64(1000000007))
}