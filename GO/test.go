package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var sc = bufio.NewScanner(os.Stdin)

func input() int {
    sc.Scan()
    i, _ := strconv.Atoi(sc.Text())
    return i
}

func main() {
	c := make([]string, 3)
	for i := 0; i < 3; i++ {
		sc.Scan()
		c[i] = sc.Text()
	}
	p := make([]string, 3)
	for i := 0; i < 3; i++ {
		p[i] = strings.Split(c[0], "")[3]
	}
	fmt.Println(c)
	fmt.Println(p[0])
}