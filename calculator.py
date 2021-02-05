# import tkinter library
from tkinter import *

root = Tk()
root.title("Simple Calculator")

intake = Entry(root, width=35, borderwidth=5)
intake.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def buttonClick(number):
    # intake.delete(0, END)
    currentDigit=intake.get()
    intake.delete(0, END)
    intake.insert(0, str(currentDigit) +str(number))
    return

def buttonClear():
    intake.delete(0, END)
    return

def buttonAdd():
    firstNumber = intake.get()
    global fNum
    fNum = int(firstNumber)
    intake.delete(0, END)
    
    return

def buttonEqual():
    secondNumber = intake.get()
    intake.delete(0, END)
    intake.insert(fNum+int(secondNumber))
    return

# Define Buttons

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: buttonClick(1)).grid(row=3, column=0)
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: buttonClick(2)).grid(row=3, column=1)
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: buttonClick(3)).grid(row=3, column=2)
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: buttonClick(4)).grid(row=2, column=0)
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: buttonClick(5)).grid(row=2, column=1)
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: buttonClick(6)).grid(row=2, column=2)
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: buttonClick(7)).grid(row=1, column=0)
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: buttonClick(8)).grid(row=1, column=1)
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: buttonClick(9)).grid(row=1, column=2)
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: buttonClick(0)).grid(row=4, column=0)

# Operations
button_Add = Button(root, text="+", padx=39, pady=20, command=buttonAdd).grid(row=5, column=0)
button_equal = Button(root, text="=", padx=91, pady=20, command=buttonEqual).grid(row=5, column=1, columnspan=2)
button_clear = Button(root, text="clear", padx=79, pady=20, command=buttonClear).grid(row=4, column=1, columnspan=2)



# Put the buttons on the screen

root.mainloop()