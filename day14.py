from utils import read_file, timer
import itertools

def read_input():
    input = read_file("day14")
    arr = [x for x in input]
    return arr

def _decode(arr):
    _mask = ""
    _memory = dict()

    for i in arr:
        _item = i.split("=")
        if _item[0].strip() == "mask":
            _mask = _item[1].strip()
        else:
            _mem_map = _item[0].split()
            _binary = bin(int(_item[1].strip()))
            _val = ""
            for mask,memory in zip(_mask, _binary[2:].zfill(36)):
                if mask == "X":
                    _val += memory
                else:
                    _val += mask    
            _memory[_mem_map[0][4:-1]] = _val

    _sum = 0
    for v in _memory.values():
        _sum += int(v, 2)
    return _sum

def _decode_2(arr):
    _mask = ""
    _memory = dict()

    for i in arr:
        _item = i.split("=")
        if _item[0].strip() == "mask":
            _mask = _item[1].strip()
        else:
            _mem_map = _item[0].split()
            _binary = bin(int(_mem_map[0][4:-1]))
            _value = int(_item[1].strip())
            _address = ""
            for mask,memory in zip(_mask, _binary[2:].zfill(36)):
                if mask == "X" or mask == "1":
                    _address += mask
                else:
                    _address += memory    

            for _a_v in [list(j) for j in itertools.product(range(2), repeat=_address.count("X"))]:
                _current_add = _address
                _counter = 1
                for _c in _a_v:
                    _current_add = _current_add.replace("X", str(_c), 1)
                    _counter += 1
                _memory[int(_current_add, 2)] = _value
            
    _sum = 0
    for v in _memory.values():
        _sum += v
    return _sum

def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+1)
        n -= 1
    return start

@timer
def solve_problem_1():
    arr = read_input()
    return _decode(arr)

@timer
def solve_problem_2():
    arr = read_input()
    return _decode_2(arr)

if __name__ == "__main__":

    print(f"Solution1: {solve_problem_1()}, Solution2: {solve_problem_2()}")