import random
import tkinter as tk
from tkinter import messagebox


class HangmanGame:

    def __init__(self):
        self.count = 6
        self.window = tk.Tk()
        self.choose_word = self.create_word()
        self.hidden_word = []
        self.hangman_canvas = None
        self.canvas_text = None
        self.center_x = 0
        self.canvas_width = 0
        self.setup_window()
        self.create_game()

    def setup_window(self):
        self.window.config(background="SkyBlue4")
        self.window.title("Hangman")
        self.window.geometry("600x800")
        self.window.resizable(False, False)

    def create_game(self):

        self.create_button(self.window)
        self.hangman_screen(self.window)
        self.hidden_text(self.window)
        self.alphabet_bar(self.window)
        self.window.mainloop()

    @classmethod
    def create_word(cls):
        with open("word.txt", "r") as file:
            words = file.read().split(", ")
            return random.choice(words)

    def create_button(self, window):
        button_canvas = tk.Canvas(window, width=580, height=50, borderwidth=0, highlightthickness=1,
                                  background="SkyBlue4", highlightbackground="SkyBlue3")
        button_canvas.pack(side="bottom", pady=20)

        button_configs = [
            {"text": "NEW", "command": self.new_game, "x": 150, "y": 740},
            {"text": "RESTART", "command": self.restart, "x": 250, "y": 740},
            {"text": "QUIT", "command": window.destroy, "x": 380, "y": 740}
        ]

        for config in button_configs:
            button = tk.Button(
                text=config["text"],
                command=config["command"],
                background="Steel Blue",
                borderwidth=0
            )
            button.pack()
            button.place(x=config["x"], y=config["y"])

    def hangman_screen(self, window):
        self.hangman_canvas = tk.Canvas(window, width=300, height=650, borderwidth=0, highlightthickness=1,
                                        highlightbackground="SkyBlue3", background="SkyBlue4")
        self.hangman_canvas.place(x=10, y=10)
        lines = [[100, 600, 270, 600, 10], [170, 50, 270, 50, 10], [268, 45, 268, 605, 10], [170, 45, 170, 70, 5]]
        for line in lines:
            self.hangman_canvas.create_line(line[0:4], fill="black", width=line[4])

    def hidden_text(self, window):
        for i in range(len(self.choose_word)):
            self.hidden_word.append('_')
        self.canvas_width = len(self.choose_word) * 30
        self.canvas_text = tk.Canvas(window, width=self.canvas_width, height=40, borderwidth=0, highlightthickness=1,
                                     highlightbackground="SkyBlue3", background="SkyBlue4")
        self.canvas_text.place(x=10, y=675)

        self.center_x = self.canvas_width // 2

        self.canvas_text.create_text(self.center_x, 20, fill="SkyBlue3", font="Arial 20 bold",
                                     text=' '.join(self.hidden_word))

    def alphabet_bar(self, window):
        alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                    "U",
                    "V", "W", "X", "Y", "Z"]
        x = 350
        y = 200
        for text in alphabet:
            alphabet_button = tk.Button(window, text=text,
                                        command=lambda t=text: self.letter_placement(t),
                                        background="Steel Blue", borderwidth=0, width=1, height=1)

            alphabet_button.pack()
            alphabet_button.place(x=x, y=y)
            x += 50
            if x > 550:
                x = 350
                y += 50

    def letter_placement(self, t):
        if t not in self.choose_word and self.count != 0:
            if self.count == 6:
                self.hangman_canvas.create_oval(130, 70, 210, 140, fill="black", width=5)
            elif self.count == 5:
                self.hangman_canvas.create_line(170, 140, 170, 350, fill="black", width=10)
            elif self.count == 4:
                self.hangman_canvas.create_line(170, 140, 100, 170, fill="black", width=10)
            elif self.count == 3:
                self.hangman_canvas.create_line(170, 140, 240, 170, fill="black", width=10)
            elif self.count == 2:
                self.hangman_canvas.create_line(170, 350, 100, 380, fill="black", width=10)
            elif self.count == 1:
                self.hangman_canvas.create_line(170, 350, 240, 380, fill="black", width=10)
            self.count -= 1
        elif self.count == 0:
            game_play = messagebox.askyesno("GAME OVER", "        Game Over \nDo you want play again ?")
            if game_play:
                self.restart()
        else:
            if t in self.choose_word:
                self.canvas_text.delete("all")
                for character in range(len(self.choose_word)):
                    if self.choose_word[character] == t:
                        self.hidden_word[character] = t

                self.canvas_text.create_text(self.center_x, 20, fill="SkyBlue3", font="Arial 20 bold",
                                             text=' '.join(self.hidden_word))
            if '_' not in self.hidden_word:
                game_play = messagebox.askyesno("Congratulations", "     Congratulations \nDo you want play again ?")
                if game_play:
                    self.restart()

    def new_game(self):
        self.restart()

    def restart(self):
        self.count = 6

        self.hidden_word = []
        self.choose_word = self.create_word()

        self.hangman_canvas.destroy()
        self.canvas_text.destroy()

        self.hangman_screen(self.window)
        self.hidden_text(self.window)


if __name__ == "__main__":
    hangman_game = HangmanGame()