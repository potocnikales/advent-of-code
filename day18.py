from utils import timer
import ast, sys

def read_input():
    with open("input/" + "day18") as f:
        source = f.read()
    return source

def _traverse(node, num):
    if isinstance(node, ast.Module):
        for child in node.body:
            _traverse(child, num)
    elif isinstance(node, ast.Expr):
        _traverse(node.value, num)
    elif isinstance(node, ast.BinOp):
        _visit(node, num)
        _traverse(node.left, num)
        _traverse(node.right, num)

def _visit(node, num):
    if num == 1:
        if isinstance(node.op, ast.Sub):
            node.op = ast.Mult()
    else:
        if isinstance(node.op, ast.Add):
            node.op = ast.Mult()
        elif isinstance(node.op, ast.Mult):
            node.op = ast.Add()

def _calculate(source, num):
    tree = ast.parse(source)
    _traverse(tree, num)
    res = 0
    for expr in tree.body:
        val = eval(compile(ast.Expression(expr.value), 'solve_problem_'+str(num), 'eval'))
        res += val
    return res

@timer
def solve_problem_1():
    source = read_input().replace('*', '-')
    return _calculate(source, 1)

@timer
def solve_problem_2():
    source = read_input().translate(str.maketrans('+*', '*+'))
    return _calculate(source, 2)

if __name__ == "__main__":

    print(f"Solution1: {solve_problem_1()}, Solution2: {solve_problem_2()}")