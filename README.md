# Connect Four Game (Tkinter GUI)

A simple two-player **Connect Four** game implemented in Python with a graphical interface using **tkinter**.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Recording](#recording)
3. [Features](#features)
4. [Installation Instructions](#installation-instructions)
5. [How to Play](#how-to-play)

---

## Project Overview

This **Connect Four** game allows two players to compete in a turn-based game of Connect Four using a 6x7 grid. Players take turns to drop colored discs into columns, aiming to connect four discs in a row, either horizontally, vertically, or diagonally. The game features a graphical user interface (GUI) created with Python’s **Tkinter** library.

The game includes functionality such as win conditions, tie detection, real-time player updates, and a restart option after a game ends.

---

## Recording

You can view a demo of the gameplay below:

https://github.com/user-attachments/assets/1655039b-ee18-4e9b-b30b-a2f5ea4ebf2a

---

## Features

- **Two-player gameplay**: Players alternate turns by clicking on a column to drop their colored discs.
- **Win conditions**: The first player to align four discs in a row (horizontally, vertically, or diagonally) wins.
- **Tie detection**: The game detects when the board is full with no winner and declares a tie.
- **Dynamic game board**: The board automatically updates after each move, visually displaying player moves.
- **Restart option**: After a game concludes, players can restart the game with a button click.

---

## Installation Instructions

No external installation required!  
Ensure you have **Python 3.x** installed. Tkinter comes pre-installed with standard Python distributions.

To run the game:
1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/hamnah1026/connect-four-python.git
    ```
2. Navigate to the project directory and save the game file as `connect4_gui.py` (or any filename you prefer).
3. Run the game using Python:
    ```bash
    python connect4_gui.py
    ```

---

## How to Play

- The game is played on a **6x7** grid.
- Players alternate turns by clicking on a column to drop their piece.
- The disc falls to the **lowest available slot** in the chosen column.
- The first player to connect **four** of their colored discs horizontally, vertically, or diagonally wins the game.
- After a win, the game displays the winner and shows a **Restart** button.
