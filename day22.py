from utils import read_file, timer

def read_input():
    with open("input/" + "day22") as f:
        source = f.read()

    player1, player2 = source.split('\n\n')

    return ([int(x.strip()) for x in player1.split('\n')[1:]], [int(x.strip()) for x in player2.split('\n')[1:]])

def _simple_combat(player1, player2):
    while bool(player1) and bool(player2):
        cardP1 = player1.pop(0)
        cardP2 = player2.pop(0)
        if cardP1 > cardP2:
            player1.extend([cardP1, cardP2])
        else:
            player2.extend([cardP2, cardP1])

    return (player1, player2)

def _calculate(cards):
    _mul = 1
    _sum = 0
    for _c in reversed(cards):
        _sum += _mul * _c
        _mul += 1
    return _sum

def _advanced_combat(player1, player2, depth=0):
    seen = set()
    while True:
        if (tuple(player1), tuple(player2)) in seen:
            return True, player1
        seen.add((tuple(player1), tuple(player2)))
        if len(player1) and len(player2):
            cardP1 = player1.pop(0)
            cardP2 = player2.pop(0)
            if len(player1) >= cardP1 and len(player2) >= cardP2:
                player1win, _ = _advanced_combat(player1[:cardP1], player2[:cardP2], depth+1)
            else:
                player1win = cardP1 > cardP2
        else:
            player1win = bool(player1)
            return player1win, player1 if player1win else player2

        if player1win:
            player1.extend([cardP1, cardP2])
        else:
            player2.extend([cardP2, cardP1])

@timer
def solve_problem_1():
    player1, player2 = read_input()
    player1, player2 = _simple_combat(player1, player2)
    return _calculate(player1+player2)

@timer
def solve_problem_2():
    player1, player2 = read_input()
    _, player = _advanced_combat(player1, player2)
    return _calculate(player)

if __name__ == "__main__":

    print(f"Solution1: {solve_problem_1()}, Solution2: {solve_problem_2()}")