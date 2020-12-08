from utils import read_file, timer

def read_input_any():
    input = read_file("day6")
    _line = ""
    _arr = []
    for x in input:
        _line += x
        if x == "":
            _arr.append(''.join(set(_line)))
            _line = ""
    _arr.append(''.join(set(_line)))
    return _arr

def read_input_all():
    input = read_file("day6")
    _line = ""
    _arr = []
    for x in input:
        _line += " " + "".join(sorted(x))
        if x == "":
            _arr.append(_line.split())
            _line = ""
    _arr.append(_line.split())
    return _arr

def _calculate_any(arr):  
    _sum = 0
    for l in arr:
        _sum += len(l)
    return _sum

def _calculate_all(arr):  
    _sum = 0
    for l in arr:
        _length = len(l)
        _source = l[0]
        _counter = 0
        for c in _source:
            for i in l:
                if c in i:
                    _counter += 1
            if _counter == _length:
                _sum += 1
            _counter = 0
    return _sum

@timer
def solve_problem_1():
    arr = read_input_any()
    return _calculate_any(arr)

@timer
def solve_problem_2():
    arr = read_input_all()
    return _calculate_all(arr)

if __name__ == "__main__":

    print(f"Solution1: {solve_problem_1()}, Solution2: {solve_problem_2()}")