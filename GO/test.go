package main

import (
	"bufio"
	"log"
	"os"
	"runtime"
	"strconv"
)

var sc = bufio.NewScanner(os.Stdin)

func input() int {
    sc.Scan()
    i, _ := strconv.Atoi(sc.Text())
    return i
}

func main() {
	log.Println(runtime.NumGoroutine())
}