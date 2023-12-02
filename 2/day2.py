from collections import Counter, defaultdict

def is_valid(cube_iter):
    for itert in cube_iter:
        c = Counter()
        for cube in itert.split(","):
            cube_data = cube.strip().split()
            c[cube_data[1]]+= int(cube_data[0])
        if c.get("red",0) > 12 or c.get("green",0) > 13 or c.get("blue",0) > 14:
            return False
    return True

    

def part_one():
    with open("input") as f:
        res = 0
        for line in f.readlines():
            data = line.split(":")

            game_id = int(data[0].split()[-1])
            cube_iter = data[1].strip().split(";")
            
            if is_valid(cube_iter):
                res += game_id
                
        print(res)
        
def part_two():
    with open("input") as f:
        res = 0
        
        for line in f.readlines():
            data = line.split(":")
            
            game_id = int(data[0].split()[-1])
            cube_iter = data[1].strip().split(";")
            c = defaultdict(int)
            
            for itert in cube_iter:
                for cube in itert.split(","):
                    cube_data = cube.strip().split()
                    if int(cube_data[0]) > c.get(cube_data[1],0):
                        c[cube_data[1]] = int(cube_data[0])
            
            prod = 1
            for _ ,v in c.items():
                prod *= v
                
            res += prod       
        print(res)
                
part_two()