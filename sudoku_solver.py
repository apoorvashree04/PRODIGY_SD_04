import customtkinter as ctk
from tkinter import messagebox

# ======================================
# SETTINGS
# ======================================
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ======================================
# WINDOW
# ======================================
app = ctk.CTk()
app.geometry("750x850")
app.title("🧩 Ultra Sudoku Solver")

# ======================================
# TITLE
# ======================================
title = ctk.CTkLabel(
    app,
    text="🧩 SUDOKU SOLVER",
    font=("Arial", 34, "bold"),
    text_color="cyan"
)

title.pack(pady=20)

# ======================================
# FRAME
# ======================================
frame = ctk.CTkFrame(app)
frame.pack(pady=20)

# ======================================
# GRID ENTRIES
# ======================================
entries = []

for row in range(9):

    row_entries = []

    for col in range(9):

        entry = ctk.CTkEntry(
            frame,
            width=55,
            height=55,
            justify="center",
            font=("Arial", 22, "bold")
        )

        entry.grid(
            row=row,
            column=col,
            padx=3,
            pady=3
        )

        row_entries.append(entry)

    entries.append(row_entries)

# ======================================
# GET BOARD
# ======================================
def get_board():

    board = []

    for row in range(9):

        current_row = []

        for col in range(9):

            value = entries[row][col].get()

            if value == "":
                current_row.append(0)
            else:
                current_row.append(int(value))

        board.append(current_row)

    return board

# ======================================
# DISPLAY BOARD
# ======================================
def display_board(board):

    for row in range(9):

        for col in range(9):

            entries[row][col].delete(0, "end")

            if board[row][col] != 0:

                entries[row][col].insert(
                    0,
                    str(board[row][col])
                )

# ======================================
# FIND EMPTY CELL
# ======================================
def find_empty(board):

    for row in range(9):

        for col in range(9):

            if board[row][col] == 0:
                return row, col

    return None

# ======================================
# CHECK VALID
# ======================================
def is_valid(board, number, position):

    row, col = position

    # Check row
    for i in range(9):

        if board[row][i] == number and i != col:
            return False

    # Check column
    for i in range(9):

        if board[i][col] == number and i != row:
            return False

    # Check box
    box_x = col // 3
    box_y = row // 3

    for i in range(box_y * 3, box_y * 3 + 3):

        for j in range(box_x * 3, box_x * 3 + 3):

            if board[i][j] == number and (i, j) != position:
                return False

    return True

# ======================================
# SOLVE SUDOKU
# ======================================
def solve(board):

    empty = find_empty(board)

    if not empty:
        return True

    row, col = empty

    for number in range(1, 10):

        if is_valid(board, number, (row, col)):

            board[row][col] = number

            if solve(board):
                return True

            board[row][col] = 0

    return False

# ======================================
# SOLVE BUTTON FUNCTION
# ======================================
def solve_puzzle():

    try:

        board = get_board()

        if solve(board):

            display_board(board)

            messagebox.showinfo(
                "Solved",
                "Sudoku solved successfully!"
            )

        else:

            messagebox.showerror(
                "Error",
                "No solution exists!"
            )

    except:

        messagebox.showerror(
            "Error",
            "Please enter valid numbers!"
        )

# ======================================
# CLEAR BOARD
# ======================================
def clear_board():

    for row in range(9):

        for col in range(9):

            entries[row][col].delete(0, "end")

# ======================================
# SAMPLE PUZZLE
# ======================================
def load_sample():

    sample = [
        [5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]
    ]

    display_board(sample)

# ======================================
# BUTTON FRAME
# ======================================
button_frame = ctk.CTkFrame(app)
button_frame.pack(pady=20)

# ======================================
# SOLVE BUTTON
# ======================================
solve_button = ctk.CTkButton(
    button_frame,
    text="🧠 Solve Sudoku",
    command=solve_puzzle,
    width=220,
    height=50,
    font=("Arial", 20, "bold"),
    fg_color="green"
)

solve_button.grid(row=0, column=0, padx=15)

# ======================================
# CLEAR BUTTON
# ======================================
clear_button = ctk.CTkButton(
    button_frame,
    text="🗑 Clear",
    command=clear_board,
    width=180,
    height=50,
    font=("Arial", 20, "bold"),
    fg_color="red"
)

clear_button.grid(row=0, column=1, padx=15)

# ======================================
# SAMPLE BUTTON
# ======================================
sample_button = ctk.CTkButton(
    button_frame,
    text="🎲 Load Sample",
    command=load_sample,
    width=220,
    height=50,
    font=("Arial", 20, "bold"),
    fg_color="purple"
)

sample_button.grid(row=0, column=2, padx=15)

# ======================================
# FOOTER
# ======================================
footer = ctk.CTkLabel(
    app,
    text="💻 Built with Python + Backtracking Algorithm",
    font=("Arial", 15),
    text_color="gray"
)

footer.pack(pady=10)

# ======================================
# RUN APP
# ======================================
app.mainloop()