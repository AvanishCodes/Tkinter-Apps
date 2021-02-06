# Import the libraries
from tkinter import *

# Tkinter root 
root = Tk()
root.title('Adding Windows') # Name of the window

top = Toplevel()     # The window to be opened
top.title('This is the inherited window')
# add elements to a new window
# content = open('files/input.txt', 'r')
with open('files/input.txt', 'r') as file:
    content = file.read().replace('\n', '\n')
lbl = Label(top, text=content)
lbl.pack()


mainloop()