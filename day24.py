from utils import read_file, timer
from collections import defaultdict

def tokenise_line(line: str):
    tokens = []
    token = ""
    for char in line:
        if char in "sn":
            token = char
        else:
            tokens.append(token + char)
            token = ""
    return tokens

def read_input():
    with open("input/" + "day24") as f:
        source = f.read()

    return [tokenise_line(line) for line in source.splitlines()]

def part_one(data):
    tiles = defaultdict(bool)
    for tile in data:
        x = 0
        y = 0
        for direction in tile:
            if direction == "e":
                x += 1
            elif direction == "w":
                x -= 1
            elif direction == "ne":
                x += 0.5
                y -= 1
            elif direction == "nw":
                x -= 0.5
                y -= 1
            elif direction == "se":
                x += 0.5
                y += 1
            elif direction == "sw":
                x -= 0.5
                y += 1
        tiles[x, y] = not tiles[x, y]
    return sum(tiles.values())

def neighbours(tiles, x, y):
    return [
        tiles[x - 0.5, y - 1],
        tiles[x + 0.5, y - 1],
        tiles[x - 1, y],
        tiles[x + 1, y],
        tiles[x - 0.5, y + 1],
        tiles[x + 0.5, y + 1],
    ]


def part_two(data):
    tiles = defaultdict(bool)
    for tile in data:
        x = 0.0
        y = 0
        for direction in tile:
            if direction == "e":
                x += 1
            elif direction == "w":
                x -= 1
            elif direction == "ne":
                x += 0.5
                y -= 1
            elif direction == "nw":
                x -= 0.5
                y -= 1
            elif direction == "se":
                x += 0.5
                y += 1
            elif direction == "sw":
                x -= 0.5
                y += 1
        tiles[x, y] = not tiles[x, y]
    for _ in range(100):
        new_tiles = defaultdict(bool)
        all_positions = [key for key, val in tiles.items() if val]
        all_x = [x for x, y in all_positions]
        all_y = [y for x, y in all_positions]
        min_x = int(min(all_x))
        min_y = min(all_y)
        max_x = int(max(all_x))
        max_y = max(all_y)
        for y in range(min_y - 1, max_y + 2):
            for x in range(min_x - 1 - (y % 2), max_x + 2 - (y % 2)):
                x += 0.0
                if y % 2:
                    x += 0.5
                black_neighbours = sum(neighbours(tiles, x, y))
                if tiles[x, y] and black_neighbours in (1, 2):
                    new_tiles[x, y] = True
                elif (not tiles[x, y]) and black_neighbours == 2:
                    new_tiles[x, y] = True
        tiles = new_tiles
    return sum(tiles.values())

@timer
def solve_problem_1():
    data = read_input()
    return part_one(data)

@timer
def solve_problem_2():
    data = read_input()
    return part_two(data)

if __name__ == "__main__":

    print(f"Solution1: {solve_problem_1()}, Solution2: {solve_problem_2()}")