import tkinter as tk
import random
from tkinter import messagebox

BG_COLOR = "#0F172A"          
SURFACE_COLOR = "#1E293B"     
CARD_COLOR = "#334155"        
ACCENT_COLOR = "#14B8A6"      
TEXT_COLOR = "#F8FAFC"        
MUTED_TEXT = "#94A3B8"        
WARNING_COLOR = "#F59E0B"     

FONT_FAMILY = "Segoe UI"
TITLE_FONT = (FONT_FAMILY, 22, "bold")
HEADING_FONT = (FONT_FAMILY, 14, "bold")
NORMAL_FONT = (FONT_FAMILY, 11)
BUTTON_FONT = (FONT_FAMILY, 12, "bold")
SMALL_FONT = (FONT_FAMILY, 10)

# ==================================
# MAIN WINDOW
# ==================================

root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("850x780")
root.resizable(False, False)
root.configure(bg=BG_COLOR)
root.minsize(800, 740)


player_score = 0
computer_score = 0
draw_score = 0
total_games = 0

player_win_rate = 0
computer_win_rate = 0

winning_streak = 0
best_winning_streak = 0
losing_streak = 0

match_history = []


# ==================================
# PLAYER CHOICE
# ==================================

def player_choice(choice):

    global player_score, computer_score, draw_score
    global total_games, player_win_rate, computer_win_rate
    global winning_streak, best_winning_streak, losing_streak

    # Display Player Choice
    player_choice_label.config(
        text=f"Player Choice: {choice}"
    )

    # Generate Computer Choice
    computer = computer_choice()
    computer_choice_label.config(
        text=f"Computer Choice: {computer}"
    )

    # Check Winner
    result = check_winner(choice, computer)

    result_label.config(
        text=f"Result: {result}"
    )

    # Update Scores and Streaks
    if result == "Player Wins":

        player_score += 1
        winning_streak += 1
        losing_streak = 0

        if winning_streak > best_winning_streak:
            best_winning_streak = winning_streak

        result_label.config(fg=ACCENT_COLOR)

    elif result == "Computer Wins":

        computer_score += 1
        losing_streak += 1
        winning_streak = 0

        result_label.config(fg=WARNING_COLOR)

    else:

        draw_score += 1
        winning_streak = 0
        losing_streak = 0

        result_label.config(fg=TEXT_COLOR)

    # Update Total Games
    total_games += 1

    # Calculate Win Rates
    player_win_rate = (player_score / total_games) * 100
    computer_win_rate = (computer_score / total_games) * 100

    # Save Match History
    match = f"{total_games}. You: {choice} | Computer: {computer} | {result}"

    match_history.insert(0, match)

    # Keep Only Last 10 Matches
    if len(match_history) > 100:
        match_history.pop()

    # Update Scoreboard
    player_score_label.config(
        text=f"Player: {player_score}"
    )

    computer_score_label.config(
        text=f"Computer: {computer_score}"
    )

    draw_score_label.config(
        text=f"Draw: {draw_score}"
    )

    total_games_label.config(
        text=f"Total Games: {total_games}"
    )

    # Update Win Rates
    player_win_rate_label.config(
        text=f"Player Win Rate: {player_win_rate:.2f}%"
    )

    computer_win_rate_label.config(
        text=f"Computer Win Rate: {computer_win_rate:.2f}%"
    )

    # Update Streaks
    winning_streak_label.config(
        text=f"Current Win Streak: {winning_streak}"
    )

    best_streak_label.config(
        text=f"Best Win Streak: {best_winning_streak}"
    )

    losing_streak_label.config(
        text=f"Losing Streak: {losing_streak}"
    )

    # Update Match History
    update_history()


# ==================================
# COMPUTER CHOICE
# ==================================

def computer_choice():

    choices = ["Rock", "Paper", "Scissors"]

    return random.choice(choices)


# ==================================
# CHECK WINNER
# ==================================

def check_winner(player, computer):

    if player == computer:
        return "Draw"

    elif player == "Rock" and computer == "Scissors":
        return "Player Wins"

    elif player == "Paper" and computer == "Rock":
        return "Player Wins"

    elif player == "Scissors" and computer == "Paper":
        return "Player Wins"

    else:
        return "Computer Wins"


# ==================================
# NEW ROUND
# ==================================

def new_round():

    player_choice_label.config(
        text="Player Choice: Waiting..."
    )

    computer_choice_label.config(
        text="Computer Choice: Waiting..."
    )

    result_label.config(
        text="Result: Waiting...",
        fg=TEXT_COLOR
    )


# ==================================
# UPDATE HISTORY
# ==================================

def update_history():

    history_listbox.delete(0, tk.END)

    for match in match_history:
        history_listbox.insert(tk.END, match)


# ==================================
# RESET GAME
# ==================================

def reset_game():

    global player_score, computer_score, draw_score
    global total_games, player_win_rate, computer_win_rate
    global winning_streak, best_winning_streak, losing_streak

    answer = messagebox.askyesno(
        "Reset Game",
        "Are you sure you want to reset the game?"
    )

    if not answer:
        return

    # Reset Variables
    player_score = 0
    computer_score = 0
    draw_score = 0
    total_games = 0

    player_win_rate = 0
    computer_win_rate = 0

    winning_streak = 0
    best_winning_streak = 0
    losing_streak = 0

    match_history.clear()

    # Reset Scoreboard
    player_score_label.config(text="Player: 0")
    computer_score_label.config(text="Computer: 0")
    draw_score_label.config(text="Draw: 0")
    total_games_label.config(text="Total Games: 0")

    # Reset Statistics
    player_win_rate_label.config(text="Player Win Rate: 0%")
    computer_win_rate_label.config(text="Computer Win Rate: 0%")

    winning_streak_label.config(text="Current Win Streak: 0")
    best_streak_label.config(text="Best Win Streak: 0")
    losing_streak_label.config(text="Losing Streak: 0")

    # Clear History
    update_history()

    # Clear Current Round
    new_round()


# ==================================
# EXIT GAME
# ==================================

def exit_game():

    answer = messagebox.askyesno(
        "Exit Game",
        "Are you sure you want to exit?"
    )

    if answer:
        root.destroy()


# ==================================
# BUTTON HOVER EFFECT
# ==================================

def add_hover_effect(button, normal_bg, hover_bg, normal_fg, hover_fg):
    """Change a button's colors while the mouse is over it."""
    button.configure(
        bg=normal_bg,
        fg=normal_fg,
        activebackground=hover_bg,
        activeforeground=hover_fg,
        relief="flat",
        cursor="hand2"
    )

    button.bind(
        "<Enter>",
        lambda event: button.configure(bg=hover_bg, fg=hover_fg)
    )

    button.bind(
        "<Leave>",
        lambda event: button.configure(bg=normal_bg, fg=normal_fg)
    )


# ==================================
# HEADER FRAME
# ==================================

header_frame = tk.Frame(
    root,
    bg=SURFACE_COLOR,
    height=85
)

header_frame.pack(
    fill="x",
    padx=10,
    pady=8
)

header_frame.pack_propagate(False)

title_label = tk.Label(
    header_frame,
    text="ROCK PAPER SCISSORS",
    font=TITLE_FONT,
    bg=SURFACE_COLOR,
    fg=TEXT_COLOR
)

title_label.pack(pady=(8, 3))

instruction_label = tk.Label(
    header_frame,
    text="Choose Rock, Paper, or Scissors to play!",
    font=NORMAL_FONT,
    bg=SURFACE_COLOR,
    fg=MUTED_TEXT
)

instruction_label.pack()


# ==================================
# GAME FRAME
# ==================================

game_frame = tk.Frame(
    root,
    bg=SURFACE_COLOR,
    height=205
)

game_frame.pack(
    fill="x",
    padx=10,
    pady=8
)

game_frame.pack_propagate(False)

for i in range(3):
    game_frame.grid_columnconfigure(i, weight=1)


# Rock Button
rock_button = tk.Button(
    game_frame,
    text="Rock",
    font=BUTTON_FONT,
    width=12,
    height=2,
    bg=ACCENT_COLOR,
    fg=BG_COLOR,
    activebackground="#0D9488",
    activeforeground=TEXT_COLOR,
    relief="flat",
    cursor="hand2",
    command=lambda: player_choice("Rock")
)

rock_button.grid(row=0, column=0, padx=10, pady=15)


# Paper Button
paper_button = tk.Button(
    game_frame,
    text="Paper",
    font=BUTTON_FONT,
    width=12,
    height=2,
    bg=ACCENT_COLOR,
    fg=BG_COLOR,
    activebackground="#0D9488",
    activeforeground=TEXT_COLOR,
    relief="flat",
    cursor="hand2",
    command=lambda: player_choice("Paper")
)

paper_button.grid(row=0, column=1, padx=10, pady=15)


# Scissors Button
scissors_button = tk.Button(
    game_frame,
    text="Scissors",
    font=BUTTON_FONT,
    width=12,
    height=2,
    bg=ACCENT_COLOR,
    fg=BG_COLOR,
    activebackground="#0D9488",
    activeforeground=TEXT_COLOR,
    relief="flat",
    cursor="hand2",
    command=lambda: player_choice("Scissors")
)

scissors_button.grid(row=0, column=2, padx=10, pady=15)


# Player Choice
player_choice_label = tk.Label(
    game_frame,
    text="Player Choice: Waiting...",
    font=BUTTON_FONT,
    bg=SURFACE_COLOR,
    fg=TEXT_COLOR
)

player_choice_label.grid(
    row=1, column=0, columnspan=3, pady=4
)


# Computer Choice
computer_choice_label = tk.Label(
    game_frame,
    text="Computer Choice: Waiting...",
    font=BUTTON_FONT,
    bg=SURFACE_COLOR,
    fg=WARNING_COLOR
)

computer_choice_label.grid(
    row=2, column=0, columnspan=3, pady=4
)


# Game Result
result_label = tk.Label(
    game_frame,
    text="Result: Waiting...",
    font=HEADING_FONT,
    bg=SURFACE_COLOR,
    fg=TEXT_COLOR
)

result_label.grid(
    row=3, column=0, columnspan=3, pady=4
)


# ==================================
# SCOREBOARD FRAME
# ==================================

score_frame = tk.Frame(
    root,
    bg=CARD_COLOR,
    height=75
)

score_frame.pack(
    fill="x",
    padx=10,
    pady=8
)

score_frame.pack_propagate(False)

for i in range(4):
    score_frame.grid_columnconfigure(i, weight=1)


player_score_label = tk.Label(
    score_frame,
    text="Player: 0",
    font=HEADING_FONT,
    bg=CARD_COLOR,
    fg=TEXT_COLOR
)

player_score_label.grid(row=0, column=0, pady=20)


draw_score_label = tk.Label(
    score_frame,
    text="Draw: 0",
    font=HEADING_FONT,
    bg=CARD_COLOR,
    fg=TEXT_COLOR
)

draw_score_label.grid(row=0, column=1, pady=20)


computer_score_label = tk.Label(
    score_frame,
    text="Computer: 0",
    font=HEADING_FONT,
    bg=CARD_COLOR,
    fg=WARNING_COLOR
)

computer_score_label.grid(row=0, column=2, pady=20)


total_games_label = tk.Label(
    score_frame,
    text="Total Games: 0",
    font=HEADING_FONT,
    bg=CARD_COLOR,
    fg=ACCENT_COLOR
)

total_games_label.grid(row=0, column=3, pady=20)


# ==================================
# STATISTICS FRAME
# ==================================

statistics_frame = tk.Frame(
    root,
    bg=SURFACE_COLOR,
    height=65
)

statistics_frame.pack(
    fill="x",
    padx=10,
    pady=5
)

statistics_frame.pack_propagate(False)

for i in range(3):
    statistics_frame.grid_columnconfigure(i, weight=1)


player_win_rate_label = tk.Label(
    statistics_frame,
    text="Player Win Rate: 0%",
    font=NORMAL_FONT,
    bg=SURFACE_COLOR,
    fg=TEXT_COLOR
)

player_win_rate_label.grid(row=0, column=0, pady=20)


computer_win_rate_label = tk.Label(
    statistics_frame,
    text="Computer Win Rate: 0%",
    font=NORMAL_FONT,
    bg=SURFACE_COLOR,
    fg=WARNING_COLOR
)

computer_win_rate_label.grid(row=0, column=1, pady=20)


winning_streak_label = tk.Label(
    statistics_frame,
    text="Current Win Streak: 0",
    font=NORMAL_FONT,
    bg=SURFACE_COLOR,
    fg=ACCENT_COLOR
)

winning_streak_label.grid(row=0, column=2, pady=20)


# ==================================
# STREAK FRAME
# ==================================

streak_frame = tk.Frame(
    root,
    bg=CARD_COLOR,
    height=55
)

streak_frame.pack(
    fill="x",
    padx=10,
    pady=5
)

streak_frame.pack_propagate(False)

for i in range(2):
    streak_frame.grid_columnconfigure(i, weight=1)


best_streak_label = tk.Label(
    streak_frame,
    text="Best Win Streak: 0",
    font=BUTTON_FONT,
    bg=CARD_COLOR,
    fg=ACCENT_COLOR
)

best_streak_label.grid(row=0, column=0, pady=15)


losing_streak_label = tk.Label(
    streak_frame,
    text="Losing Streak: 0",
    font=BUTTON_FONT,
    bg=CARD_COLOR,
    fg=WARNING_COLOR
)

losing_streak_label.grid(row=0, column=1, pady=15)


# ==================================
# MATCH HISTORY FRAME
# ==================================

history_frame = tk.Frame(
    root,
    bg=SURFACE_COLOR,
    height=130
)

history_frame.pack(
    fill="x",
    padx=10,
    pady=5
)

history_frame.pack_propagate(False)

history_title = tk.Label(
    history_frame,
    text="RECENT MATCH HISTORY",
    font=NORMAL_FONT,
    bg=SURFACE_COLOR,
    fg=TEXT_COLOR
)

history_title.pack(pady=5)

history_listbox = tk.Listbox(
    history_frame,
    font=SMALL_FONT,
    height=4,
    width=95,
    bg=CARD_COLOR,
    fg=TEXT_COLOR,
    selectbackground=ACCENT_COLOR,
    selectforeground=BG_COLOR,
    relief="flat",
    highlightthickness=1,
    highlightbackground=MUTED_TEXT
)

history_listbox.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=3
)


# ==================================
# CONTROL FRAME
# ==================================

control_frame = tk.Frame(
    root,
    bg=CARD_COLOR,
    height=65
)

control_frame.pack(
    fill="x",
    padx=10,
    pady=8
)

control_frame.pack_propagate(False)


new_round_button = tk.Button(
    control_frame,
    text="New Round",
    font=BUTTON_FONT,
    width=15,
    bg=CARD_COLOR,
    fg=TEXT_COLOR,
    activebackground=ACCENT_COLOR,
    activeforeground=BG_COLOR,
    relief="flat",
    cursor="hand2",
    command=new_round
)

new_round_button.pack(
    side="left",
    padx=90,
    pady=15
)


reset_button = tk.Button(
    control_frame,
    text="Reset Game",
    font=BUTTON_FONT,
    width=15,
    bg=CARD_COLOR,
    fg=TEXT_COLOR,
    activebackground=ACCENT_COLOR,
    activeforeground=BG_COLOR,
    relief="flat",
    cursor="hand2",
    command=reset_game
)

reset_button.pack(
    side="left",
    padx=20,
    pady=15
)


exit_button = tk.Button(
    control_frame,
    text="Exit Game",
    font=BUTTON_FONT,
    width=15,
    bg=CARD_COLOR,
    fg=TEXT_COLOR,
    activebackground=ACCENT_COLOR,
    activeforeground=BG_COLOR,
    relief="flat",
    cursor="hand2",
    command=exit_game
)

exit_button.pack(
    side="left",
    padx=30,
    pady=15
)


# ==================================
# APPLY BUTTON HOVER EFFECTS
# ==================================

# Game buttons: teal becomes a slightly darker teal on hover
add_hover_effect(rock_button, ACCENT_COLOR, "#0D9488", BG_COLOR, TEXT_COLOR)
add_hover_effect(paper_button, ACCENT_COLOR, "#0D9488", BG_COLOR, TEXT_COLOR)
add_hover_effect(scissors_button, ACCENT_COLOR, "#0D9488", BG_COLOR, TEXT_COLOR)

# Control buttons: slate becomes teal on hover
add_hover_effect(new_round_button, CARD_COLOR, ACCENT_COLOR, TEXT_COLOR, BG_COLOR)
add_hover_effect(reset_button, CARD_COLOR, ACCENT_COLOR, TEXT_COLOR, BG_COLOR)

# Exit button: red hover clearly indicates the exit action
add_hover_effect(exit_button, CARD_COLOR, "#DC2626", TEXT_COLOR, TEXT_COLOR)


# ==================================
# RUN APPLICATION
# ==================================

root.mainloop()
