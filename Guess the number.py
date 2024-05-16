import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")

        self.random_number = random.randint(1, 100)

        self.label = tk.Label(root, text="Guess a number between 1 and 100")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, width=10)
        self.entry.pack(pady=5)

        self.guess_button = tk.Button(root, text="Guess", command=self.check_guess)
        self.guess_button.pack(pady=5)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_game)
        self.reset_button.pack(pady=5)

    def check_guess(self):
        try:
            user_guess = int(self.entry.get())
            if user_guess < 1 or user_guess > 100:
                raise ValueError("Out of bounds")

            if user_guess < self.random_number:
                messagebox.showinfo("Result", "Too low! Try again.")
            elif user_guess > self.random_number:
                messagebox.showinfo("Result", "Too high! Try again.")
            else:
                messagebox.showinfo("Result", "Congratulations! You guessed it right!")
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number between 1 and 100.")

    def reset_game(self):
        self.random_number = random.randint(1, 100)
        self.entry.delete(0, tk.END)
        messagebox.showinfo("Game Reset", "The game has been reset. Guess a new number.")

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
