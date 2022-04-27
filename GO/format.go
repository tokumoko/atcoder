package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var sc = bufio.NewScanner(os.Stdin)

func input() int {
    sc.Scan()
    i, _ := strconv.Atoi(sc.Text())
    return i
}

func main() {
	sc.Split(bufio.ScanWords)
	N := input()
	var T[N] int
}