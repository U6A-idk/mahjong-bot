import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Mahjong Tiles")
root.configure(background = 'White')
root.geometry("1470x700+100+100")

# Mahjong Tiles Input Frame
MainFrame = tk.Frame(root, width=1250, height=490, bg='White', bd=10, relief=RIDGE)
MainFrame.place(x=100, y=360)

# Row 1
keys = [ [PhotoImage(file="MahjongTiles\\bamboo-1.png"), PhotoImage(file="MahjongTiles\\bamboo-2.png"), PhotoImage(file="MahjongTiles\\bamboo-3.png"), PhotoImage(file="MahjongTiles\\bamboo-4.png"), PhotoImage(file="MahjongTiles\\bamboo-5.png"), PhotoImage(file="MahjongTiles\\bamboo-6.png"), PhotoImage(file="MahjongTiles\\bamboo-7.png"), PhotoImage(file="MahjongTiles\\bamboo-8.png"), PhotoImage(file="MahjongTiles\\bamboo-9.png")
          , PhotoImage(file="MahjongTiles\\honors-dong.png"), PhotoImage(file="MahjongTiles\\honors-nan.png"), PhotoImage(file="MahjongTiles\\honors-xi.png"), PhotoImage(file="MahjongTiles\\honors-bei.png"), PhotoImage(file="MahjongTiles\\honors-zhong.png"), PhotoImage(file="MahjongTiles\\honors-fa.png"), PhotoImage(file="MahjongTiles\\honors-bai.png")],

# Row 2
[PhotoImage(file="MahjongTiles\\char-1.png"), PhotoImage(file="MahjongTiles\\char-2.png"), PhotoImage(file="MahjongTiles\\char-3.png"), PhotoImage(file="MahjongTiles\\char-4.png"), PhotoImage(file="MahjongTiles\\char-5.png"), PhotoImage(file="MahjongTiles\\char-6.png"), PhotoImage(file="MahjongTiles\\char-7.png"), PhotoImage(file="MahjongTiles\\char-8.png"), PhotoImage(file="MahjongTiles\\char-9.png")
 , PhotoImage(file="MahjongTiles\\flower-red-1.png"), PhotoImage(file="MahjongTiles\\flower-red-2.png"), PhotoImage(file="MahjongTiles\\flower-red-3.png"), PhotoImage(file="MahjongTiles\\flower-red-4.png")],

# Row 3
[PhotoImage(file="MahjongTiles\\dots-1.png"), PhotoImage(file="MahjongTiles\\dots-2.png"), PhotoImage(file="MahjongTiles\\dots-3.png"), PhotoImage(file="MahjongTiles\\dots-4.png"), PhotoImage(file="MahjongTiles\\dots-5.png"), PhotoImage(file="MahjongTiles\\dots-6.png"), PhotoImage(file="MahjongTiles\\dots-7.png"), PhotoImage(file="MahjongTiles\\dots-8.png"), PhotoImage(file="MahjongTiles\\dots-9.png")
, PhotoImage(file="MahjongTiles\\flower-blue-1.png"), PhotoImage(file="MahjongTiles\\flower-blue-2.png"), PhotoImage(file="MahjongTiles\\flower-blue-3.png"), PhotoImage(file="MahjongTiles\\flower-blue-4.png")]
]

for i, key_row in enumerate(keys):
    for j, key in enumerate(key_row):
        MainFrameButton = tk.Button(MainFrame, image=key, width=63, height=93, command=lambda k=key: TileClick(k)).grid(row=i, column=j)

# FLower Box Input Frame
FlowerBox = tk.Frame(root, width=10, height=2, bg='White', bd=10, relief=RIDGE)
FlowerBox.place(x=60, y=50)

FlowerButton = tk.Button(FlowerBox, text="Flowers", width=10, height=2, command=lambda: Click(FlowerBox, FlowerButton))
FlowerButton.grid(row=0, column=0, padx=10, pady=10)

# Eyes Input Frame
EyesBox = tk.Frame(root, width=10, height=2, bg='White', bd=10, relief=RIDGE)
EyesBox.place(x=400, y=50)

EyesButton = tk.Button(EyesBox, text="Eyes", width=10, height=2, command=lambda: Click(EyesBox, EyesButton))
EyesButton.grid(row=0, column=0, padx=10, pady=10)

# Set 1 Input Frame
Set1Box = tk.Frame(root, width=10, height=2, bg='White', bd=10, relief=RIDGE)
Set1Box.place(x=740, y=50)

Set1Button = tk.Button(Set1Box, text="Set 1", width=10, height=2, command=lambda: Click(Set1Box, Set1Button))
Set1Button.grid(row=0, column=0, padx=10, pady=10)

# Set 2 Input Frame
Set2Box = tk.Frame(root, width=10, height=2, bg='White', bd=10, relief=RIDGE)
Set2Box.place(x=1080, y=50)

Set2Button = tk.Button(Set2Box, text="Set 2", width=10, height=2, command=lambda: Click(Set2Box, Set2Button))
Set2Button.grid(row=0, column=0, padx=10, pady=10)

# Set 3 Input Frame
Set3Box = tk.Frame(root, width=10, height=2, bg='White', bd=10, relief=RIDGE)
Set3Box.place(x=400, y=190)

Set3Button = tk.Button(Set3Box, text="Set 3", width=10, height=2, command=lambda: Click(Set3Box, Set3Button))
Set3Button.grid(row=0, column=0, padx=10, pady=10)

# Set 4 Input Frame
Set4Box = tk.Frame(root, width=10, height=2, bg='White', bd=10, relief=RIDGE)
Set4Box.place(x=740, y=190)

Set4Button = tk.Button(Set4Box, text="Set 4", width=10, height=2, command=lambda: Click(Set4Box, Set4Button))
Set4Button.grid(row=0, column=0, padx=10, pady=10)

# Submit Frame
SubmitBox = tk.Frame(root, width=10, height=2, bg='Green', bd=10, relief=RIDGE)
SubmitBox.place(x=1300, y=600)

SubmitButton = tk.Button(SubmitBox, text="Submit", width=10, height=2, command=lambda: Submit())
SubmitButton.grid(row=0, column=0, padx=10, pady=10)

# Defining some global variables
SelectedBox = None
SelectedButton = None
NumberofTilesSelected = 0
row_number = 0
column_number = 0
FlowerSet = list()
EyesSet = list()
Set1Set = list()
Set2Set = list()
Set3Set = list()
Set4Set = list()

# Function that runs on button click
def Click(selectionbox, selectionbutton):
    FlowerBox.config(bg="White")
    EyesBox.config(bg="White")
    Set1Box.config(bg="White")
    Set2Box.config(bg="White")
    Set3Box.config(bg="White")
    Set4Box.config(bg="White")
    selectionbox.config(bg="Yellow")
    global SelectedBox
    SelectedBox = selectionbox
    global SelectedButton
    SelectedButton = selectionbutton
    global NumberofTilesSelected
    NumberofTilesSelected = 0
    global row_number
    row_number = 0
    global column_number
    column_number = 0

# Function that runs on tile click
def TileClick(key):
    SelectedTile = key
    global TileName
    TileName = str(SelectedTile.cget('file')).removeprefix("MahjongTiles\\").removesuffix(".png")
    global NumberofTilesSelected
    global row_number
    global column_number
    # If box is empty, replace the button with the tile
    if SelectedBox is not None and NumberofTilesSelected == 0:
        SelectedButton.rowconfigure(row_number)
        SelectedButton.columnconfigure(column_number)
        SelectedButton.grid_configure(padx=2, pady=2)
        SelectedButton.config(image=SelectedTile, width=63, height=93)
        # Stores the tile name
        storetiles(TileName)
        NumberofTilesSelected += 1
        if column_number == 3:
            column_number = 0
            row_number += 1
        else:
            column_number += 1
    # If box already has tiles, add the tile alongside the existing tiles
    elif SelectedBox is not None and NumberofTilesSelected != 0:
        NewTile = tk.Button(SelectedBox, image=SelectedTile, width=63, height=93).grid(row=row_number, column=column_number, padx=2, pady=2)
        # Stores the tile name
        storetiles(TileName)
        NumberofTilesSelected += 1
        if column_number == 3:
            column_number = 0
            row_number += 1
        else:
            column_number += 1
    else:
        print("No box selected")

# Function to call back stored tiles
def storetiles(tile):
    if SelectedButton == FlowerButton:
        FlowerSet.append(TileName)
    elif SelectedButton == EyesButton:
        EyesSet.append(TileName)
    elif SelectedButton == Set1Button:
        Set1Set.append(TileName)
    elif SelectedButton == Set2Button:
        Set2Set.append(TileName)
    elif SelectedButton == Set3Button:
        Set3Set.append(TileName)
    elif SelectedButton == Set4Button:
        Set4Set.append(TileName)

# Function to submit the hand
def Submit():
    print("Flowers: " + str(FlowerSet))
    print("Eyes: " + str(EyesSet))
    print("Set 1: " + str(Set1Set))
    print("Set 2: " + str(Set2Set))
    print("Set 3: " + str(Set3Set))
    print("Set 4: " + str(Set4Set))

root.mainloop()