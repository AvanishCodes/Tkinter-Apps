# Import the libraries
from tkinter import *
import sqlite3

# Tkinter root 
root = Tk()
root.title('Inclusing a database in a Tkinter Program') # Name of the window

# create a DB or connect to one
conn = sqlite3.connect('StudentsList.db')

# Create a cursor
c = conn.cursor()


# Create a table and comment out after running once

'''
c.execute("""CREATE TABLE students(
    firstName text,
    lastName test,
    yearOfEntry integer,
    branch text,
    uiNo text,
    email text
)
""")
'''

# Create Submit Function
def submit():
    # clear the text boxes
    fName.delete(0, END)
    lName.delete(0, END)
    yOE.delete(0, END)
    Branch.delete(0, END)
    uiNum.delete(0, END)
    studentEmail.delete(0, END)
    # create a DB or connect to one
    conn = sqlite3.connect('StudentsList.db')
    # Create a cursor
    c = conn.cursor()
    # Use the inputs
    c.execute("INSERT INTO students VALUES(:firstName, :lastName, :yearOfEntry, :branch, :uiNo, :email)",
        {
            'firstName': fName.get(),
            'firstName': lName.get(),
            'yearOfEntry': yOE.get(),
            'branch': Branch.get(),
            'ioNo': uiNum.get(),
            'email': studentEmail.get()
        }
    )
    # Commit chanegs
    conn.commit()
    # Close the connection
    conn.close()
    

# Define a query Function
def query():
    
    return

# Create text boxes

fName = Entry(root, width=30)
fName.grid(row=0, column=1, padx=20)

lName = Entry(root, width=30)
lName.grid(row=1, column=1)

yOE = Entry(root, width=30)
yOE.grid(row=2, column=1)

Branch = Entry(root, width=30)
Branch.grid(row=3, column=1)

uiNum = Entry(root, width=30)
uiNum.grid(row=4, column=1)

studentEmail = Entry(root, width=30)
studentEmail.grid(row=5, column=1)

# Create Labels to display data

fNameLabel = Label(root, text="First Name: ")
fNameLabel.grid(row=0, column=0)

lNameLabel = Label(root, text="Last Name: ")
lNameLabel.grid(row=1, column=0)

yOELabel = Label(root, text="Year of Entry: ")
yOELabel.grid(row=2, column=0)

BranchLabel = Label(root, text="Branch: ")
BranchLabel.grid(row=3, column=0)

uiNumLabel = Label(root, text="UI Number: ")
uiNumLabel.grid(row=4, column=0)

studentEmailLabel = Label(root, text="Student Email: ")
studentEmailLabel.grid(row=5, column=0)

# Create Submit button
submtButton = Button(root, text="Add record to database", command=submit)
submtButton.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create a Query Button

queryBtn = Button(root, text="Show Records", command=query)
queryBtn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# Commit chanegs
conn.commit()

# Close the connection
conn.close()

mainloop()