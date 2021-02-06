# Import the libraries
from tkinter import *
from tkinter import messagebox

# Tkinter loop
root = Tk()
root.title('Message Box Program in Tkinter')

# Function for simple popup
def popup():
    response = messagebox.showinfo("This is my PopUp", "Hello, peeps!")
    Label(root, text=response).pack()

# Function for question popup
def popupWithQn():
    # messagebox.askquestion("Robo verifier", "Are you human?", options={"Yes": "Yes, I am", "No": "No, I am not", "Maybe": "I may be the one"})
    response = messagebox.askquestion("Robo verifier", "Are you human?")
    Label(root, text=response).pack()

# Function for asking to cancel or abort a process
def askToCancel():
    response = messagebox.askokcancel("Attention", "Would you like to cancel?")
    Label(root, text=response).pack()


def askYesNo():
    response = messagebox.askyesno("Before you procees", "Are you sure that the details are correct?")
    Label(root, text=response).pack()

'''
    Other available messagebox types:
        1. showerror
        2. showwarning
        3. showinfo
'''

# Simple popup with info
Button(root, text='Info opup', command=popup).pack()

# Popup with question
Button(root, text='Question Popup', command=popupWithQn).pack()

# Popup with OK/Cancel Answers
Button(root, text='OK?Cancel Popup', command=askToCancel).pack()

# Popup with Yes/No Answers
Button(root, text='Yes/No Popup', command=askYesNo).pack()

root.mainloop()