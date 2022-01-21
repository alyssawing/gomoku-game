def is_empty(board):
    '''Check if all squares in board are empty'''
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] != ' ':
                return False
    return True


def is_bounded(board, y_end, x_end, length, d_y, d_x):
    '''Check if there's an open square in the direction of the already existing line on either side'''

    y_start = y_end - (d_y * length) + 1
    x_start = x_end - (d_x * length) + 1 #for all directions except (1, -1)

    if (d_y == 1 and d_x == 0):  # top to bottom
        if (y_end - (d_y * length)) < 0 or (
                x_end - (d_x * length)) < 0:  # if iterating backwards goes out of bounds/at an edge
            if board[y_end + d_y][x_end + d_x] == ' ':
                   return "SEMIOPEN"
            else:
                return "CLOSED"
        if y_end == 7:
            if board[y_end - (d_y * length)][x_end - (d_x * length)] == ' ':  # must count backwards since at bottom row
                return "SEMIOPEN"
            else:
                return "CLOSED"
        elif y_end == 0:
            if board[y_end + (d_y * length)][x_end + (d_x * length)] == ' ':
                return "SEMIOPEN"
            else:
                return "CLOSED"
        else:
            if board[y_end + d_y][x_end + d_x] == ' ' and board[y_end - (d_y * length)][x_end - (d_x * length)] == ' ':
                return "OPEN"
            elif board[y_end + d_y][x_end + d_x] == ' ' or board[y_end - (d_y * length)][x_end - (d_x * length)] == ' ':
                return "SEMIOPEN"
            else:
                return "CLOSED"

    if (d_y == 0 and d_x == 1):  # left to right
        if (y_end - (d_y * length)) < 0 or (
                x_end - (d_x * length)) < 0:  # if iterating backwards goes out of bounds/at an edge
            if board[y_end + d_y][x_end + d_x] == ' ':
                return "SEMIOPEN"
            else:
                return "CLOSED"
        if x_end == 7:
            if board[y_end - (d_y * length)][x_end - (d_x * length)] == ' ':  # must count backwards since at bottom row
                return "SEMIOPEN"
            else:
                return "CLOSED"
        elif x_end == 0:
            if board[y_end + (d_y * length)][x_end + (d_x * length)] == ' ':
                return "SEMIOPEN"
            else:
                return "CLOSED"
        else:
            if board[y_end + d_y][x_end + d_x] == ' ' and board[y_end - (d_y * length)][x_end - (d_x * length)] == ' ':
                return "OPEN"
            elif board[y_end + d_y][x_end + d_x] == ' ' or board[y_end - (d_y * length)][x_end - (d_x * length)] == ' ':
                return "SEMIOPEN"
            else:
                return "CLOSED"

    if (d_y == 1 and d_x == 1):  # left down right
        #single corner cases
        if (y_end == 7 and x_end == 0) or (y_end == 0 and x_end == 7):
            return "CLOSED"
        #larger corner cases
        if (x_start == 7 and y_end == 7) or (x_start == 0 and y_end == 7) or (y_start == 0 and x_end == 0) or (y_start == 0 and x_end == 7):
            return "CLOSED"
        elif y_end == 7 or x_end == 7:
            if board[y_end - (d_y * length)][x_end - (d_x * length)] == ' ':
                return "SEMIOPEN"
            else:
                return "CLOSED"
        elif y_end == 0 or x_end == 0:
            if board[y_end + (d_y * length)][x_end + (d_x * length)] == ' ':
                return "SEMIOPEN"
            else:
                return "CLOSED"
        else:
            if (y_end - (d_y * length)) < 0 or (x_end - (d_x * length)) < 0:  # if iterating backwards goes out of bounds/at an edge
                if board[y_end + d_y][x_end + d_x] == ' ':
                    return "SEMIOPEN"
                else:
                    return "CLOSED"
            elif board[y_end + d_y][x_end + d_x] == ' ' and board[y_end - (d_y * length)][
                x_end - (d_x * length)] == ' ':
                return "OPEN"
            elif board[y_end + d_y][x_end + d_x] == ' ' or board[y_end - (d_y * length)][x_end - (d_x * length)] == ' ':
                return "SEMIOPEN"
            else:
                return "CLOSED"

    if (d_y == 1 and d_x == -1):  # right down left
        x_start1 = x_end - ((d_x * length) + 1) #for (1, -1) direction
        #single corner cases
        if (y_end == 0 and x_end == 0) or (y_end == 7 and x_end == 7):
            return "CLOSED"
        #larger corner cases
        if (x_start1 == 7 and y_end == 7) or (x_start1 == 0 and y_end == 7) or (y_start == 0 and x_end == 0) or (y_start == 0 and x_end == 7):
            return "CLOSED"

        elif y_end == 7 or x_end == 0:

                if board[y_end - (d_y * length)][x_end - (d_x * length)] == ' ':
                    return "SEMIOPEN"
                else:
                    return "CLOSED"

        elif y_end == 0 or x_end == 7:
            if board[y_end + (d_y * length)][x_end + (d_x * length)] == ' ':
                return "SEMIOPEN"
            else:
                return "CLOSED"
        else:
            if (y_end - (d_y * length)) < 0 or (x_end - (d_x * length)) < 0 or (x_end - (d_x * length)) >= 8:  # if iterating backwards goes out of bounds/at an edge
                if board[y_end + d_y][x_end + d_x] == ' ':
                    return "SEMIOPEN"
                else:
                    return "CLOSED"
            elif board[y_end + d_y][x_end + d_x] == ' ' and board[y_end - (d_y * length)][
                x_end - (d_x * length)] == ' ':
                return "OPEN"
            elif board[y_end + d_y][x_end + d_x] == ' ' or board[y_end - (d_y * length)][x_end - (d_x * length)] == ' ':
                return "SEMIOPEN"
            else:
                return "CLOSED"


def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    '''Give number of sequences for a specific colour that are both open or semiopen in the form of a tuple'''
    # first value tuple[0] is the count of how many open things there are (use is_bounded) for whatever specifications
    open_seq_count = 0
    semi_open_seq_count = 0
    y_cur = y_start
    x_cur = x_start
    len_count = 0  # counts length of current sequence we're iterating through

    # for rows and columns:
    if (d_y == 1 and d_x == 0) or (d_y == 0 and d_x == 1):
        for i in range(0, 8):
            while 0 <= y_cur < 8 and 0 <= x_cur < 8:
                if board[y_cur][x_cur] == col:
                    len_count += 1
                else:
                    len_count = 0

                if len_count == length and (y_cur < 7 and x_cur < 7):
                    if board[y_cur + d_y][x_cur + d_x] != col:  # ensures not too long sequence
                        if is_bounded(board, y_cur, x_cur, length, d_y, d_x) == 'OPEN':
                            open_seq_count += 1
                        if is_bounded(board, y_cur, x_cur, length, d_y, d_x) == 'SEMIOPEN':
                            semi_open_seq_count += 1
                elif len_count == length and x_cur == 7 and d_y == 1 and d_x == 0 and y_cur < 7:
                    if board[y_cur + d_y][x_cur + d_x] != col:  # ensures not too long sequence
                        if is_bounded(board, y_cur, x_cur, length, d_y, d_x) == 'OPEN':
                            open_seq_count += 1
                        if is_bounded(board, y_cur, x_cur, length, d_y, d_x) == 'SEMIOPEN':
                            semi_open_seq_count += 1
                elif len_count == length and y_cur == 7 and x_cur < 7 and d_y == 0 and d_x == 1:
                    if board[y_cur + d_y][x_cur + d_x] != col:  # ensures not too long sequence
                        if is_bounded(board, y_cur, x_cur, length, d_y, d_x) == 'OPEN':
                            open_seq_count += 1
                        if is_bounded(board, y_cur, x_cur, length, d_y, d_x) == 'SEMIOPEN':
                            semi_open_seq_count += 1

                elif len_count == length and y_cur == 7 and d_y == 1 and d_x == 0:
                    if is_bounded(board, y_cur, x_cur, length, d_y, d_x) == 'SEMIOPEN':
                        semi_open_seq_count += 1

                elif len_count == length and x_cur == 7 and d_y == 0 and d_x == 1:
                    if is_bounded(board, y_cur, x_cur, length, d_y, d_x) == 'SEMIOPEN':
                        semi_open_seq_count += 1

                y_cur += d_y  # updates current positions for iteration
                x_cur += d_x

    # for diagonals:
    if (d_y == 1 and d_x == 1) or (d_y == 1 and d_x == -1):
        for i in range(0, 8):
            while 0 <= y_cur < 8 and 0 <= x_cur < 8:
                if board[y_cur][x_cur] == col:
                    len_count += 1
                else:
                    len_count = 0

                if len_count == length and y_cur < 7 and 0 < x_cur < 7:
                    if board[y_cur + d_y][x_cur + d_x] != col:  # ensures not too long sequence
                        if is_bounded(board, y_cur, x_cur, length, d_y, d_x) == 'OPEN':
                            open_seq_count += 1
                        if is_bounded(board, y_cur, x_cur, length, d_y, d_x) == 'SEMIOPEN':
                            semi_open_seq_count += 1
                elif len_count == length and (y_cur == 7 or x_cur == 7 or x_cur == 0):
                    if is_bounded(board, y_cur, x_cur, length, d_y, d_x) == 'SEMIOPEN':
                        semi_open_seq_count += 1
                y_cur += d_y
                x_cur += d_x

    return (open_seq_count, semi_open_seq_count)


def detect_rows(board, col, length):
    open_seq_count, semi_open_seq_count = 0, 0

    for y_start in range(0, 8):
        tuple1 = detect_row(board, col, y_start, 0, length, 0, 1)  # all covered by right to left
        open_seq_count += tuple1[0]
        semi_open_seq_count += tuple1[1]

        tuple2 = detect_row(board, col, y_start, 0, length, 1, 1)  # all covered by left down from left edge
        open_seq_count += tuple2[0]
        semi_open_seq_count += tuple2[1]

        tuple3 = detect_row(board, col, y_start, 7, length, 1, -1)  # all covered right down from right edge
        open_seq_count += tuple3[0]
        semi_open_seq_count += tuple3[1]

    for x_start in range(0, 8):
        tuple4 = detect_row(board, col, 0, x_start, length, 1, 0)  # all covered by top down
        open_seq_count += tuple4[0]
        semi_open_seq_count += tuple4[1]

    for x_start in range(1, 8):
        tuple5 = detect_row(board, col, 0, x_start, length, 1, 1)  # all covered by left down from top edge
        open_seq_count += tuple5[0]
        semi_open_seq_count += tuple5[1]

    for x_start in range(0, 7):
        tuple6 = detect_row(board, col, 0, x_start, length, 1, -1)  # all covered right down from top edge
        open_seq_count += tuple6[0]
        semi_open_seq_count += tuple6[1]

    return (open_seq_count, semi_open_seq_count)


def search_max(board):
    '''Return empty location tuple (y,x) that will maximize black/AI score as calculated by score() without actually adding it in'''

    dictionary = {}

    for y in range(0, 8):
        for x in range(0, 8):

            if board[y][x] == ' ':
                board[y][x] = 'b'
                # print(board)
                dictionary[y, x] = score(board)
                #print(dictionary.items())
                board[y][x] = ' '
                # print(board)

    #print(dictionary.items())
    (move_y, move_x) = max(dictionary, key=dictionary.get)
    return move_y, move_x


def score(board):
    MAX_SCORE = 100000

    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}

    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)

    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE

    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE

    return (-10000 * (open_w[4] + semi_open_w[4]) +
            500 * open_b[4] +
            50 * semi_open_b[4] +
            -100 * open_w[3] +
            -30 * semi_open_w[3] +
            50 * open_b[3] +
            10 * semi_open_b[3] +
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])


def closed5(board, col, y_start, x_start, length, d_y, d_x):
    y_cur = y_start
    x_cur = x_start
    len_count = 0  # counts length of current sequence we're iterating through
    closed_count = 0

    # for rows and columns:
    if (d_y == 1 and d_x == 0) or (d_y == 0 and d_x == 1):
        for i in range(0, 8):
            while 0 <= y_cur < 8 and 0 <= x_cur < 8:
                if board[y_cur][x_cur] == col:
                    len_count += 1
                else:
                    len_count = 0

                if len_count == length and (y_cur < 7 and x_cur < 7):
                    if board[y_cur + d_y][x_cur + d_x] != col:  # ensures not too long sequence
                        if is_bounded(board, y_cur, x_cur, length, d_y, d_x) == 'CLOSED':
                            closed_count += 1
                elif len_count == length and (y_cur == 7 or x_cur == 7):
                    if is_bounded(board, y_cur, x_cur, length, d_y, d_x) == 'CLOSED':
                        closed_count += 1
                y_cur += d_y  # updates current positions for iteration
                x_cur += d_x

    # for diagonals:
    if (d_y == 1 and d_x == 1) or (d_y == 1 and d_x == -1):
        for i in range(0, 8):
            while 0 <= y_cur < 8 and 0 <= x_cur < 8:
                if board[y_cur][x_cur] == col:
                    len_count += 1
                else:
                    len_count = 0

                if len_count == length and y_cur < 7 and 0 < x_cur < 7:
                    if board[y_cur + d_y][x_cur + d_x] != col:  # ensures not too long sequence
                        if is_bounded(board, y_cur, x_cur, length, d_y, d_x) == 'CLOSED':
                            closed_count += 1
                elif len_count == length and (y_cur == 7 or x_cur == 7 or x_cur == 0):
                    if is_bounded(board, y_cur, x_cur, length, d_y, d_x) == 'CLOSED':
                        closed_count += 1
                y_cur += d_y
                x_cur += d_x

    return closed_count


def detect_closed_rows(board, col, length):
    closed_count = 0

    for y_start in range(0, 8):
        closed_count += closed5(board, col, y_start, 0, length, 0, 1)  # all covered by right to left
        closed_count += closed5(board, col, y_start, 0, length, 1, 1)  # all covered by left down
        closed_count += closed5(board, col, y_start, 7, length, 1, -1)  # all covered right down

    for x_start in range(0, 8):
        closed_count += closed5(board, col, 0, x_start, length, 1, 0)  # all covered by top down
        closed_count += closed5(board, col, 0, x_start, length, 1, 1)  # all covered by left down from top edge
        closed_count += closed5(board, col, 0, x_start, length, 1, -1)  # all covered right down from top edge


    return closed_count

def is_win(board):
    space = None
    for y in range(0, 8):
        for x in range(0, 8):

            # check for closed sequences of 5
            if detect_closed_rows(board, 'w', 5) > 0:
                return "White won"
                break

            elif detect_closed_rows(board, 'b', 5) > 0:
                return 'Black won'
                break

            # use detect rows to see if any open/semiopen sequences of 5 (use length = 5 and if tuple > 0)
            elif detect_rows(board, 'w', 5)[0] > 0 or detect_rows(board, 'w', 5)[1] > 0:
                return "White won"
                break
            elif detect_rows(board, 'b', 5)[0] > 0 or detect_rows(board, 'b', 5)[1] > 0:
                return "Black won"
                break

            # checking for any empty square:
            elif board[y][x] == ' ':
                return "Continue playing"
                space == True
                break

            # no wins, no empty squares; thus, must be full
            elif space == False:
                return "Draw"
                break

        break       #-- KEEPS RETURNING NONE AT THE END OF EACH ONE??



def print_board(board):
    s = "*"
    for i in range(len(board[0]) - 1):
        s += str(i % 10) + "|"
    s += str((len(board[0]) - 1) % 10)
    s += "*\n"

    for i in range(len(board)):
        s += str(i % 10)
        for j in range(len(board[0]) - 1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0]) - 1])

        s += "*\n"
    s += (len(board[0]) * 2 + 1) * "*"

    print(s)


def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "] * sz)
    return board


def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))


def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])

    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)

        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res

        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res


def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col
        y += d_y
        x += d_x


def test_is_empty():
    board = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")


def test_is_bounded():
    board = make_empty_board(8)
    x = 5;
    y = 1;
    d_x = 0;
    d_y = 1;
    length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)

    y_end = 3
    x_end = 5

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")


def test_detect_row():
    board = make_empty_board(8)
    x = 5;
    y = 1;
    d_x = 0;
    d_y = 1;
    length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", 0, x, length, d_y, d_x) == (1, 0):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")


def test_detect_rows():
    board = make_empty_board(8)
    x = 5;
    y = 1;
    d_x = 0;
    d_y = 1;
    length = 3;
    col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col, length) == (1, 0):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")


def test_search_max():
    board = make_empty_board(8)
    x = 5;
    y = 0;
    d_x = 0;
    d_y = 1;
    length = 4;
    col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6;
    y = 0;
    d_x = 0;
    d_y = 1;
    length = 4;
    col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4, 6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")


def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()


def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5;
    x = 2;
    d_x = 0;
    d_y = 1;
    length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)

    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0

    y = 3;
    x = 5;
    d_x = -1;
    d_y = 1;
    length = 2

    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)

    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #

    y = 5;
    x = 3;
    d_x = -1;
    d_y = 1;
    length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b");
    print_board(board);
    analysis(board);

    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #
    #
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0


##############
#
# import numpy as np
#
