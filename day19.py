from utils import read_file, timer

def read_input():
    input = read_file("day19")

    _rules = []
    _index = 0
    for i in input:
        if i == "":
            _index = input.index(i)
            break

        _rules.append(i)

    return (_rules, input[_index+1:])

def _matching_rows(rules, rule, row):
    return any(mr == '' for mr in _helper(rules, rule, row))


def _helper(rules, rule, row):
    _rule = rules[rule]
    if isinstance(_rule, str):
        if row.startswith(_rule):
            yield row[len(_rule):]
        return

    for rs in _rule:
        suffixes = [row]
        _new_s = []
        for rule in rs:
            for r in suffixes:
                _new_s.extend(_helper(rules, rule, r))
            suffixes = _new_s
            _new_s = []
        yield from suffixes


def _prepare(data):
    rules = {}
    for row in data:
        l, r = row.split(': ')
        if r.startswith('"'):
            rules[l] = r.strip('"')
        else:
            _rules = r.split(' | ')
            rules[l] = [_rule.split() for _rule in _rules]
    return rules

@timer
def solve_problem_1():
    data = read_input()
    return sum(1 for row in data[1] if _matching_rows(_prepare(data[0]), '0', row))

@timer
def solve_problem_2():
    data = read_input()
    rules = _prepare(data[0])
    rules['8'] = [['42'], ['42', '8']]
    rules['11'] = [['42', '31'], ['42', '11', '31']]
    return sum(1 for row in data[1] if _matching_rows(rules, '0', row))

if __name__ == "__main__":

    print(f"Solution1: {solve_problem_1()}, Solution2: {solve_problem_2()}")