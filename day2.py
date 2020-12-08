from utils import read_file, timer

def read_input():
    input = read_file("day2")
    arr = [x for x in input]
    return arr

def _occurences(str):
    num=0
    char=str.partition(":")[0]
    pwd=str.partition(":")[2]
    num=pwd.count(char) 
    return num
    

def _calculate_how_many(arr):  
    num=0
    for l in arr:
        minO=int(l.partition("-")[0])
        maxO=int(l.partition("-")[2].partition(" ")[0])
        occ=_occurences(l.partition("-")[2].partition(" ")[2])
        if occ >= minO and occ <= maxO:
            num = num + 1
    return num

def _calculate_at_one_position(arr):  
    num=0
    for l in arr:
        pos1=int(l.partition("-")[0])
        pos2=int(l.partition("-")[2].partition(" ")[0])
        char=l.partition("-")[2].partition(" ")[2].partition(":")[0]
        _str=l.partition("-")[2].partition(" ")[2].partition(":")[2]
        if pos1 <= len(_str) and pos2 <= len(_str):
            if _str[pos1] == char and _str[pos2] != char:
                num = num + 1
            elif _str[pos1] != char and _str[pos2] == char:
                num = num + 1
    return num

@timer
def solve_problem_1():
    arr = read_input()
    return _calculate_how_many(arr) 

@timer
def solve_problem_2():
    arr = read_input()
    return _calculate_at_one_position(arr) 

if __name__ == "__main__":

    print(f"Solution1: {solve_problem_1()}, Solution2: {solve_problem_2()}")