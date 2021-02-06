from tkinter import *

# root tkinter widget
root = Tk()
root.title('Adding radio buttons')

# r = IntVar()
# r.set('2')

# Branches to be selected by the user
Branches = [
    ("CSE", "Computer Science and Engineering"),
    ("ECE", "Electronics and Communication Engineering"),
    ("CE", "Civil Engineering"),
    ("ME", "Mechanical Engineering"),
    ("CHE", "Chemical Engineering"),
    ("EE", "Electrical Engineering"),
]

# Declare a string type variable
branch = StringVar()
# Set a default value
branch.set('Computer Science and Engineering')

# Declare the radio buttons
for short, full in Branches:
    Radiobutton(root, text=short, value=full, variable = branch).pack()

# Define the function of the click button
def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()


# myLabel = Label(root, text=r.get())
myLabel = Label(root, text=branch .get())
myLabel.pack()

myButton = Button(root, text = 'Click Me!', command= lambda: clicked(branch.get())).pack()

root.mainloop()

