import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Крестики-нолики")
        self.current_player = "X"
        self.board = [" "] * 9

        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(master, text=" ", font=('Helvetica', 20), width=5, height=2,
                                   command=lambda row=i, col=j: self.on_click(row, col))
                button.grid(row=i, column=j, sticky="nsew")
                row.append(button)
            self.buttons.append(row)

        reset_button = tk.Button(master, text="Начать заново", command=self.reset)
        reset_button.grid(row=3, column=0, columnspan=3, sticky="nsew")

    def on_click(self, row, col):
        if self.board[row * 3 + col] == " ":
            self.buttons[row][col].config(text=self.current_player)
            self.board[row * 3 + col] = self.current_player
            if self.check_winner():
                messagebox.showinfo("Победа!", f"Игрок {self.current_player} победил!")
                self.reset()
            elif " " not in self.board:
                messagebox.showinfo("Ничья", "Ничья!")
                self.reset()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        lines = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        for line in lines:
            if self.board[line[0]] == self.board[line[1]] == self.board[line[2]] != " ":
                return True
        return False

    def reset(self):
        self.current_player = "X"
        self.board = [" "] * 9
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=" ")


root = tk.Tk()
game = TicTacToe(root)
root.mainloop()
