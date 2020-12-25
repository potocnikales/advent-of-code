from utils import read_file, timer

def read_input():
    _input = read_file("day25")

    return (int(_input[0]), int(_input[1]))

def _get_loop_size(key, _const):
    _counter = 0
    _subject = 7
    _num = 1
    while True:
        _num = _num * _subject
        _num %= _const
        _counter += 1
        if _num == key:
            return _counter

def _decrypt(_loop_size, key, _const):
    _num = 1
    for _ in range(_loop_size):
        _num = _num * key
        _num %= 20201227 
    return _num

@timer
def solve_problem_1():
    _const = 20201227
    _card_key, _door_key = read_input()
    _card_loop_size = _get_loop_size(_card_key, _const)
    return _decrypt(_card_loop_size, _door_key, _const)

@timer
def solve_problem_2():
    return "Done"

if __name__ == "__main__":

    print(f"Solution1: {solve_problem_1()}, Solution2: {solve_problem_2()}")