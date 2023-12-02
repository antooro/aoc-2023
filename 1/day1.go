package main

import (
	"bufio"
	"fmt"
	"os"
	"unicode"
	"strconv"
	"strings"
)

func part_one() {
	readFile, err := os.Open("input")
  
    if err != nil {
        fmt.Println(err)
    }
    fileScanner := bufio.NewScanner(readFile)
 
    fileScanner.Split(bufio.ScanLines)
	resultado := 0
    for fileScanner.Scan() {
		cleared := ""
		for _ , char := range fileScanner.Text() {
			if unicode.IsDigit(char) {
				cleared += string(char)
			}
		}
		partialres := string(string(cleared[0]) + string(cleared[len(cleared)-1:]))
		num, _ := strconv.Atoi(partialres)
		resultado += num

    }
	fmt.Printf(strconv.Itoa(resultado))

    readFile.Close()
}

func part_two() {
	readFile, err := os.Open("input")
  
    if err != nil {
        fmt.Println(err)
    }
    fileScanner := bufio.NewScanner(readFile)
 
    fileScanner.Split(bufio.ScanLines)
	resultado := 0
	listanums := [9]string{"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"}

    for fileScanner.Scan() {
		cleared := ""
		for i , char := range fileScanner.Text() {
			if unicode.IsDigit(char) {
				cleared += string(char)
			} else {
				for index, element := range listanums {
					if strings.HasPrefix(fileScanner.Text()[i:], element) {
						cleared += strconv.Itoa(index+1)
					}
				}
			}
		}
		partialres := string(string(cleared[0]) + string(cleared[len(cleared)-1:]))
		num, _ := strconv.Atoi(partialres)
		resultado += num

    }
	fmt.Printf(strconv.Itoa(resultado))

    readFile.Close()
}

func main() {
 
    part_two()
}