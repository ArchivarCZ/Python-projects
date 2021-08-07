from tkinter import *
from tkinter import messagebox
import random


root = Tk()
root.title("Tic Tac Toe vs Computer")
#root.geometry("430x400")

btns = []
board_list = []


# Defining the click button function
def click_btn(b):
    if b["text"] == " ":
        b["text"] = "X"
        create_sub_board()
        win()
        C_move()


def C_move():
    global btns
    occupied = True
    while occupied == True:
        choice = random.choice(btns)
        if choice["text"] == " ":
            occupied = False
            if occupied == False:
               choice["text"] = "O"
    create_sub_board()
    win()


# Defining function to determine if the game is a draw
def draw():
    count = 0
    for row in board_list:
        for item in row:
            if item == " ":
                count += 1
    if count  == 0:
        messagebox.showinfo("Tic Tac Toe", "It is a draw!")
        create_board()
        return True
    else:
        return False


# Function to create an empty board
def create_board():
    global btns, b00, b01, b02, b10, b11, b12, b20, b21, b22
    # Creating board buttons
    b00 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="Grey", command=lambda: click_btn(b00))
    b01 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="Grey", command=lambda: click_btn(b01))
    b02 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="Grey", command=lambda: click_btn(b02))

    b10 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="Grey", command=lambda: click_btn(b10))
    b11 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="Grey", command=lambda: click_btn(b11))
    b12 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="Grey", command=lambda: click_btn(b12))

    b20 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="Grey", command=lambda: click_btn(b20))
    b21 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="Grey", command=lambda: click_btn(b21))
    b22 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="Grey", command=lambda: click_btn(b22))

    # Putting board buttons on the screen
    b00.grid(row=2, column=0)
    b01.grid(row=2, column=1)
    b02.grid(row=2, column=2)

    b10.grid(row=3, column=0)
    b11.grid(row=3, column=1)
    b12.grid(row=3, column=2)

    b20.grid(row=4, column=0)
    b21.grid(row=4, column=1)
    b22.grid(row=4, column=2)

    btns = [b00, b01, b02, b10, b11, b12, b20, b21, b22]


# function to create a backend board to check for wins
def create_sub_board():
    global b00, b01, b02, b10, b11, b12, b20, b21, b22, btns, board_list
    board_list = []
    for button in btns:
        board_list.append(button["text"])
    a = board_list[0:3]
    b = board_list[3:6]
    c = board_list[6:]
    board_list = [a, b, c]


# Function to check if someone has won
def win():
    global computer_score, player_score
    P_score = int(player_score.cget("text"))
    C_score = int(computer_score.cget("text"))
    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != " ":
            return True
        else:
            return False

    # horizontal
    for row in board_list:
        if all_same(row):
            messagebox.showinfo("Tic Tac Toe", row[0] + " has won this round!\nIt was a horizontal win!")
            if row[0] == "X":
                player_score["text"] = str(P_score+1)
            elif row[0] == "O":
                computer_score["text"] = str(C_score+1)
            create_board()
            return True

    # vertical
    for col in range(len(board_list[0])):
        check = []
        for row in board_list:
            check.append(row[col])
        if all_same(check):
            messagebox.showinfo("Tic Tac Toe", check[0] + " has won this round!\nIt was a vertical win!")
            if check[0] == "X":
                player_score["text"] = str(P_score+1)
            elif check[0] == "O":
                computer_score["text"] = str(C_score+1)
            create_board()
            return True

    # / diagonal
    diags = []
    for idx, reverse_idx in enumerate(reversed(range(len(board_list)))):
        diags.append(board_list[idx][reverse_idx])

    if all_same(diags):
        messagebox.showinfo("Tic Tac Toe", diags[0] + " has won this round!\nIt was a diagonal win!")
        if diags[0] == "X":
            player_score["text"] = str(P_score+1)
        elif diags[0] == "O":
            computer_score["text"] = str(C_score+1)
        create_board()
        return True

    # \ diagonal
    diags = []
    for ix in range(len(board_list)):
        diags.append(board_list[ix][ix])

    if all_same(diags):
        messagebox.showinfo("Tic Tac Toe", diags[0] + " has won this round!\nIt was a diagonal win!")
        if diags[0] == "X":
            player_score["text"] = str(P_score+1)
        elif diags[0] == "O":
            computer_score["text"] = str(C_score+1)
        create_board()
        return True

    draw()
    return False


# Additional buttons on the screen
my_title_label = Label(root, text="Tic Tac Toe!", font=("Helvetica", 15))
player_score_label = Label(root, text="Player score")
player_score = Label(root, text="0", font=("Helvetica", 15))
computer_score_label = Label(root, text="Computer score")
computer_score = Label(root, text="0", font=("Helvetica", 15))

my_title_label.grid(row=0, column=1, rowspan=2)
player_score_label.grid(row=0, column=0)
player_score.grid(row=1, column=0)
computer_score_label.grid(row=0, column=2)
computer_score.grid(row=1, column=2)

create_board()
root.mainloop()
