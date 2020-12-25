from utils import read_file, timer

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def read_input():
    with open("input/" + "day23") as f:
        source = f.read()

    return list([int(x) for x in source])

def _run(cups):
    N = len(cups)
    up = cups[1:4]
    cups = [cups[0]] + cups[4:]
    dest = cups[0] - 1

    if dest == 0:
        dest = N

    while dest in up:
        dest -= 1
        if dest == 0:
            dest = N

    idx = cups.index(dest)
    cups = cups[:idx+1] + up + cups[idx+1:]
    cups = cups[1:] + [cups[0]]

    return cups

def _go(cur, map, N):
    start3 = cur.next
    last3 = start3.next.next
    end3 = last3.next
    cur.next = end3
    up = [start3.val, start3.next.val, start3.next.next.val]

    dest = cur.val - 1
    if dest == 0:
        dest = N

    while dest in up:
        dest -= 1
        if dest == 0:
            dest = N

    dnode = map[dest]
    last3.next = dnode.next
    dnode.next = start3

    return cur.next

def _arrange(cups):
    for _ in range(100):
        cups = _run(cups)

    idx = cups.index(1)
    cups = cups[idx:] + cups[:idx]

    return ''.join(str(x) for x in cups)[1:]

def _calculate(cups):
    lcups = len(cups)
    N = 1000000
    map = [None]*(N+1)

    last = dummy = Node(-1)
    for i in range(1000000):
        val = cups[i] if i < lcups else i+1
        node = Node(val)
        map[val] = node
        last.next = node
        last = node
    cur = last.next = dummy.next

    for i in range(10000000):
        if i % 10000 == 0:
            pass
        cur = _go(cur, map, N)

    cup1 = map[1]
    x1 = cup1.next.val
    x2 = cup1.next.next.val

    return x1*x2

@timer
def solve_problem_1():
    data = read_input()
    data = _arrange(data)
    return data

@timer
def solve_problem_2():
    data = read_input()
    return _calculate(data)

if __name__ == "__main__":

    print(f"Solution1: {solve_problem_1()}, Solution2: {solve_problem_2()}")