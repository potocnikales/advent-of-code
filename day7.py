from utils import read_file, timer

def read_input():
    input = read_file("day7")
    arr = [x for x in input]
    return arr

def get_in_bags(arr, colorArr):
    _delimiter = "contain"
    _del = "bag"
    _returnArr = colorArr.copy()
    for l in arr:
        for i in colorArr:
            if i in l.split(_delimiter)[1]:
                _returnArr.append(l.split(_delimiter)[0].split(_del)[0].strip())
    _returnArr = list(set(_returnArr))
    if len(_returnArr) > len(colorArr):
        return get_in_bags(arr, _returnArr)
    return _returnArr

def _calculate_in_how_many(arr):  
    _bag = "shiny gold"
    _delimiter = "contain"
    _del = "bag"
    _colors = []
    for l in arr:
        if _bag in l.split(_delimiter)[1]:
            _colors.append(l.split(_delimiter)[0].split(_del)[0].strip())
    _colors = list(set(_colors))
    _all_colors = get_in_bags(arr, _colors)
    return len(_all_colors)

def get_bags_in(arr, colorArr, depth):
    _delimiter = "contain"
    _del = "bag"
    _stop = "no other"
    _has_more_data = False
    _bags = []
    _current_arr = colorArr[depth:]
    for l in arr:
        for i in _current_arr:
            _items = []   
            if i[1] in l.split(_delimiter)[0]:
                if _stop not in l.split(_delimiter)[1]: 
                    _items = [[item[:item.find(" ")], item[item.find(" "):].strip(), colorArr.index(i), 0, 0, 1] for item in [element.split(_del)[0].strip() for element in l.split(_delimiter)[1].split(",")]]
                    colorArr[colorArr.index(i)][4] = 1
                    _has_more_data = True      
            for _i in _items:
                _bags.append(_i)    
    if _has_more_data:
        _current_length = len(colorArr)
        for _b in _bags:
            colorArr.append(_b) 
        return get_bags_in(arr, colorArr, _current_length)
    return colorArr

def _calculate_how_many_in(arr):  
    _bag = "shiny gold"
    _delimiter = "contain"
    _del = "bag"
    _stop = "no other"
    for l in arr:
        if _bag in l.split(_delimiter)[0]:
            if _stop not in l.split(_delimiter)[1]: 
                _bags = [[item[:item.find(" ")], item[item.find(" "):].strip(), -1, 0, 0, 0] for item in [element.split(_del)[0].strip() for element in l.split(_delimiter)[1].split(",")]]
    _all_bags = get_bags_in(arr, _bags, 0)
    for _final_b in _all_bags[::-1]:
        _sum = 0
        _parent_val = 1
        _val = int(_final_b[0])
        if _final_b[4] == 1:
            if _final_b[5] == 1:
                _parent_val = int(_all_bags[_final_b[2]][0])
            _sum += (_val + sum([int(item[3]) for item in _all_bags if item[2] == _all_bags.index(_final_b)])) * _parent_val
        else:
            if _final_b[5] == 1:
                _parent_val = int(_all_bags[_final_b[2]][0])
            _sum += _val * _parent_val
        _all_bags[_all_bags.index(_final_b)][3] = _sum
    return sum([int(item[3]) for item in _all_bags if item[2] == -1])

@timer
def solve_problem_1():
    arr = read_input()
    return _calculate_in_how_many(arr)

@timer
def solve_problem_2():
    arr = read_input()
    return _calculate_how_many_in(arr)

if __name__ == "__main__":

    print(f"Solution1: {solve_problem_1()}, Solution2: {solve_problem_2()}")