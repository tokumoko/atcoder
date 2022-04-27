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
func min(a, b int) int {
	if a < b{
		return a
	}
	return b
}

func main() {
	var taka, aoki int
    sc.Split(bufio.ScanWords)
    A := input()
	B := input()
    C := input()
	D := input()
    E := input()
	F := input()
    X := input()

	taka = (X / (A+C))*A + min(A, X % (A+C))
	aoki = (X / (D+F))*D + min(D, X % (D+F))
	

	taka *= B
	aoki *= E
	if taka > aoki{
		fmt.Println("Takahashi")
	} else if taka < aoki{
		fmt.Println("Aoki")
	} else{
		fmt.Println("Draw")
	}
}