import tkinter as tk
from tkinter import messagebox
import random

class GuessNumberGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Guess the Number Game")

        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.life_points = 4

        self.create_widgets()

    def create_widgets(self):
        self.label_instruction = tk.Label(self.window, text="Guess the number between 1 and 100:")
        self.label_instruction.pack()

        self.entry_guess = tk.Entry(self.window)
        self.entry_guess.pack()

        self.button_guess = tk.Button(self.window, text="Guess", command=self.check_guess)
        self.button_guess.pack()

        self.label_life_points = tk.Label(self.window, text=f"Life Points: {self.life_points}")
        self.label_life_points.pack()

    def check_guess(self):
        guess = self.entry_guess.get()
        self.entry_guess.delete(0, tk.END)

        if guess.lower() == 'q':
            self.quit_game()
            return

        if not guess.isdigit():
            messagebox.showerror("Error", "Please enter a valid number.")
            return

        guess = int(guess)
        self.attempts += 1

        if guess < self.secret_number:
            messagebox.showinfo("Hint", "Too low! Try again.")
        elif guess > self.secret_number:
            messagebox.showinfo("Hint", "Too high! Try again.")
        else:
            messagebox.showinfo("Congratulations", f"Congratulations! You've guessed the number {self.secret_number} in {self.attempts} attempts!")
            self.restart_game()
            return

        self.life_points -= 1
        self.label_life_points.config(text=f"Life Points: {self.life_points}")

        if self.life_points == 0:
            messagebox.showinfo("Game Over", f"FUCK OFF! The number was {self.secret_number}.")
            self.restart_game()

    def quit_game(self):
        self.window.destroy()

    def restart_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.life_points = 4
        self.label_life_points.config(text=f"Life Points: {self.life_points}")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = GuessNumberGame()
    game.run()
