from utils import read_file, timer

def read_input():
    input = read_file("day3")
    arr = [x for x in input]
    return arr
    
def _calculate(arr, pos_num):  
    num = 0
    _len = len(arr[0])
    _pos = 0
    _char = "#"
    for l in arr:
        if l[_pos] == _char:
            num = num + 1
        _pos = _pos + pos_num
        if _pos >= _len:
            _pos = _pos - _len
    return num

@timer
def solve_problem_1():
    arr = read_input()
    return _calculate(arr, 3) 

@timer
def solve_problem_2():
    arr = read_input()
    iArr = [[1,1], [1,3], [1,5], [1,7], [2,1]]
    mul = 1
    for x, y in iArr:
        r = _calculate(arr[::x], y)
        mul *= r
    return mul

if __name__ == "__main__":

    print(f"Solution1: {solve_problem_1()}, Solution2: {solve_problem_2()}")