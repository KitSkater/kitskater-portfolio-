import tkinter as tk
import random

class GuessTheNumberGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Guess the Number Game")
        self.root.geometry("400x300")

        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0

        # Label
        self.label = tk.Label(root, text="Guess a number between 1 and 100!", font=("Arial", 14))
        self.label.pack(pady=10)

        # Entry Box
        self.entry = tk.Entry(root, font=("Arial", 14))
        self.entry.pack(pady=5)

        # Guess Button
        self.guess_button = tk.Button(root, text="Guess", font=("Arial", 14), command=self.check_guess)
        self.guess_button.pack(pady=5)

        # Result Label
        self.result_label = tk.Label(root, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

        # Reset Button
        self.reset_button = tk.Button(root, text="Play Again", font=("Arial", 14), command=self.reset_game, state=tk.DISABLED)
        self.reset_button.pack(pady=5)

    def check_guess(self):
        guess = self.entry.get()

        if not guess.isdigit():
            self.result_label.config(text="Enter a valid number!", fg="orange")
            return

        guess = int(guess)
        self.attempts += 1

        if guess < self.number_to_guess:
            self.result_label.config(text="Too low! Try again.", fg="blue")
        elif guess > self.number_to_guess:
            self.result_label.config(text="Too high! Try again.", fg="red")
        else:
            self.result_label.config(text=f"Congratulations! You guessed it in {self.attempts} attempts.", fg="green")
            self.guess_button.config(state=tk.DISABLED)
            self.reset_button.config(state=tk.NORMAL)

    def reset_game(self):
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        self.result_label.config(text="")
        self.entry.delete(0, tk.END)
        self.guess_button.config(state=tk.NORMAL)
        self.reset_button.config(state=tk.DISABLED)

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = GuessTheNumberGame(root)
    root.mainloop()
