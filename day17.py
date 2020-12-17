from utils import read_file, timer

def read_input():
    input = read_file("day17")
    return input

# Conway’s Game of Life
# https://medium.com/@martin.robertandrew/conways-game-of-life-in-python-2900a6dcdc97

def _input_3d(input):
    _3d = set()
    for x, l in enumerate(input):
        for y, c in enumerate(l):
            if c == '#':
                _3d.add((x, y, 0))
    return _3d

def _input_4d(input):
    _4d = set()
    for x, l in enumerate(input):
        for y, c in enumerate(l):
            if c == '#':
                _4d.add((x, y, 0, 0))
    return _4d

def _transform_nd(data, n):
    _trans = []
    for d in range(n):
        lo = min(x[d] for x in data) - 1
        hi = max(x[d] for x in data) + 2
        _trans.append((lo, hi))
    return _trans

def _around_3d(x, y, z):
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                if not (dx == dy == dz == 0):
                    yield (dx + x, dy + y, dz + z)

def _around_4d(x, y, z, w):
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                for dw in range(-1, 2):
                    if not (dx == dy == dz == dw == 0):
                        yield (dx + x, dy + y, dz + z, dw + w)

def _count_3d(data, x, y, z):
    r = 0
    for pos in _around_3d(x, y, z):
        if pos in data:
            r += 1
    return r

def _count_4d(data, x, y, z, w):
    r = 0
    for pos in _around_4d(x, y, z, w):
        if pos in data:
            r += 1
    return r

def _calculate_3d(data):
    _data = set()
    t1, t2, t3 = _transform_nd(data, 3)
    for x in range(t1[0], t1[1]):
        for y in range(t2[0], t2[1]):
            for z in range(t3[0], t3[1]):
                n = _count_3d(data, x, y, z)
                if (x, y, z) in data:
                    if n in [2,3]:
                        _data.add((x, y, z))
                else:
                    if n == 3:
                        _data.add((x, y, z))
    return _data

def _calculate_4d(data):
    _data = set()
    t1, t2, t3, t4 = _transform_nd(data, 4)
    for x in range(t1[0], t1[1]):
        for y in range(t2[0], t2[1]):
            for z in range(t3[0], t3[1]):
                for w in range(t4[0], t4[1]):
                    n = _count_4d(data, x, y, z, w)
                    if (x, y, z, w) in data:
                        if n in [2,3]:
                            _data.add((x, y, z, w))
                    else:
                        if n == 3:
                            _data.add((x, y, z, w))
    return _data

def solve(data, steps, nD):
    _counter = 0
    while _counter < steps:
        if nD == 3:
            data = _calculate_3d(data)
        elif nD == 4:
            data = _calculate_4d(data)
        _counter += 1
    return data

@timer
def solve_problem_1():
    data = solve(_input_3d(read_input()), 6, 3)
    return len(data)

@timer
def solve_problem_2():
    data = solve(_input_4d(read_input()), 6, 4)
    return len(data)

if __name__ == "__main__":

    print(f"Solution1: {solve_problem_1()}, Solution2: {solve_problem_2()}")