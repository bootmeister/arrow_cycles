def step(pos_x, pos_y, arrow, b_length, b_width):
    board_size = b_length, b_width
    print("before step xy = ", pos_x, pos_y, "arrow =", arrow)
    if arrow == "<":
        pos_x = make_board_range(pos_x - 1, "x", *board_size)
    elif arrow == ">":
        pos_x = make_board_range(pos_x + 1, "x", *board_size)
    elif arrow == "^":
        pos_y = make_board_range(pos_y - 1, "y", *board_size)
    elif arrow == "v":
        pos_y = make_board_range(pos_y + 1, "y", *board_size)
    print("after step xy = ", pos_x, pos_y, "arrow =", arrow)
    return pos_x, pos_y

 
def make_board():
    board = []
    b_length = 0
    with open('board.txt', 'r') as f:
        b_width = len(f.readline()) - 1
        f.seek(0,0)
        for line in f:
            board.append(list(line[0:len(line) - 1]))
            b_length += 1
        b_length -= 1
    return board, b_length, b_width

def make_board_range(pos , way, b_lenght, b_width):
    if way == "x":
        if pos > b_width:
            pos = 0
        elif pos < 0:
            pos = b_width
    elif way == "y":
        if pos > b_lenght:
            pos = 0
        elif pos < 0:
            pos = b_lenght
    return pos

full_loop = False
board, b_length, b_width = make_board()
print(b_length, b_width)
board_size = (b_length, b_width)
start_pos_x = 0
start_pos_y = 0
cycle_len_map = board
while full_loop is False:
    cur_pos_x = start_pos_x
    cur_pos_y = start_pos_y
    first_loop = True
    cycle_len = 0
    while not (start_pos_x == cur_pos_y and start_pos_y == cur_pos_y) and (first_loop is True):
        print("cur_pos_x, cur_pos_y =",  cur_pos_x, cur_pos_y, "board[x,y]", board[cur_pos_y][cur_pos_x])
        cur_pos_x, cur_pos_y = step(cur_pos_x, cur_pos_y, board[cur_pos_y][cur_pos_x], *board_size)
        cycle_len += 1
        if first_loop == True:
            first_loop = False
    if start_pos_x < b_width:
        start_pos_x += 1
    elif start_pos_x >= b_width:
        start_pos_y += 1
        start_pos_x = 0
    elif start_pos_y == b_length:
        start_pos_y = 0
    print("pos_x =", start_pos_x, "pos_y =", start_pos_y)
    print(len("x", cycle_len[start_pos_y], "y", len(cycle_len[start_pos_x])))
    cycle_len_map[start_pos_y][start_pos_x] = cycle_len
    print("len_map[x:y] = ", cycle_len_map[start_pos_y][start_pos_x])
    print("cycle_len = ", cycle_len, "\n")
    if start_pos_x == 0 and start_pos_y == 0:
        full_loop = True

