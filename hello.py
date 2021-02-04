# Import the Tkinter Library
from tkinter import *
# import tkinter
    

def main():

    # root Widget
    root = Tk()

    # creating a label widget
    myLabel = Label(root, text="Hello, World!, Tkinter here")

    # Show it on screen
    myLabel.pack()

    root.mainloop()

    return

if __name__ == "__main__":
    main()