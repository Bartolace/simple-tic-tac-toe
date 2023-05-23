from random import randrange


def display_board(board):
    print("+-------" * 3, "+", sep="")
    for row in range(3):
        print("|       " * 3, "|", sep="")
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ", end="")
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")


def make_list_of_free_fields(board):
    free = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['X', 'O']:
                free.append((row, col))
    return free


def enter_move(board):
    ok = False
    while not ok:
        move = input('Escolha um campo para o seu movimento: ')
        ok = len(move) == 1 and move >= '1' and move <= '9'
        if (not ok):
            print("Movimento inválido")
            continue
        move = int(move) - 1
        row = move // 3
        col = move % 3
        sign = board[row][col]
        ok = sign not in ['X', 'O']
        if not ok:
            print("Campo ocupado, escolha outro movimento")
            continue
        board[row][col] = 'O'


def draw_move(board):
    free = make_list_of_free_fields(board)
    ctn = len(free)
    if ctn > 0:
        this = randrange(ctn)
        row, col = free[this]
        board[row][col] = 'X'


def victory_for(board, sgn):
    if sgn == 'X':
        who = 'me'
    elif sgn == 'O':
        who = 'you'
    else:
        who = None
    cross1 = cross2 = True
    for rc in range(3):
        if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn:
            return who
        if board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn:
            return who
        if board[rc][rc] != sgn:
            cross1 = False
        if board[2 - rc][2 - rc] != sgn:
            cross2 = False
    if cross1 or cross2:
        return who
    return None


board = [[3 * j + i + 1 for i in range(3)]
         for j in range(3)]
board[1][1] = 'X'
free = make_list_of_free_fields(board)
human_turn = True
while len(free):
    display_board(board)
    if human_turn:
        enter_move(board)
        victory = victory_for(board, 'O')
    else:
        draw_move(board)
        victory = victory_for(board, 'X')
    if victory != None:
        break
    human_turn = not human_turn
    free = make_list_of_free_fields(board)


display_board(board)
if victory == 'you':
    print('Você ganhou!')
elif victory == 'me':
    print('Eu ganhei!')
else:
    print('Tranca!')
