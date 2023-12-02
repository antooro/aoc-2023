package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)


func is_valid(iterations []string) bool{
	for _ , element := range iterations { 
        valores := strings.Split(element, ",")
		limits := map[string]int{
			"red": 12,
			"green":  13,
			"blue": 14,
		}
		for _, element := range valores { 
			valores := strings.Split(strings.TrimSpace(element), " ")
			color_name := valores[1]
			color_value, _ := strconv.Atoi(valores[0])
			if color_value > limits[color_name] {
				return false
			}
		}
	}
	return true
}
func part_one() {
	readFile, err := os.Open("input")
  
    if err != nil {
        fmt.Println(err)
    }
    fileScanner := bufio.NewScanner(readFile)
 
    fileScanner.Split(bufio.ScanLines)
	sum := 0
    for fileScanner.Scan() {
		data := strings.Split(fileScanner.Text(), ":")
		game_id := strings.Split(data[0], " ")
		gid  := game_id[len(game_id)-1]
		num_game_id, _ := strconv.Atoi(gid)
		iterations := strings.Split(data[1], ";")

		if is_valid(iterations){
			sum += num_game_id
		}

    }
	fmt.Printf("%v",sum)
    readFile.Close()
}

func part_two() {
	readFile, err := os.Open("input")
  
    if err != nil {
        fmt.Println(err)
    }
    fileScanner := bufio.NewScanner(readFile)
 
    fileScanner.Split(bufio.ScanLines)
	sum := 0
    for fileScanner.Scan() {
		data := strings.Split(fileScanner.Text(), ":")
		iterations := strings.Split(data[1], ";")
		limits := map[string]int{
			"red": 0,
			"green":  0,
			"blue": 0,
		}
		for _ , element := range iterations { 
			valores := strings.Split(element, ",")
			
			for _, element := range valores { 
				valores := strings.Split(strings.TrimSpace(element), " ")
				color_name := valores[1]
				color_value, _ := strconv.Atoi(valores[0])
				if color_value > limits[color_name] {
					limits[color_name] = color_value
				}
			}
			
		}
		prod := 1
		for _ , v := range limits{
			prod *= v
		}
		sum += prod
		

		}
		

    
	fmt.Printf("%v",sum)
    readFile.Close()
}

func main(){
	part_one()
	part_two()
}