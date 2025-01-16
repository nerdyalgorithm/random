import tkinter as tk
import random

# Create a window
window = tk.Tk()
window.title("Number Guessing Game")

# Random number generation
number = random.randint(1, 100)
attempts_left = 4

# Function to handle the guess
def check_guess():
    global attempts_left
    try:
        user_guess = int(entry.get())
        if user_guess == number:
            result_label.config(text="Congratulations! You guessed the correct number!")
            result_label.config(fg="green")
            submit_button.config(state="disabled")
        else:
            attempts_left -= 1
            if attempts_left > 0:
                result_label.config(text=f"Wrong guess! You have {attempts_left} attempts left.")
            else:
                result_label.config(text=f"Game over! The correct number was {number}.")
                submit_button.config(state="disabled")
    except ValueError:
        result_label.config(text="Please enter a valid number.")
        result_label.config(fg="red")

# Create UI elements
instructions_label = tk.Label(window, text="Guess the number between 1 and 100:")
instructions_label.pack()

entry = tk.Entry(window)
entry.pack()

submit_button = tk.Button(window, text="Submit Guess", command=check_guess)
submit_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

# Run the app
window.mainloop()
