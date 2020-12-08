from utils import read_file, timer

def read_input():
    input = read_file("day5")
    arr = [x for x in input]
    return arr

def _calculate(arr):  
    row_num = 0
    column_num = 0
    rows = list(range(128))
    columns = list(range(8))
    resut = []
    for l in arr:
        ticket_row = rows
        ticket_seat = columns
        for c in l[:7]:
            if len(ticket_row) == 2:
                if c == "B":
                    row_num = ticket_row[1]
                else:
                    row_num = ticket_row[0]
            else:        
                half = int(len(ticket_row) / 2)
                if c == "B":
                    ticket_row = ticket_row[half:]
                else:
                    ticket_row = ticket_row[:half]     
        for c in l[7:]:
            if len(ticket_seat) == 2:
                if c == "R":
                    column_num = ticket_seat[1]
                else:
                    column_num = ticket_seat[0]
            else:
                half = int(len(ticket_seat) / 2)
                if c == "R":
                    ticket_seat = ticket_seat[half:]
                else:
                    ticket_seat = ticket_seat[:half]      
        resut.append(row_num * 8 + column_num)     
    return resut

def _calculate_seat(arr):      
    sorted_result = sorted(_calculate(arr))   
    previous = 0
    my_seat = 0
    for r in sorted_result:
        if r > previous + 1:
            my_seat = previous + 1
        previous = r
    return my_seat

@timer
def solve_problem_1():
    arr = read_input()
    return max(_calculate(arr))

@timer
def solve_problem_2():
    arr = read_input()
    return _calculate_seat(arr)

if __name__ == "__main__":

    print(f"Solution1: {solve_problem_1()}, Solution2: {solve_problem_2()}")