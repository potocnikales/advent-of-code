from utils import read_file, timer

def read_input():
    input = read_file("day4")
    _line = ""
    _arr = []
    for x in input:
        _line += " " + x
        if x == "":
            _arr.append(_line.split())
            _line = ""
    _arr.append(_line.split())
    return _arr

def _calculate(arr):  
    num = 0
    for l in arr:
        if len(l) == 8:
            num = num + 1
        elif len(l) == 7:
            _valid=False
            for i in l:
                if i.partition(":")[0] == "cid":
                    _valid=False
                    break
                _valid=True
            if _valid:
                num = num + 1
        else:
            pass
    return num

def _validate(_str):
    is_valid = False
    _list = _str.split(":")
    if _list[0] == "byr":
        if len(_list[1]) == 4 and 1920 <= int(_list[1]) <= 2002:
            is_valid = True
    elif _list[0] == "iyr":
        if len(_list[1]) == 4 and 2010 <= int(_list[1]) <= 2020:
            is_valid = True
    elif _list[0] == "eyr":
        if len(_list[1]) == 4 and 2020 <= int(_list[1]) <= 2030:
            is_valid = True
    elif _list[0] == "hgt":
        if _list[1][len(_list[1])-2:] == "cm" and len(_list[1]) == 5 and 150 <= int(_list[1][:3]) <= 193:
            is_valid = True
        elif _list[1][len(_list[1])-2:] == "in" and len(_list[1]) == 4 and 59 <= int(_list[1][:2]) <= 76:
            is_valid = True
    elif _list[0] == "hcl":
        _values = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
        if len(_list[1]) == 7 and _list[1][0] == "#":
            if _list[1][1:].isalnum():
                valid6 = 0
                for c in _list[1][1:]:
                    if c in _values:
                        valid6 += 1
                    if valid6 == 6:
                        is_valid = True
                valid6 = 0
    elif _list[0] == "ecl":
        _values = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        if len(_list[1]) == 3 and _list[1] in _values:
            is_valid = True
    elif _list[0] == "pid":
        if len(_list[1]) == 9 and _list[1].isnumeric():
            is_valid = True
    else:
        is_valid = True
    return is_valid

def _calculate_and_validate(arr):  
    num = 0
    valid8 = 0
    valid7 = 0
    for l in arr:
        if len(l) == 8:
            for i in l:
                _valid = _validate(i)
                if _valid:
                    valid8 += 1
            if valid8 == 8:
                num = num + 1
            valid8 = 0
        elif len(l) == 7:
            for i in l:
                if i.partition(":")[0] == "cid":
                    valid7 -= 1
                else:
                    _valid = _validate(i)
                    if _valid:
                        valid7 += 1
            if valid7 == 7:
                num = num + 1
            valid7 = 0
    return num

@timer
def solve_problem_1():
    arr = read_input()
    return _calculate(arr)

@timer
def solve_problem_2():
    arr = read_input()
    return _calculate_and_validate(arr)

if __name__ == "__main__":

    print(f"Solution1: {solve_problem_1()}, Solution2: {solve_problem_2()}")