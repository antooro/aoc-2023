import numpy as np
import string

def print_all(wall,posy,posx):
    simbolos = string.punctuation.replace(".","")
    posx = posx + 1
    posy = posy + 1
    print(wall[posy,posx],posy, posx)
    
    print(wall[posy - 1, posx] in simbolos)
    print(wall[posy - 1, posx + 1] in simbolos)
    print(wall[posy - 1, posx - 1] in simbolos)
    print(wall[posy, posx - 1] in simbolos)
    print(wall[posy, posx + 1] in simbolos)
    print(wall[posy + 1, posx - 1] in simbolos)
    print(wall[posy + 1, posx] in simbolos)
    print(wall[posy + 1, posx + 1] in simbolos)
    
def check_adj(wall, posy, posx):
    # print_all(matriz,posy,posx)
    simbolos = string.punctuation.replace(".","")
    posx = posx + 1
    posy = posy + 1
    if wall[posy - 1, posx] in simbolos: return True
    if wall[posy - 1, posx + 1] in simbolos: return True
    if wall[posy - 1, posx - 1] in simbolos: return True
    if wall[posy, posx - 1] in simbolos: return True
    if wall[posy, posx + 1] in simbolos: return True
    if wall[posy + 1, posx - 1] in simbolos: return True
    if wall[posy + 1, posx] in simbolos: return True
    if wall[posy + 1, posx + 1] in simbolos: return True

    return False

def part_one():
    with open("input") as f:
        m = []
        for line in f.readlines():
            m.append([c for c in line.strip()])

        matriz = np.matrix(m)
        valores = []
        current_n = ""
        valid = False
        wall = np.full((matriz.shape[0] + 2, matriz.shape[1] + 2),'.')
        x = 1
        y = 1
        wall[x : x + matriz.shape[1], y : y + matriz.shape[0]] = matriz
        

        for iy, ix in np.ndindex(matriz.shape):
            if matriz[iy, ix].isdigit():
                if valid:
                    current_n += matriz[iy, ix]
                    
                else:
                    
                    if check_adj(wall, iy, ix):
                        valid = True
                        
                    current_n += matriz[iy, ix]
                    
            else:
                if valid:
                    valores.append(int(current_n))
                
                valid = False
                current_n = ""

        print(sum(valores))
    
def get_number(wall, posy, posx):
    coords = {(posy,posx)}
    
    for i in reversed(range(0, posx+1)):
        if wall[posy, i - 1 ].isdigit():
            coords.add((posy,i - 1))
        else:
            break   
    
    for i in range(posx, len(wall[posy])):
        if wall[posy, i + 1 ].isdigit():
            coords.add((posy,i + 1))
        else:
            break   
        
    return tuple(coords)

def get_adj_numbers(wall, posy, posx):
    # print_all(matriz,posy,posx)
    simbolos = string.punctuation.replace(".","")
    numbers = set()
    if wall[posy - 1, posx].isdigit(): numbers.add(get_number(wall, posy - 1, posx))
    if wall[posy - 1, posx + 1].isdigit(): numbers.add(get_number(wall, posy - 1, posx + 1))
    if wall[posy - 1, posx - 1].isdigit(): numbers.add(get_number(wall, posy - 1, posx - 1))
    if wall[posy, posx - 1].isdigit(): numbers.add(get_number(wall, posy, posx - 1))
    if wall[posy, posx + 1].isdigit(): numbers.add(get_number(wall, posy, posx + 1))
    if wall[posy + 1, posx - 1].isdigit(): numbers.add(get_number(wall, posy + 1, posx - 1))
    if wall[posy + 1, posx].isdigit(): numbers.add(get_number(wall, posy + 1, posx))
    if wall[posy + 1, posx + 1].isdigit(): numbers.add(get_number(wall, posy + 1, posx + 1))
    
    
    return numbers

def part_two():
    with open("input") as f:
        m = []
        for line in f.readlines():
            m.append([c for c in line.strip()])

        matriz = np.matrix(m)

        wall = np.full((matriz.shape[0] + 2, matriz.shape[1] + 2),'.')
        x = 1
        y = 1
        wall[x : x + matriz.shape[1], y : y + matriz.shape[0]] = matriz
        
        res = 0
        nums = []
        for iy, ix in np.ndindex(wall.shape):
            if wall[iy, ix] == "*":
                n = get_adj_numbers(wall, iy, ix)
                if len(n) == 2:
                    n_list = []
                    for numer_coord in n:
                        num = ""
                        for y,x in sorted(numer_coord):
                            num += wall[y,x] 
                        n_list.append(int(num))
                    
                    nums.append(n_list[0]* n_list[1])

        print(sum(nums))
        
part_two()