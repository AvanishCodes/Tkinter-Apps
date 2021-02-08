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
    lastName text,
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
    # fName.delete(0, END)
    # lName.delete(0, END)
    # yOE.delete(0, END)
    # Branch.delete(0, END)
    # uiNum.delete(0, END)
    # studentEmail.delete(0, END)
    # create a DB or connect to one
    conn = sqlite3.connect('StudentsList.db')
    # Create a cursor
    c = conn.cursor()
    # Use the inputs
    c.execute("INSERT INTO students VALUES(:fName, :lName, :yOE, :Branch, :uiNum, :studentEmail)",
        {
            'fName': fName.get(),
            'lName': lName.get(),
            'yOE': yOE.get(),
            'Branch': Branch.get(),
            'uiNum': uiNum.get(),
            'studentEmail': studentEmail.get()
        }
    )
    # Commit chanegs
    conn.commit()
    # Close the connection
    conn.close()
    

def newWindow():
    top = Toplevel()     # The window to be opened
    top.title('Records of all the students')
    
    conn = sqlite3.connect('StudentsList.db')
    # Create a cursor
    c = conn.cursor()
    # Use the inputs
    c.execute("SELECT *, oid FROM students")
    records = c.fetchall()
    print(records)

    rowNumber = 0
    columnNumber = 0
    headerSr = Label(top, text="Sr. No.", padx=5).grid(row=rowNumber, column=columnNumber)
    columnNumber += 1
    headerFirstName = Label(top, text="First Name", padx=5).grid(row=rowNumber, column=columnNumber)
    columnNumber += 1
    headerLastName = Label(top, text="Last Name", padx=5).grid(row=rowNumber, column=columnNumber)
    columnNumber += 1
    headerYear = Label(top, text="Year of Admission", padx=5).grid(row=rowNumber, column=columnNumber)
    columnNumber += 1
    headerBranch = Label(top, text="Branch", padx=5).grid(row=rowNumber, column=columnNumber)
    columnNumber += 1
    headerUINumber = Label(top, text="UI Number", padx=5).grid(row=rowNumber, column=columnNumber)
    columnNumber += 1
    headerEmail = Label(top, text="College email", padx=5).grid(row=rowNumber, column=columnNumber)

    rowNumber += 1
    for record in records:
        columnNumber = 0
        serial = Label(top, text=rowNumber).grid(row=rowNumber, column=columnNumber)
        columnNumber += 1
        FirstName = Label(top, text=record[columnNumber-1], padx=5).grid(row=rowNumber, column=columnNumber)
        columnNumber += 1
        LastName = Label(top, text=record[columnNumber-1], padx=5).grid(row=rowNumber, column=columnNumber)
        columnNumber += 1
        Year = Label(top, text=record[columnNumber-1], padx=5).grid(row=rowNumber, column=columnNumber)
        columnNumber += 1
        Branch = Label(top, text=record[columnNumber-1], padx=5).grid(row=rowNumber, column=columnNumber)
        columnNumber += 1
        UINumber = Label(top, text=record[columnNumber-1], padx=5).grid(row=rowNumber, column=columnNumber)
        columnNumber += 1
        Email = Label(top, text=record[columnNumber-1], padx=5).grid(row=rowNumber, column=columnNumber)
        rowNumber += 1
        closeBtn = Button(top, text='Close This Window', command=top.destroy).grid(row=rowNumber)
        
        
    # Other functions are fetchone and fetchmany
    # print(c.fetchall())
    # Commit chanegs
    conn.commit()
    # Close the connection
    conn.close()
    
    return

# Define a query Function
def query():
    newWindow()

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