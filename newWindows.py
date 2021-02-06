# Import the libraries
from tkinter import *
from PIL import ImageTk, Image

# Tkinter root 
root = Tk()
root.title('Adding Windows') # Name of the window

global myImage

# Define a function to open a new window
def newWindow():
    top = Toplevel()     # The window to be opened
    top.title('This is the second window')
    global myImage
    myImage = ImageTk.PhotoImage(Image.open('images/AvanishGUPTA.png'))
    myLabel = Label(top, image=myImage).grid(row=0)

    # add elements to a new window
    # Open a file to read
    with open('files/input.txt', 'r') as file:
        content = file.read().replace('\n', '\n')
    # Insert the contents of a file into a label
    lbl = Label(top, text=content)
    lbl.grid(row=1)
    # A button for closing the window
    closeBtn = Button(top, text='Close This Window', command=top.destroy).grid(row=2)


btn = Button(root, text = 'Click to open a new window', command=newWindow).pack()

mainloop()