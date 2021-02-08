# Import the libraries
from tkinter import *

# Tkinter root 
root = Tk()
root.title('Dropdown menu ') # Name of the window
root.geometry("1000x1000")

# Drop down boxes

clicked = StringVar()

# branches = ("CSE", "ECE")

dropBranch = OptionMenu(root, clicked, "CSE", "ECE")
dropBranch.pack()

selectionButoon = Button(root, text="Show Selection")


mainloop()