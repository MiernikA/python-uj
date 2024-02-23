import tkinter as tk
from tkinter import ttk
import random

win_con = {
    'Paper': 'Scissors',
    'Rock': 'Paper',
    'Scissors': 'Rock'
}


def check_winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        return "Draw!"
    elif user_choice == win_con[comp_choice]:
        return "You Win!"
    else:
        return "You Lost!"


def on_button_click(user_choice):
    comp_choice = random.choice(['Rock', 'Paper', 'Scissors'])
    result = check_winner(user_choice, comp_choice)

    user_label.config(text=f"YOU: {user_choice}")
    comp_label.config(text=f"COMP: {comp_choice}")
    result_label.config(text=result)


root = tk.Tk()
root.title("Rock Paper Scissors")

# Styling
style = ttk.Style()
style.configure("TButton", padding=(10, 5), font=('Helvetica', 12))

user_label = ttk.Label(root, text="YOU: ")
user_label.pack(pady=10)

comp_label = ttk.Label(root, text="COMP: ")
comp_label.pack(pady=10)

result_label = ttk.Label(root, text="")
result_label.pack(pady=10)

button_frame = ttk.Frame(root)
button_frame.pack(pady=20)

paper_button = ttk.Button(button_frame, text="Paper", command=lambda: on_button_click("Paper"))
paper_button.grid(row=0, column=0, padx=10)

rock_button = ttk.Button(button_frame, text="Rock", command=lambda: on_button_click("Rock"))
rock_button.grid(row=0, column=1, padx=10)

scissors_button = ttk.Button(button_frame, text="Scissors", command=lambda: on_button_click("Scissors"))
scissors_button.grid(row=0, column=2, padx=10)

root.mainloop()
