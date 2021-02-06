# Import the libraries
from tkinter import *
from tkinter import messagebox

# Tkinter loop
root = Tk()
root.title('Message Box Program in Tkinter')

def popup():
    messagebox.showinfo("This is my PopUp, Hello, peeps!")

Button(root, text='Popup', command=popup).pack()

root.mainloop()