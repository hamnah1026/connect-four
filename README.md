# Connect 4 Game

A simple two-player **Connect 4** game implemented in Python.

## How to Play

- The game is played on a **6x7** grid.
- Player 1 uses **O**, and Player 2 uses **Z**.
- Players take turns dropping their piece into one of the **7 columns**.
- The piece falls to the lowest available row in that column.
- The game continues until one player connects **four** pieces in a row, column, or diagonal.

## Installation

No installation required! Just ensure Python is installed on your system.

## Running the Game

To start the game, run the following command in your terminal:

```bash
python connect4.py
```

## Game Rules

1. Players input their names at the start.
2. On each turn, a player selects a column (0-6) to drop their piece.
3. If the chosen column is full, the player must choose another column.
4. The board updates after every valid move.
5. The game checks for a **win condition** in rows, columns, and diagonals after each move.
6. The first player to connect **four** in a row wins.
7. If all tiles are filled without a winner, the game ends in a **draw**.

## Example Gameplay

```
WELCOME TO CONNECT 4 !!!!
Enter Name of Player 1: Alice
Enter Name of Player 2: Bob
Alice play O
Enter Column from 0-6: 3

0   1   2   3   4   5   6
 -   -   -   -   -   -   -   -   -
 -   -   -   -   -   -   -   -   -
 -   -   -   -   -   -   -   -   -
 -   -   -   -   -   -   -   -   -
 -   -   -   -   -   -   -   -   -
 -   -   -   O   -   -   -   -   -
```

## Features

- User-friendly console-based interface.
- Prevents invalid moves.
- Automatically checks for a win after each move.
- Displays an updated board after every turn.

## Future Improvements

- Add an AI opponent.
- Implement a GUI version.
- Enhance input validation with exception handling.

Enjoy the game!

