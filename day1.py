from utils import read_file, timer

def read_input():
    input = read_file("day1")
    arr = [int(x) for x in input]
    return arr

def _calculate_x2(arr):  
    sum=0
    for i in arr: 
        for j in arr: 
            sum = i + j 
            if sum == 2020:
                return(i*j)

def _calculate_x3(arr):  
    sum=0
    for i in arr: 
        for j in arr: 
            for k in arr: 
                sum = i + j + k
                if sum == 2020:
                    return(i*j*k)

@timer
def solve_problem_1():
    arr = read_input()
    return _calculate_x2(arr)  

@timer
def solve_problem_2():
    arr = read_input()
    return _calculate_x3(arr)  

if __name__ == "__main__":

    print(f"Solution1: {solve_problem_1()}, Solution2: {solve_problem_2()}")