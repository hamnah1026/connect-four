import tkinter as tk  # Import the tkinter library for GUI development

class Game:
    def __init__(self):
        # Class attributes for keeping track of game state
        self.row = 0
        self.col = 0
        self.turn_no = 0  # Number of turns taken
        self.current_player = "white"  # Will toggle between "red" and "yellow"

        # GUI setup
        self.root = tk.Tk()
        self.root.geometry("900x700")
        self.root.title("Connect Four")

        # Create the canvas where the game board will be drawn
        self.canvas = tk.Canvas(self.root, bg='white', height=700, width=900)
        self.canvas.pack()

        # Draw the blue rectangle background for the board
        rect = self.canvas.create_rectangle((50, 20, 850, 680), fill='blue')
        self.canvas.pack()

        # Initialize 6x7 grid of None to store references to circle (oval) items
        self.grid_ids = [[None for _ in range(7)] for _ in range(6)]
        cell_size = 100  # Size of each cell

        # Create and place white circles to represent empty slots
        for row in range(6):
            for col in range(7):
                x1 = col * cell_size + 100
                y1 = row * cell_size + 50
                x2 = x1 + cell_size
                y2 = y1 + cell_size

                # Create circle and tag it with its cell position
                circle_id = self.canvas.create_oval((x1 + 10, y1 + 10, x2 - 10, y2 - 10), 
                                                    fill="white", outline="blue", 
                                                    tag=f"cell{row}_{col}")
                self.grid_ids[row][col] = circle_id

                # Bind a click event to each circle that triggers a move
                self.canvas.tag_bind(f"cell{row}_{col}", "<Button-1>", lambda e, c=col: self.makeMove(c))
        
        self.canvas.pack()
        self.root.mainloop()  # Start the GUI event loop

    def makeMove(self, col):
        # Store the selected column
        self.col = col

        # Determine which player's turn it is
        if self.turn_no % 2 == 0:
            self.current_player = "red"
        else:
            self.current_player = "yellow"
        # Place the piece in the lowest available row in the selected column
        for i in range(5, -1, -1):
            if self.canvas.itemcget(self.grid_ids[i][col], "fill") == "white":
                self.turn_no += 1  # Increment turn number
                self.row = i
                self.canvas.itemconfig(self.grid_ids[i][col], fill=self.current_player)
                break
        #Check for Tie
        if self.turn_no == 42:
            self.current_player = "white"
            self.end_game()
        # Check for a win after each move
        if self.checkWin():
            self.end_game()

    def checkWin(self):
        # Check all possible win directions
        return self.horizontal_win() | self.vertical_win() | self.primary_diagonal_win() | self.secondary_diagonal_win()

    def horizontal_win(self):
        # Check horizontally for 4 consecutive pieces
        for col in range(4):
            filled = []
            for i in range(4):
                filled.append(self.canvas.itemcget(self.grid_ids[self.row][col + i], "fill"))
            if all(fill == self.current_player for fill in filled):
                return True
        return False

    def vertical_win(self):
        # Check vertically for 4 consecutive pieces
        for row in range(3):
            filled = []
            for i in range(4):
                filled.append(self.canvas.itemcget(self.grid_ids[row+i][self.col], "fill"))
            if all(fill == self.current_player for fill in filled):
                return True
        return False

    def primary_diagonal_win(self):
        # Check diagonally (top-left to bottom-right) for 4 in a row
        for row in range(3):
            for col in range(4):
                filled = []
                for i in range(4):
                    filled.append(self.canvas.itemcget(self.grid_ids[row+i][col+i], "fill"))
                if all(fill == self.current_player for fill in filled):
                    return True
        return False

    def secondary_diagonal_win(self):
        # Check diagonally (top-right to bottom-left) for 4 in a row
        for row in range(3):
            for col in range(3, 7):
                filled = []
                for i in range(4):
                    filled.append(self.canvas.itemcget(self.grid_ids[row+i][col-i], "fill"))
                if all(color == self.current_player for color in filled):
                    return True
        return False

    def end_game(self):
        # Display a dark overlay and winning message
        self.overlay = self.canvas.create_rectangle(0, 0, 900, 700, fill="black", stipple="gray25", outline="")
        if self.current_player != "white":
            self.win_text = self.canvas.create_text(450, 250, text=f"{self.current_player} wins!",fill=self.current_player, font=("Helvetica", 40, "bold"))
        else:
            self.win_text = self.canvas.create_text(450, 250, text=f"TIE",fill=self.current_player, font=("Helvetica", 40, "bold"))
        # Restart button
        self.restart_btn = tk.Button(self.root, text="Restart", font=("Arial", 16),
                                     bg="white", fg="black", command=start)
        self.canvas.create_window(450, 350, window=self.restart_btn)

# Function to start a new game
def start():
    game = Game()

# Start the game
start()
