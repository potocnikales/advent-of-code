from utils import read_file, timer

def read_input():
    input = read_file("day12")
    arr = [x for x in input]
    return arr

def _calculate_turn(degrees):
    _facing_dir = ""

    _mod_deg = degrees % 360

    if _mod_deg == 0:
        _facing_dir = "N"
    elif _mod_deg == 90:
        _facing_dir = "E"
    elif _mod_deg == 180:
        _facing_dir = "S"
    else:
        _facing_dir = "W"

    return _facing_dir

def _calculate(arr):
    _directions = {"N/S":0, "E/W":0, "L/R":90, "F":"E"}
    _sum = 0

    for item in arr:
        if item[0] == "N":
            _directions["N/S"] += int(item[1:])
        elif item[0] == "S":
            _directions["N/S"] -= int(item[1:])
        elif item[0] == "E":
            _directions["E/W"] += int(item[1:])
        elif item[0] == "W":
            _directions["E/W"] -= int(item[1:])
        elif item[0] == "L":
            _directions["L/R"] -= int(item[1:])
            _directions["F"] = _calculate_turn(_directions["L/R"])
        elif item[0] == "R":
            _directions["L/R"] += int(item[1:])
            _directions["F"] = _calculate_turn(_directions["L/R"])
        else:
            if _directions["F"] == "N":
                _directions["N/S"] += int(item[1:])
            elif _directions["F"] == "S":
                _directions["N/S"] -= int(item[1:])
            elif _directions["F"] == "E":
                _directions["E/W"] += int(item[1:])
            elif _directions["F"] == "W":
                _directions["E/W"] -= int(item[1:])

    _sum = abs(_directions["N/S"]) + abs(_directions["E/W"])
    return _sum

def _calculate_waypoint(arr):
    _directions = {"N/S":0, "E/W":0, "L/R":90, "F1":"N", "F2":"E", "F1V":1, "F2V":10}
    _sum = 0

    for item in arr:
        if item[0] == "N":
            if _directions["F1"] == "N":
                _directions["F1V"] += int(item[1:])
            elif _directions["F1"] == "S":
                _directions["F1V"] -= int(item[1:])
            elif _directions["F2"] == "N":
                _directions["F2V"] += int(item[1:])
            elif _directions["F2"] == "S":
                _directions["F2V"] -= int(item[1:])
        elif item[0] == "S":
            if _directions["F1"] == "N":
                _directions["F1V"] -= int(item[1:])
            elif _directions["F1"] == "S":
                _directions["F1V"] += int(item[1:])
            elif _directions["F2"] == "N":
                _directions["F2V"] -= int(item[1:])
            elif _directions["F2"] == "S":
                _directions["F2V"] += int(item[1:])
        elif item[0] == "E":
            if _directions["F1"] == "E":
                _directions["F1V"] += int(item[1:])
            elif _directions["F1"] == "W":
                _directions["F1V"] -= int(item[1:])
            elif _directions["F2"] == "E":
                _directions["F2V"] += int(item[1:])
            elif _directions["F2"] == "W":
                _directions["F2V"] -= int(item[1:])
        elif item[0] == "W":
            if _directions["F1"] == "E":
                _directions["F1V"] -= int(item[1:])
            elif _directions["F1"] == "W":
                _directions["F1V"] += int(item[1:])
            elif _directions["F2"] == "E":
                _directions["F2V"] -= int(item[1:])
            elif _directions["F2"] == "W":
                _directions["F2V"] += int(item[1:])
        elif item[0] == "L":
            _directions["L/R"] -= int(item[1:])
            _directions["F1"] = _calculate_turn(_directions["L/R"]-90)
            _directions["F2"] = _calculate_turn(_directions["L/R"])
        elif item[0] == "R":
            _directions["L/R"] += int(item[1:])
            _directions["F1"] = _calculate_turn(_directions["L/R"]-90)
            _directions["F2"] = _calculate_turn(_directions["L/R"])
        else:
            if _directions["F1"] == "N":
                _directions["N/S"] += int(item[1:]) * _directions["F1V"]
            elif _directions["F1"] == "S":
                _directions["N/S"] -= int(item[1:]) * _directions["F1V"]
            elif _directions["F1"] == "E":
                _directions["E/W"] += int(item[1:]) * _directions["F1V"]
            elif _directions["F1"] == "W":
                _directions["E/W"] -= int(item[1:]) * _directions["F1V"]
            if _directions["F2"] == "N":
                _directions["N/S"] += int(item[1:]) * _directions["F2V"]
            elif _directions["F2"] == "S":
                _directions["N/S"] -= int(item[1:]) * _directions["F2V"]
            elif _directions["F2"] == "E":
                _directions["E/W"] += int(item[1:]) * _directions["F2V"]
            elif _directions["F2"] == "W":
                _directions["E/W"] -= int(item[1:]) * _directions["F2V"]

    _sum = abs(_directions["N/S"]) + abs(_directions["E/W"])
    return _sum

@timer
def solve_problem_1():
    arr = read_input()
    return _calculate(arr)

@timer
def solve_problem_2():
    arr = read_input()
    return _calculate_waypoint(arr)

if __name__ == "__main__":

    print(f"Solution1: {solve_problem_1()}, Solution2: {solve_problem_2()}")