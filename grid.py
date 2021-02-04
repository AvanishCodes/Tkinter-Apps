# Import the Tkinter Library
from tkinter import *
# import tkinter
    

def main():

    # root Widget
    root = Tk()

    # creating a label widget
    myLabel1 = Label(root, text="Hello, World!, Tkinter here")
    myLabel2 = Label(root, text="Would you like to play with me?")

    # Show it on screen
    # myLabel.pack()
    myLabel1.grid(row=0, column=0)
    myLabel2.grid(row=10, column=12)    # Keeping a very high number of row or column will not create any or much effect

    root.mainloop()

    return

if __name__ == "__main__":
    main()