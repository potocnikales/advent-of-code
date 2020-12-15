from utils import read_file, timer

def read_input():
    input = read_file("day15")
    arr = [int(x) for x in input[0].split(",")]
    return arr

def _calculate(arr, nth_num):
    _counter = 0
    _arr = arr.copy()
    while _counter < nth_num - len(arr):
        _last = _arr[-1]
        if _last in _arr[:-1]:
            _prev_occurance = [i for i,v in enumerate(_arr[:-1]) if v == _last][-1]
            _last_occurance = len(_arr[:-1])
            _arr.append(_last_occurance - _prev_occurance)
        else:
            _arr.append(0)
        _counter += 1
    return _arr[-1]

def _calculate_big(arr, nth_num):
    _counter = 0
    _last = arr[-1]
    _last_occurance = len(arr[:-1])
    _dict = {v: i for i, v in enumerate(arr)}
    _helper_dict = dict()
    while _counter < nth_num - len(arr):
        if _last in _dict.keys() and _last_occurance == _dict[_last] and _last not in _helper_dict.keys():
            _last = 0
        else:
            _dict[_last] = _last_occurance - _dict[_last]
            _last = _dict[_last]
        _last_occurance += 1
        if _last in _dict.keys():
            if _last in _helper_dict.keys():
                _dict[_last] = _helper_dict[_last]
            _helper_dict[_last] = _last_occurance
        else:
            _dict[_last] = _last_occurance
        _counter += 1
    return _last

@timer
def solve_problem_1():
    arr = read_input()
    return _calculate(arr, 2020)

@timer
def solve_problem_2():
    arr = read_input()
    return _calculate_big(arr, 30000000)

if __name__ == "__main__":

    print(f"Solution1: {solve_problem_1()}, Solution2: {solve_problem_2()}")