from utils import read_file, timer
import itertools

def read_input():
    input = read_file("day10")
    arr = [int(x) for x in input]
    return arr

def _calculate(arr):
    _length = len(arr)
    _count_3 = 1
    _count_1 = 1
    for i in range(1,_length):
        if arr[i] - arr[i-1] == 3:
            _count_3 += 1
        elif arr[i] - arr[i-1] == 1:
            _count_1 += 1
    return _count_1 * _count_3

def ranges(arr):
    arr = sorted(set(arr))
    gaps = [[s, e] for s, e in zip(arr, arr[1:]) if s+1 < e]
    edges = iter(arr[:1] + sum(gaps, []) + arr[-1:])
    return list(zip(edges, edges))

def _calculate_arrangements(arr):
    _length = len(arr)
    _current = []
    _sum = 1

    for i in range(1,_length-1):
        if 0 < arr[i+1] - arr[i-1] <= 3:
            _current.append(arr[i])

    for item in ranges(_current):
        _repeat = item[1] - item[0] + 1
        _numbers = list(range(1, _repeat + 1))
        if len(_numbers) == 1:
            _sum *= 2
        else:
            _sum_item_combinations = 0
            for e in range(_repeat + 1):
                if len(_numbers) == 3 and e == 0:
                    continue
                _sum_item_combinations += len(list(itertools.combinations(_numbers, e)))
            _sum *= _sum_item_combinations

    return _sum

@timer
def solve_problem_1():
    arr = read_input()
    return _calculate(sorted(arr))

@timer
def solve_problem_2():
    arr = read_input()
    arr.append(0)
    arr = sorted(arr)
    return _calculate_arrangements(arr)

if __name__ == "__main__":

    print(f"Solution1: {solve_problem_1()}, Solution2: {solve_problem_2()}")