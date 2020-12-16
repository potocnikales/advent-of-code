from utils import read_file, timer

def read_input():
    input = read_file("day16")

    fields = input[:input.index("")]
    ticket = [int(x) for x in input[input.index("your ticket:")+1:input.index("", input.index("")+1)][0].split(",")]
    tickets = [[int(x) for x in t.split(",")] for t in input[input.index("nearby tickets:")+1:]]

    data = {"fields": fields, "ticket": ticket, "tickets": tickets}
    return data

def field_list(arr):
    _range = []
    for i in arr:
        _range_list = i.split(":")[1].strip().split("or")
        for r in _range_list:
            item = r.strip().split("-")
            _range.append(list(range(int(item[0]), int(item[1])+1)))
    return _range

def _calculate(fields, tickets):
    _not_in_fields = []
    _valid_tickets = []

    for t in tickets:
        _is_valid = True
        for num in t:
            _counter = 0
            for f in fields:
                if num in f:
                    _counter += 1

            if _counter == 0:
                _not_in_fields.append(num)
                _is_valid = False
        
        if _is_valid:
            _valid_tickets.append(t)

    return {"sum": sum(_not_in_fields), "valid_tickets": _valid_tickets}

def _validate(fields, tickets, ticket):
    _dict = {}
    _fields = []
    _f = 0
    while _f < len(fields):
        _f0 = fields[_f]
        _f1 = fields[_f+1]
        _f0.extend(_f1)
        _fields.append(_f0)
        _f += 2

    for i in ticket:
        _in_fields = []

        for f in _fields:
            if i in f:
                _in_fields.append(_fields.index(f))
                
        _dict[ticket.index(i)] = _in_fields

    for t in tickets:
        for num in t:
            _less_fields = []
            _in_fields = _dict[t.index(num)]

            for f in _fields:
                if _fields.index(f) in _in_fields and num in f:
                    _less_fields.append(_fields.index(f))

            _dict[t.index(num)] = _less_fields

    solve_dict(_dict)
    _res = 1
    for k,v in _dict.items():
        if v[0] < 6:
            _res *= ticket[k]
        else:
            continue

    return _res

def solve_dict(_dict):
    _counter = 0
    for k,v in _dict.items():
        if len(v) > 1:
            continue
        else:
            _counter += 1
            for i,val in _dict.items():
                if i == k:
                    continue
                else:
                    if v[0] in val:
                        val.remove(v[0])

    if _counter < 20:
        solve_dict(_dict)     
    return _dict             


@timer
def solve_problem_1():
    arr = read_input()
    return _calculate(field_list(arr["fields"]),arr["tickets"])["sum"]

@timer
def solve_problem_2():
    arr = read_input()
    return _validate(field_list(arr["fields"]), _calculate(field_list(arr["fields"]),arr["tickets"])["valid_tickets"], arr["ticket"])

if __name__ == "__main__":

    print(f"Solution1: {solve_problem_1()}, Solution2: {solve_problem_2()}")