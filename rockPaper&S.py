import tkinter as tk
import random

# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissors")

# Define the global variables
player_score = 0
computer_score = 0
rounds_played = 0
choices = ["rock", "paper", "scissors"]

# function to get random computer choice
def generate_computer_choice():
    return random.choice(choices)

# function to determine the winner of the round
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"
    elif player_choice == "rock":
        if computer_choice == "paper":
            return "computer"
        else:
            return "player"
    elif player_choice == "paper":
        if computer_choice == "scissors":
            return "computer"
        else:
            return "player"
    elif player_choice == "scissors":
        if computer_choice == "rock":
            return "computer"
        else:
            return "player"

# function to start a new game
def play_game(player_choice, player_name):
    global player_score, computer_score, rounds_played
    computer_choice = generate_computer_choice()
    winner = determine_winner(player_choice, computer_choice)

    if winner == "player":
        player_score += 1
        result = "You win!"
    elif winner == "computer":
        computer_score += 1
        result = "You lose!"
    else:
        result = "It's a tie!"

    rounds_played += 1
    
    # Update the labels to show the results
    if rounds_played == 5:
        if player_score > computer_score:
            winner_label.config(text=f"{player_name}, you win the game!")
        elif player_score < computer_score:
            winner_label.config(text="Computer wins the game!", fg="red")
        else:
            winner_label.config(text="It's a tie game!", fg="blue")
        play_again_button.pack(side="top", pady=10)
        rock_button.config(state="disabled")
        paper_button.config(state="disabled")
        scissors_button.config(state="disabled")
    else:
        player_score_label.config(text=f"{player_name} Score: {player_score}")
        computer_score_label.config(text=f"Computer Score: {computer_score}")
        player_result_label.config(text=f"{player_name} Choose {player_choice}")
        computer_result_label.config(text=f"Computer Choose {computer_choice}")
        rounds_label.config(text=f"Round {rounds_played + 1}/5")
        
# function to play again after the game is over
def restart_game():
    global player_score, computer_score, rounds_played
    player_score = 0
    computer_score = 0
    rounds_played = 0
    player_score_label.config(text=f"{player_name} Score: {player_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")
    player_result_label.config(text="")
    computer_result_label.config(text="")
    winner_label.config(text="")
    play_again_button.pack_forget()
    rock_button.config(state="normal")
    paper_button.config(state="normal")
    scissors_button.config(state="normal")
    rounds_label.config(text=f"Round {rounds_played + 1}/5")

# function to get the player's name
def get_player_name():
    global player_name_var
    player_name_var = tk.StringVar()
    name_window = tk.Toplevel(root)
    name_window.title("Enter your name")
    name_label = tk.Label(name_window, text="Please enter your name:", font="Arial 20 bold", fg="blue")
    name_label.pack(side="top", pady=10)
    name_entry = tk.Entry(name_window, textvariable=player_name_var, font="Arial 20 bold", fg="black")
    name_entry.pack(side="top", pady=10)
    
    # function to submit the name
    def submit_name():
        global player_name
        player_name = player_name_var.get()
        name_window.destroy()
        player_score_label.config(text=f"{player_name} Score: {player_score}")
        computer_score_label.config(text=f"Computer Score: {computer_score}")
        rounds_label.config(text=f"Round {rounds_played + 1}/5")

    # button to submit the name
    name_button = tk.Button(name_window, text="Submit", command=submit_name, font="Arial 20 bold", bg="green", fg="white")
    name_button.pack(side="top", pady=10)

# label to display the header
head=tk.Label(text='Rock Paper Scissor',font='arial 35 bold',bg='black',fg='white')
head.pack()

# label to display the player's score
player_score_label = tk.Label(root, text="", font="Arial 20 bold", fg="blue")
player_score_label.pack(side="top", pady=10)

# label to display the computer's score
computer_score_label = tk.Label(root, text="", font="Arial 20 bold", fg="red")
computer_score_label.pack(side="top", pady=10)

# label to display the round number
player_result_label = tk.Label(root, text="", font="Arial 20 bold", fg="blue")
player_result_label.pack(side="top", pady=10)

# label to display the computer's choice
computer_result_label = tk.Label(root, text="", font="Arial 20 bold", fg="red")
computer_result_label.pack(side="top", pady=10)

# winner label to display the winner
winner_label = tk.Label(root, text="", font="Arial 20 bold")
winner_label.pack(side="top", pady=10)

# image for rock, paper, and scissors
rock_img = tk.PhotoImage(file="rock2.png")
paper_img = tk.PhotoImage(file="paper2.png")
scissors_img = tk.PhotoImage(file="scissors2.png")



# Button to play the game again
play_again_button = tk.Button(root, text="Play Again", command=restart_game, font="Arial 20 bold", fg="green")
play_again_button.pack(side="top", pady=10)

# Round label to show which round the game is on
rounds_label = tk.Label(root, text="", font="Arial 20 bold", fg="blue")
rounds_label.pack(side="top", pady=10)

# Button to play rock
rock_button = tk.Button(root, image=rock_img, command=lambda: play_game("rock", player_name_var.get()))
rock_button.pack(side="left", padx=10)

# Button to play paper
paper_button = tk.Button(root, image=paper_img, command=lambda: play_game("paper", player_name_var.get()))
paper_button.pack(side="left", padx=10)

# Button to play scissors
scissors_button = tk.Button(root, image=scissors_img, command=lambda: play_game("scissors", player_name_var.get()))
scissors_button.pack(side="left", padx=10)


# Start the program
get_player_name()
root.mainloop()