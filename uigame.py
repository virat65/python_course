import tkinter as tk
import random

# Game dictionaries
gamedictionary = {1: "Rock", 2: "Paper", 3: "Scissor"}
reversegamedictionary = {"r": 1, "p": 2, "c": 3}

def play(user_choice):
    computer_choice = random.choice(["r", "p", "c"])
    computer = reversegamedictionary[computer_choice]
    user = reversegamedictionary[user_choice]

    result_text.set(f"You chose {gamedictionary[user]} and Computer chose {gamedictionary[computer]}.")

    if computer == user:
        winner_text.set("It's a Draw 🤝")
    elif (computer == 1 and user == 2) or (computer == 2 and user == 3) or (computer == 3 and user == 1):
        winner_text.set("You Win 🎉")
    else:
        winner_text.set("Computer Wins 💻")

# Create main window
root = tk.Tk()
root.title("Stone Paper Scissors Game")
root.geometry("400x400")
root.config(bg="#222831")

# Title Label
tk.Label(root, text="🪨 Stone  📄 Paper  ✂️ Scissors", font=("Arial", 16, "bold"), bg="#222831", fg="#FFD369").pack(pady=20)

# Result Labels
result_text = tk.StringVar()
winner_text = tk.StringVar()

tk.Label(root, textvariable=result_text, font=("Arial", 12), bg="#222831", fg="white").pack(pady=10)
tk.Label(root, textvariable=winner_text, font=("Arial", 14, "bold"), bg="#222831", fg="#00ADB5").pack(pady=10)

# Buttons for user choice
btn_frame = tk.Frame(root, bg="#222831")
btn_frame.pack(pady=20)

tk.Button(btn_frame, text="Rock 🪨", font=("Arial", 12), width=10, command=lambda: play("r"), bg="#393E46", fg="white").grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Paper 📄", font=("Arial", 12), width=10, command=lambda: play("p"), bg="#393E46", fg="white").grid(row=0, column=1, padx=10)
tk.Button(btn_frame, text="Scissor ✂️", font=("Arial", 12), width=10, command=lambda: play("c"), bg="#393E46", fg="white").grid(row=0, column=2, padx=10)

# Exit Button
tk.Button(root, text="Exit", font=("Arial", 12), width=10, command=root.destroy, bg="#FF2E63", fg="white").pack(pady=20)

# Run the app
root.mainloop()
