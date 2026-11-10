<div align="center">
 🎮 ROCK ROYALE

### Rock • Paper • Scissors --- The Ultimate Hand Battle

**Three choices. One winner. Are you ready to rule the arena?**

A feature-rich desktop Rock Paper Scissors game built with **Python &
Tkinter**.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GUI](https://img.shields.io/badge/GUI-Tkinter-14A06F?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Desktop-64748B?style=for-the-badge)
![Dependencies](https://img.shields.io/badge/External_Dependencies-None-0F9D8A?style=for-the-badge)

**Live Score Tracking • Match Statistics • Winning Streaks • Midnight
Elegance Theme**
</div>

------------------------------------------------------------------------

## 🌟 About the Project

**Rock Royale** is a Python desktop game based on the classic Rock Paper
Scissors challenge. Play against the computer, track your performance,
build winning streaks, and review your recent matches --- all through a
modern graphical interface.

The project was created as a hands-on Python and Tkinter learning
journey, combining fundamental programming concepts with practical
desktop GUI development.

## ✨ Features at a Glance

  -----------------------------------------------------------------------
  Feature                             What it does
  ----------------------------------- -----------------------------------
  🪨 **Classic Gameplay**             Play Rock, Paper, or Scissors
                                      against the computer

  🤖 **Computer Opponent**            Generates a random move for every
                                      round

  🏆 **Live Scoreboard**              Tracks player wins, computer wins,
                                      and draws

  📊 **Game Statistics**              Displays total games and
                                      player/computer win rates

  🔥 **Winning Streak**               Tracks the current winning streak
                                      and best streak

  💥 **Losing Streak**                Counts consecutive losses

  📜 **Match History**                Shows the latest 10 match results

  🔄 **New Round**                    Starts another round without
                                      clearing the scores

  ♻️ **Reset Game**                   Resets scores, statistics, streaks,
                                      and match history

  🎨 **Midnight Elegance UI**         Dark navy interface with slate
                                      surfaces and teal accents

  🖱️ **Hover Effects**                Changes button colors when the
                                      mouse enters or leaves

  🚪 **Exit Confirmation**            Asks for confirmation before
                                      closing the game
  -----------------------------------------------------------------------

## 🧰 Technologies & Tools

### Programming Language

-   **Python 3** --- handles the game logic, conditions, functions,
    score tracking, and statistics.

### GUI Library

-   **Tkinter** --- creates the desktop application window and graphical
    interface.

### Python Modules

  Module                 Purpose
  ---------------------- -----------------------------------------
  `tkinter`              Creates the main window and GUI widgets
  `random`               Randomly selects the computer's move
  `tkinter.messagebox`   Displays confirmation dialogs

### Tkinter Widgets & Methods

  Widget / Method   Usage
  ----------------- -----------------------------------------------------
  `Tk()`            Creates the main application window
  `Frame`           Organizes the interface into sections
  `Label`           Displays headings, choices, results, and statistics
  `Button`          Provides clickable game and control buttons
  `Listbox`         Displays recent match history
  `configure()`     Updates widget properties such as colors and text
  `bind()`          Connects mouse events to hover effects
  `mainloop()`      Keeps the GUI running and responsive

### Python Concepts Used

-   Functions, parameters, and return values
-   Variables and global state
-   Conditional statements (`if`, `elif`, `else`)
-   Lists and random selection
-   Lambda functions and callbacks
-   Event handling
-   Updating GUI elements dynamically

## 🚀 Getting Started

### Requirements

-   Python 3.x
-   Tkinter (usually included with standard Python installations)

### Run Locally

**1. Clone the repository**

``` bash
git clone https://github.com/MH-Topu1/Rock,Seasor,paper.git
```

**2. Move into the project folder**

``` bash
cd Rock,Seasor,paper
```

**3. Run the game**

``` bash
python rock_paper_scissors.py
```

If your system uses `python3`, run:

``` bash
python3 rock_paper_scissors.py
```

> **Note:** Replace `rock_paper_scissors.py` with your actual Python
> filename if it is different. Replace the repository URL with your own
> GitHub URL.

## 🎯 How to Play

1.  Launch **Rock Royale**.
2.  Select **Rock**, **Paper**, or **Scissors**.
3.  The computer randomly chooses its move.
4.  The game displays both choices and announces the result.
5.  Your scores, statistics, and streaks update automatically.
6.  Click **New Round** to play again.

### ⚔️ Game Rules

  Your Choice   Beats
  ------------- -------------
  🪨 Rock       ✂️ Scissors
  📄 Paper      🪨 Rock
  ✂️ Scissors   📄 Paper

If both the player and computer choose the same option, the round is a
**Draw**.

## 🎨 UI Theme --- Midnight Elegance

The interface uses a consistent dark color palette for a clean
desktop-game experience.

  Color        Hex Code    Role
  ------------ ----------- --------------------
  Deep Navy    `#0F172A`   Main background
  Slate        `#1E293B`   Primary surfaces
  Card Slate   `#334155`   Secondary surfaces
  Teal         `#14B8A6`   Main accent
  Soft White   `#F8FAFC`   Primary text
  Muted Text   `#94A3B8`   Secondary text
  Amber        `#F59E0B`   Highlights

**Font:** Segoe UI

## 🗺️ Project Structure

``` text
rock-royale/
│
├── rock_paper_scissors.py
└── README.md
```

> This is a basic example. Update the structure if your project contains
> additional files or folders.

## 🔮 Future Improvements

-   🔊 Add sound effects
-   🎚️ Introduce difficulty levels
-   🥇 Add Best-of-5 and Best-of-10 match modes
-   💾 Save match history between sessions
-   🎨 Add more themes and customization options
-   🏅 Introduce achievements and player badges

## 👨‍💻 Learning Outcomes

Building this project provided practical experience with Python
fundamentals and Tkinter GUI development, especially creating widgets,
handling events, using callbacks, and updating the interface
dynamically.

## 📄 License

This project is created for learning and educational purposes. Feel free
to explore, modify, and improve it.

------------------------------------------------------------------------

<div align="center">

 MAKE YOUR MOVE. CLAIM YOUR VICTORY.

**Made with Python 🐍 and Tkinter**
</div>
