from utils import read_file, timer

def read_input():
    input = read_file("day11")
    arr = [[y for y in x] for x in input]
    return arr

def _num_adjacent_occupied(arr,i,j):
    _num = 0
    i_len = len(arr)-1
    j_len = len(arr[i])-1
    _i_range = []
    _j_range = []

    if i == 0:
        _i_range = [i,i+1]
    elif i == i_len:
        _i_range = [i-1,i]
    else:
        _i_range = [i-1,i,i+1]

    if j == 0:
        _j_range = [j,j+1]
    elif j == j_len:
        _j_range = [j-1,j]
    else:
        _j_range = [j-1,j,j+1]

    for x in _i_range:
        for y in _j_range:
            if x == i and y == j:
                continue
            else:
                if arr[x][y] == "#":
                    _num += 1
    
    return _num

def _num_first_one_all_dir_occupied(arr,i,j):
    _num = 0
    i_len = len(arr)-1
    j_len = len(arr[i])-1
    _i_iter = i
    _j_iter = j

    while _i_iter <= i_len:
        if _i_iter == i:
            _i_iter += 1
            continue
        else:
            if arr[_i_iter][j] == "#":
                _num += 1
                break
            elif arr[_i_iter][j] == "L":
                break
        _i_iter += 1
    _i_iter = i
    while _i_iter >= 0:
        if _i_iter == i:
            _i_iter -= 1
            continue
        else:
            if arr[_i_iter][j] == "#":
                _num += 1
                break
            elif arr[_i_iter][j] == "L":
                break
        _i_iter -= 1
    _i_iter = i
    
    while _j_iter <= j_len:
        if _j_iter == j:
            _j_iter += 1
            continue
        else:
            if arr[i][_j_iter] == "#":
                _num += 1
                break
            elif arr[i][_j_iter] == "L":
                break
        _j_iter += 1
    _j_iter = j
    while _j_iter >= 0:
        if _j_iter == j:
            _j_iter -= 1
            continue
        else:
            if arr[i][_j_iter] == "#":
                _num += 1
                break
            elif arr[i][_j_iter] == "L":
                break
        _j_iter -= 1
    _j_iter = j

    while _j_iter <= j_len and _i_iter <= i_len:
        if _j_iter == j and _i_iter == i:
            _j_iter += 1
            _i_iter += 1
            continue
        else:
            if arr[_i_iter][_j_iter] == "#":
                _num += 1
                break
            elif arr[_i_iter][_j_iter] == "L":
                break
        _j_iter += 1
        _i_iter += 1
    _j_iter = j
    _i_iter = i
    while _j_iter >= 0 and _i_iter >= 0:
        if _j_iter == j and _i_iter == i:
            _j_iter -= 1
            _i_iter -= 1
            continue
        else:
            if arr[_i_iter][_j_iter] == "#":
                _num += 1
                break
            elif arr[_i_iter][_j_iter] == "L":
                break
        _j_iter -= 1
        _i_iter -= 1
    _j_iter = j
    _i_iter = i

    while _j_iter <= j_len and _i_iter >= 0:
        if _j_iter == j and _i_iter == i:
            _j_iter += 1
            _i_iter -= 1
            continue
        else:
            if arr[_i_iter][_j_iter] == "#":
                _num += 1
                break
            elif arr[_i_iter][_j_iter] == "L":
                break
        _j_iter += 1
        _i_iter -= 1
    _j_iter = j
    _i_iter = i
    while _j_iter >= 0 and _i_iter <= i_len:
        if _j_iter == j and _i_iter == i:
            _j_iter -= 1
            _i_iter += 1
            continue
        else:
            if arr[_i_iter][_j_iter] == "#":
                _num += 1
                break
            elif arr[_i_iter][_j_iter] == "L":
                break
        _j_iter -= 1
        _i_iter += 1

    return _num

def _change_occupancy(arr, i, j, num_matches):
    _seat = "."
    if arr[i][j] == "L":
        if num_matches == 4:
            _num = _num_adjacent_occupied(arr, i, j)
        else: 
            _num = _num_first_one_all_dir_occupied(arr, i, j)
        if _num == 0:
            _seat = "#"
        else:
            _seat = "L"
    elif arr[i][j] == "#":
        if num_matches == 4:
            _num = _num_adjacent_occupied(arr, i, j)
        else:
            _num = _num_first_one_all_dir_occupied(arr, i, j)
        if _num >= num_matches:
            _seat = "L"
        else:
            _seat = "#"
    else:
        pass
    return _seat

def _rounds(arr, num_matches):
    _next_arr =  [x[:] for x in arr]
    _has_changes = False
    for i in range(len(_next_arr)):
        for j in range(len(_next_arr[i])):
            _current_seat_occupancy = _next_arr[i][j]
            _new_seat_occupancy = _change_occupancy(arr, i, j, num_matches)
            if _current_seat_occupancy != _new_seat_occupancy:
                _has_changes = True
                _next_arr[i][j] = _new_seat_occupancy
    if _has_changes:
        return _rounds(_next_arr, num_matches)
    return _next_arr

@timer
def solve_problem_1():
    arr = read_input()
    _num = 0
    _next_arr = _rounds(arr, 4)
    for i in range(len(_next_arr)):
        for j in range(len(_next_arr[i])):
            if _next_arr[i][j] == "#":
                _num += 1
    return _num

@timer
def solve_problem_2():
    arr = read_input()
    _num = 0
    _next_arr = _rounds(arr, 5)
    for i in range(len(_next_arr)):
        for j in range(len(_next_arr[i])):
            if _next_arr[i][j] == "#":
                _num += 1
    return _num

if __name__ == "__main__":

    print(f"Solution1: {solve_problem_1()}, Solution2: {solve_problem_2()}")