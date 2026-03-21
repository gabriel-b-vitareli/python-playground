import tkinter as tk
import math

PLAYER = "X"
AI = "O"

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Velha 4.0")
        self.board = [" " for _ in range(9)]
        self.buttons = []

        self.status = tk.Label(root, text="Sua vez (X)", font=("Arial", 14))
        self.status.grid(row=3, column=0, columnspan=3, pady=10)

        self.create_board()
        self.reset_button = tk.Button(root, text="Reiniciar", command=self.reset_game)
        self.reset_button.grid(row=4, column=0, columnspan=3, pady=5)

    def create_board(self):
        for i in range(9):
            button = tk.Button(
                self.root,
                text=str(i + 1),
                font=("Arial", 24),
                width=5,
                height=2,
                command=lambda i=i: self.player_move(i)
            )
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

    def player_move(self, index):
        if self.board[index] == " ":
            self.board[index] = PLAYER
            self.buttons[index].config(text="X", fg="red")
            if self.check_winner(PLAYER):
                self.status.config(text="Você venceu!")
                self.disable_buttons()
                return
            if self.check_draw():
                self.status.config(text="Empate!")
                return
            self.status.config(text="IA pensando...")
            self.root.after(300, self.ai_move)

    def ai_move(self):
        move = self.best_move()
        self.board[move] = AI
        self.buttons[move].config(text="O", fg="blue")

        if self.check_winner(AI):
            self.status.config(text="Você perdeu!")
            self.disable_buttons()
            return
        if self.check_draw():
            self.status.config(text="Empate!")
            return

        self.status.config(text="Sua vez (X)")

    def check_winner(self, player):
        win_conditions = [
            [0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]
        ]
        for condition in win_conditions:
            if all(self.board[i] == player for i in condition):
                return True
        return False

    def check_draw(self):
        return " " not in self.board

    def minimax(self, is_maximizing):
        if self.check_winner(AI):
            return 1
        if self.check_winner(PLAYER):
            return -1
        if self.check_draw():
            return 0

        if is_maximizing:
            best_score = -math.inf
            for i in range(9):
                if self.board[i] == " ":
                    self.board[i] = AI
                    score = self.minimax(False)
                    self.board[i] = " "
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = math.inf
            for i in range(9):
                if self.board[i] == " ":
                    self.board[i] = PLAYER
                    score = self.minimax(True)
                    self.board[i] = " "
                    best_score = min(score, best_score)
            return best_score

    def best_move(self):
        best_score = -math.inf
        move = None
        for i in range(9):
            if self.board[i] == " ":
                self.board[i] = AI
                score = self.minimax(False)
                self.board[i] = " "
                if score > best_score:
                    best_score = score
                    move = i
        return move

    def disable_buttons(self):
        for button in self.buttons:
            button.config(state="disabled")

    def reset_game(self):
        self.board = [" " for _ in range(9)]
        for i, button in enumerate(self.buttons):
            button.config(text=str(i + 1), state="normal", fg="black")
        self.status.config(text="Sua vez (X)")

root = tk.Tk()
game = TicTacToe(root)
root.mainloop()
