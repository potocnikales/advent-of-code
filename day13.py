from utils import read_file, timer
from functools import reduce

def read_input():
    input = read_file("day13")
    arr = [x for x in input]
    return arr

def _calculate(arr):
    _minutes = int(arr[0])
    _buses = [int(x) for x in arr[-1].split(",") if x.isnumeric()]
    _value = _minutes
    _bus_num = 0

    for _bus in _buses:
        _val = _bus - (_minutes % _bus)
        if _val < _value:
            _value = _val
            _bus_num = _bus

    return _value * _bus_num

def _calc_mod_div(_target, _num, _diff, _range):
    _ret = []
    for i in range(_range):
        _mod = _diff % _num
        _full = int(_diff/_num) * _num
        _x = i * _num + (_full + (_num - _mod))
        if _x % _target == 0:
            _ret.append(_x)
    return _ret

def _calc_mod_div_test(_arr, _range):
    _ret = 0
    for i in range(_range):
        _counter = 0
        for e in _arr:
            if i % e[0] == e[1]:
                _counter += 1
        if _counter == len(_arr):
            _ret = i
            break
    return _ret

###################################################################
# https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1
###################################################################

def _calculate_earliest(arr):
    _buses = arr[-1].split(",")
    _values = []
    _mods = []

    for i,_bus in enumerate(_buses):
        if not _bus.isnumeric():
            continue

        _values.append(int(_bus))
        _mods.append(int(_bus)-i)

    return chinese_remainder(_values, _mods)

@timer
def solve_problem_1():
    arr = read_input()
    return _calculate(arr)

@timer
def solve_problem_2():
    arr = read_input()
    return _calculate_earliest(arr)

if __name__ == "__main__":

    print(f"Solution1: {solve_problem_1()}, Solution2: {solve_problem_2()}")