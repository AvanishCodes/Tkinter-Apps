# Import the Tkinter Library
from tkinter import *
# import tkinter
root = Tk()

# A function to be performed when the button is clicked
def buttonClick():
    myLabel = Label(root, text="A button was clicked", bg="cyan", fg="#342343", width=100)
    myLabel.pack()
    return

def main():
    # root Widget
    
    # creating a label widget
    myButton = Button(root, text="Click me to see if  it works", padx=100, pady=100, command=buttonClick, bg="green", fg="red")
    # A button can be disabled using the following property
    # myButton = Button(root, text="Click me to see if  it works", padx=100, pady=100, state=DISABLED)
    # Show it on screen
    myButton.pack()
    root.mainloop()

    return


if __name__ == "__main__":
    main()
