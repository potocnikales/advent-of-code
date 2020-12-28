import math
from collections import defaultdict
from utils import read_file, timer

def read_input():
    with open("input/" + "day20") as f:
        source = f.read()

    tiles = source.split("\n\n")
    return dict((int(tile.splitlines()[0][5:-1]), tile.splitlines()[1:]) for tile in tiles)

def get_image(data):
    edges = defaultdict(set)
    neighbours = defaultdict(set)
    for i, tile in data.items():

        top_edge = tile[0]
        neighbours[i] |= edges[top_edge]
        for neighbour in edges[top_edge]:
            neighbours[neighbour].add(i)
        edges[top_edge].add(i)
        neighbours[i] |= edges[top_edge[::-1]]
        for neighbour in edges[top_edge[::-1]]:
            neighbours[neighbour].add(i)
        edges[top_edge[::-1]].add(i)

        bottom_edge = tile[-1]
        neighbours[i] |= edges[bottom_edge]
        for neighbour in edges[bottom_edge]:
            neighbours[neighbour].add(i)
        edges[bottom_edge].add(i)
        neighbours[i] |= edges[bottom_edge[::-1]]
        for neighbour in edges[bottom_edge[::-1]]:
            neighbours[neighbour].add(i)
        edges[bottom_edge[::-1]].add(i)

        left_edge = "".join(i[0] for i in tile)
        neighbours[i] |= edges[left_edge]
        for neighbour in edges[left_edge]:
            neighbours[neighbour].add(i)
        edges[left_edge].add(i)
        neighbours[i] |= edges[left_edge[::-1]]
        for neighbour in edges[left_edge[::-1]]:
            neighbours[neighbour].add(i)
        edges[left_edge[::-1]].add(i)

        right_edge = "".join(i[-1] for i in tile)
        neighbours[i] |= edges[right_edge]
        for neighbour in edges[right_edge]:
            neighbours[neighbour].add(i)
        edges[right_edge].add(i)
        neighbours[i] |= edges[right_edge[::-1]]
        for neighbour in edges[right_edge[::-1]]:
            neighbours[neighbour].add(i)
        edges[right_edge[::-1]].add(i)
        
    corners = [k for k, v in neighbours.items() if len(v) == 2]
    return edges, neighbours, corners

def flip_x(image):
    return [row[::-1] for row in image]

def flip_y(image):
    return image[::-1]

def rotate(image):
    return [[image[x][y] for x in range(len(image[0]))] for y in range(len(image))]

def monsters(im):
    monsters = 0
    hashes = "\n".join("".join(row) for row in im).count("#")
    for x in range(len(im[0]) - 18):
        for y in range(len(im[0]) - 2):
            if im[y][x : x + 20][18] != "#":
                continue
            if any(monster == "#" and image != monster for monster, image in zip("#    ##    ##    ###", im[y + 1][x : x + 20])):
                continue
            if any(monster == "#" and image != monster for monster, image in zip(" #  #  #  #  #  #   ", im[y + 2][x : x + 20])):
                continue
            monsters += 1
    return monsters, hashes - monsters * 15

def find_monsters(data):
    edges, neighbours, corners = get_image(data)
    rev_edges = defaultdict(set)
    for k, v in edges.items():
        for id in v:
            rev_edges[id].add(k)
    edge_tiles = len([k for k, v in neighbours.items() if len(v) == 3]) // 4
    all_values = set.union(*neighbours.values())
    grid = [[all_values.copy() for i in range(edge_tiles + 2)] for i in range(edge_tiles + 2)]
    grid[0][0] = {corners[0]}
    grid[0][1] = {neighbours[corners[0]].pop()}
    grid[1][0] = neighbours[corners[0]]
    used = set.union(grid[0][0], grid[0][1], grid[1][0])
    while any(len(v) > 1 for row in grid for v in row):
        for y, row in enumerate(grid):
            for x, poss in enumerate(row):
                if len(poss) == 1:
                    continue
                poss -= used
                if x > 0:
                    poss &= set.union(*[neighbours[i] for i in row[x - 1]])
                if y > 0:
                    poss &= set.union(*[neighbours[i] for i in grid[y - 1][x]])
                if len(poss) == 1:
                    used |= poss
                    continue
    image = []
    for y in grid:
        l_idx = next(iter(y[0]))
        c_idx = next(iter(y[1]))
        shared_side = rev_edges[l_idx] & rev_edges[c_idx]
        tile = data[l_idx]
        top_edge = "".join(tile[0])
        bottom_edge = "".join(tile[-1])
        left_edge = "".join(i[0] for i in tile)
        right_edge = "".join(i[-1] for i in tile)
        if top_edge in shared_side:
            tile = flip_x(rotate(tile))
        if bottom_edge in shared_side:
            tile = rotate(tile)
        if left_edge in shared_side:
            tile = flip_x(tile)
        edge = "".join(i[-1] for i in tile)
        row = [tile]
        for last, current in zip(y, y[1:]):
            l_idx = next(iter(last))
            c_idx = next(iter(current))
            shared_side = rev_edges[l_idx] & rev_edges[c_idx]
            tile = data[c_idx]
            top_edge = "".join(tile[0])
            bottom_edge = "".join(tile[-1])
            left_edge = "".join(i[0] for i in tile)
            right_edge = "".join(i[-1] for i in tile)
            if top_edge in shared_side:
                tile = rotate(tile)
            if bottom_edge in shared_side:
                tile = flip_x(rotate(tile))
            if right_edge in shared_side:
                tile = flip_x(tile)
            my_edge = "".join(i[0] for i in tile)
            my_right_edge = "".join(i[-1] for i in tile)
            if my_edge == edge:
                row.append(tile)
                edge = my_right_edge
            else:
                row.append(tile[::-1])
                edge = my_right_edge[::-1]
        processed_row = [[] for i in row[0]]
        for tile in row:
            for prow, trow in zip(processed_row, tile):
                prow.extend(trow[1:-1])
        image.append(processed_row)
    processed_image = []
    c_top = "".join(image[0][0])
    c_bottom = "".join(image[0][-1])
    n_top = "".join(image[1][0])
    n_bottom = "".join(image[1][-1])
    if c_bottom in (n_top, n_bottom):
        processed_image.extend(image[0][1:-1])
        edge = c_bottom
    else:
        processed_image.extend(image[0][::-1][1:-1])
        edge = c_top
    for _, current in zip(image, image[1:]):
        c_top = "".join(current[0])
        c_bottom = "".join(current[-1])
        if c_top == edge:
            processed_image.extend(current[1:-1])
            edge = c_bottom
        else:
            processed_image.extend(flip_y(current)[1:-1])
            edge = c_top
    results = {}
    k,v = monsters(processed_image)
    results[k] = v
    k,v = monsters(flip_y(processed_image))
    results[k] = v
    k,v = monsters(flip_x(processed_image))
    results[k] = v
    k,v = monsters(flip_x(flip_y(processed_image)))
    results[k] = v
    k,v = monsters(rotate(processed_image))
    results[k] = v
    k,v = monsters(flip_y(rotate(processed_image)))
    results[k] = v
    k,v = monsters(flip_x(rotate(processed_image)))
    results[k] = v
    k,v = monsters(flip_x(flip_y(rotate(processed_image))))
    results[k] = v
    return results[max(results)]

@timer
def solve_problem_1():
    data = read_input()
    _, _, corners = get_image(data)
    return math.prod(corners)

@timer
def solve_problem_2():
    data = read_input()
    return find_monsters(data)

if __name__ == "__main__":

    print(f"Solution1: {solve_problem_1()}, Solution2: {solve_problem_2()}")