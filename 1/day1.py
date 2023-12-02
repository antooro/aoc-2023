
def part_two():
    result = 0
    dic = {
                'one': "o1e", 
                'two': "t2o",
                'three': "t3e",
                'four': "f4r",
                'five': "f5e",
                'six': "s6x",
                'seven': "s7n",
                'eight': "e8t",
                'nine': "n9e"
                }
    
    with open("input") as f:
        for file in f.readlines():
                       
            for k,v in dic.items():
                file = file.replace(k,v)
            digits = ''.join(filter(str.isdigit, file))

            result += int(digits[0]+digits[-1])
            
    return result
    
def part_one():
    result = 0
    with open("input") as f:
        for file in f.readlines():
            digits = ''.join(filter(str.isdigit, file))
            result += int(digits[0]+digits[-1])
            
            
    return result

print(part_two())