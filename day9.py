from utils import read_file, timer
import itertools

def read_input():
    input = read_file("day9")
    arr = [x for x in input]
    return arr

def _calculate(arr, step):
    _index = step
    for i in arr[step:]:
        _is_ok = False
        _comb_arr = [int(item) for item in arr[_index-step:_index]]
        for numbers in itertools.combinations(_comb_arr, 2):
            if sum(numbers) == int(i):
               _is_ok = True
        if _is_ok:
            _index += 1
        else:
            return i
    return 0

def _search_contiguous(arr, target_sum, r): 
    _contiguous_list = [0]  
    n = len(arr) 
    start = 0
    curr_sum = arr[0] 
    index = 1
    i = 1
    while i <= n: 
        if curr_sum == target_sum and index == r: 
            _contiguous_list = arr[i-r:i]
        while index >= r: 
            curr_sum -= arr[start] 
            start += 1
            index = r-1
        if i < n: 
            curr_sum += arr[i] 
            index += 1
        i += 1
          
    return min(_contiguous_list) + max(_contiguous_list) 

def _calculate_contiguous(arr, step):
    _target = _calculate(arr, step)
    _int_arr = [int(element) for element in arr]
    for i in range(2,50):
        _result = _search_contiguous(_int_arr, int(_target), i)
        if _result > 0:
            return _result
    return 0

@timer
def solve_problem_1():
    arr = read_input()
    return _calculate(arr, 25)

@timer
def solve_problem_2():
    arr = read_input()
    return _calculate_contiguous(arr, 25)

if __name__ == "__main__":

    print(f"Solution1: {solve_problem_1()}, Solution2: {solve_problem_2()}")