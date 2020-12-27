from utils import read_file, timer

def read_input():
    input = read_file("day21")

    _map = {}
    _data = []
    for line in input:
        _content, _allergens = line.split("(contains")
        _content = set(_content.strip().split())
        _allergens = _allergens[:-1].strip().split(",")
        _allergens = [x.strip() for x in _allergens]
        for alg in _allergens:
            if alg not in _map:
                _map[alg] = set(_content)
            else:
                _map[alg] &= _content

        _data.append((_content, _allergens))

    _with = set()
    for v in _map.values():
        _with |= v

    return (_map, _data, _with)

# https://en.wikipedia.org/wiki/Hopcroft–Karp_algorithm
def hopcroft_karp(graph, n, m):
    """
    Maximum bipartite matching using Hopcroft-Karp algorithm, running in O(|E| sqrt(|V|))
    """
    assert (n == len(graph))
    match1 = [-1] * n
    match2 = [-1] * m

    # Find a greedy match for possible speed up
    for node in range(n):
        for nei in graph[node]:
            if match2[nei] == -1:
                match1[node] = nei
                match2[nei] = node
                break
    while 1:
        bfs = [node for node in range(n) if match1[node] == -1]
        depth = [-1] * n
        for node in bfs:
            depth[node] = 0

        for node in bfs:
            for nei in graph[node]:
                next_node = match2[nei]
                if next_node == -1:
                    break
                if depth[next_node] == -1:
                    depth[next_node] = depth[node] + 1
                    bfs.append(next_node)
            else:
                continue
            break
        else:
            break

        pointer = [len(c) for c in graph]
        dfs = [node for node in range(n) if depth[node] == 0]
        while dfs:
            node = dfs[-1]
            while pointer[node]:
                pointer[node] -= 1
                nei = graph[node][pointer[node]]
                next_node = match2[nei]
                if next_node == -1:
                    # Augmenting path found
                    while nei != -1:
                        node = dfs.pop()
                        match2[nei], match1[node], nei = node, nei, match1[node]
                    break
                elif depth[node] + 1 == depth[next_node]:
                    dfs.append(next_node)
                    break
            else:
                dfs.pop()
    return match1, match2

@timer
def solve_problem_1():
    _map, _data, _with = read_input()

    _res = 0
    for ingredients, _ in _data:
        for x in ingredients:
            _res += x not in _with
    return _res

@timer
def solve_problem_2():
    _map, _, _with = read_input()

    alergens = list(_map.keys())
    ingredients = list(_with)
    alergens.sort()
    ingredients.sort()

    graph = [[] for _ in alergens]
    for alg, v in _map.items():
        for x in v:
            graph[alergens.index(alg)].append(ingredients.index(x))

    match, _ = hopcroft_karp(graph, len(alergens), len(ingredients))
    return ",".join(ingredients[x] for x in match)

if __name__ == "__main__":

    print(f"Solution1: {solve_problem_1()}, Solution2: {solve_problem_2()}")