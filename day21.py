from utils import read_file, timer

def read_input():
    input = read_file("day21")

    revmap = {}
    data = []
    for line in input:
        igs, alls = line.split("(contains")
        igs = set(igs.strip().split())
        alls = alls[:-1].strip().split(",")
        alls = [x.strip() for x in alls]
        for alg in alls:
            if alg not in revmap:
                revmap[alg] = set(igs)
            else:
                revmap[alg] &= igs

        data.append((igs, alls))

    return (revmap, data)

# Taken from (https://github.com/cheran-senthil/PyRival/blob/master/pyrival/graphs/hopcroft_karp.py)
# Apache License 2.0 (https://github.com/cheran-senthil/PyRival/blob/master/LICENSE)
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
    revmap, data = read_input()

    bad = set()
    for v in revmap.values():
        bad |= v

    part1 = 0
    for igs, _ in data:
        for x in igs:
            part1 += x not in bad
    return part1

@timer
def solve_problem_2():
    revmap, data = read_input()

    bad = set()
    for v in revmap.values():
        bad |= v

    algs = list(revmap.keys())
    ings = list(bad)
    algs.sort()
    ings.sort()

    graph = [[] for _ in algs]
    for alg, v in revmap.items():
        for x in v:
            graph[algs.index(alg)].append(ings.index(x))

    m1, _ = hopcroft_karp(graph, len(algs), len(ings))
    return ",".join(ings[x] for x in m1)

if __name__ == "__main__":

    print(f"Solution1: {solve_problem_1()}, Solution2: {solve_problem_2()}")