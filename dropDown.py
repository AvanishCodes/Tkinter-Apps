
# Import the libraries
from tkinter import *

# Tkinter root 
root = Tk()
root.title('Dropdown menu ') # Name of the window
root.geometry("1000x1000")

# Drop down boxes


def show():
    nyLabel = Label(root, text=clicked.get()).pack()

clicked = StringVar()
clicked.set(None)

branches = ("CSE", "ECE", "CE", "ME", "CHE", "EE")

# dropBranch = OptionMenu(root, clicked, "CSE", "ECE")
dropBranch = OptionMenu(root, clicked, *branches)
dropBranch.pack()

selectionButoon = Button(root, text="Show Selection", command=show).pack()



mainloop()