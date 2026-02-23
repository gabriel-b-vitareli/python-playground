import math

RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[1;31m"
BLUE = "\033[1;34m"
GREEN = "\033[1;32m"
PURPLE = "\033[1;35m"
CYAN = "\033[1;36m"

PLAYER = "X"
AI = "O"

board = [" " for _ in range(9)]

def colored(symbol):
    if symbol == PLAYER:
        return RED + BOLD + "X" + RESET
    elif symbol == AI:
        return BLUE + BOLD + "O" + RESET
    else:
        return symbol

def display_cell(i):
    if board[i] == " ":
        return BOLD + str(i + 1) + RESET
    return colored(board[i])

def print_board():
    print()
    print(" " + display_cell(0) + " | " + display_cell(1) + " | " + display_cell(2))
    print(BOLD + "---+---+---" + RESET)
    print(" " + display_cell(3) + " | " + display_cell(4) + " | " + display_cell(5))
    print(BOLD + "---+---+---" + RESET)
    print(" " + display_cell(6) + " | " + display_cell(7) + " | " + display_cell(8))
    print()

def check_winner(player):
    win_conditions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def check_draw():
    return " " not in board

def minimax(is_maximizing):
    if check_winner(AI):
        return 1
    if check_winner(PLAYER):
        return -1
    if check_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = AI
                score = minimax(False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = PLAYER
                score = minimax(True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

def best_move():
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = AI
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    board[move] = AI

def play():
    print(CYAN + BOLD + "JOGO DA VELHA 3.1" + RESET)
    print(CYAN + BOLD + "Você é X (vermelho) | IA é O (azul)" + RESET)

    while True:
        print_board()

        try:
            move = int(input(CYAN + BOLD + "Sua jogada: " + RESET)) - 1
            if move < 0 or move > 8 or board[move] != " ":
                print(RED + BOLD + "Posição inválida!" + RESET)
                continue
        except:
            print(RED + BOLD + "Entrada inválida!" + RESET)
            continue

        board[move] = PLAYER

        if check_winner(PLAYER):
            print_board()
            print(GREEN + BOLD + "Você venceu!" + RESET)
            break
        if check_draw():
            print_board()
            print(PURPLE + BOLD + "Empate!" + RESET)
            break

        best_move()

        if check_winner(AI):
            print_board()
            print(RED + BOLD + "Você perdeu!" + RESET)
            break
        if check_draw():
            print_board()
            print(PURPLE + BOLD + "Empate!" + RESET)
            break

if __name__ == "__main__":
    play()
