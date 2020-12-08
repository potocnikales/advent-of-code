from utils import read_file, timer

def read_input():
    input = read_file("day8")
    arr = [x for x in input]
    return arr

def _calculate_accumulator(arr):  
    _sum = 0
    _pos = 0
    _completed_commands_i = []
    while True:
        if _pos >= len(arr):
            break
        _command = arr[_pos].split()
        if _pos in _completed_commands_i:
            break
        _completed_commands_i.append(_pos)
        if _command[0].strip() == "nop":
            _pos += 1
        elif _command[0].strip() == "acc":
            _sum += int(_command[1].strip())
            _pos += 1
        else:
            _pos += int(_command[1].strip())
    return _sum

def _calculate_accumulator_finish(arr):  
    _all_changeable = [it for it, val in enumerate(arr) if val.split()[0].strip() in ["nop", "jmp"]]
    _is_completed = False
    for _changable in _all_changeable:
        _sum = 0
        _pos = 0
        _completed_commands_i = []
        while True:
            if _pos >= len(arr):
                _is_completed = True
                break
            _com, _val = arr[_pos].split()
            if _pos in _completed_commands_i:
                break
            if _changable == _pos:
                if _com == "nop":
                    _com = "jmp"
                else:
                    _com = "nop"
            _completed_commands_i.append(_pos)
            if _com.strip() == "nop":
                _pos += 1
            elif _com.strip() == "acc":
                _sum += int(_val.strip())
                _pos += 1
            else:
                _pos += int(_val.strip())
        if _is_completed:
            break
    return _sum

@timer
def solve_problem_1():
    arr = read_input()
    return _calculate_accumulator(arr)

@timer
def solve_problem_2():
    arr = read_input()
    return _calculate_accumulator_finish(arr)

if __name__ == "__main__":

    print(f"Solution1: {solve_problem_1()}, Solution2: {solve_problem_2()}")