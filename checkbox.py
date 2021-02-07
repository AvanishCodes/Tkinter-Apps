# Import the libraries
from tkinter import *

# Tkinter root 
root = Tk()
root.title('Adding checkbox code') # Name of the window
root.geometry("1000x1000")

def show():
    myLabel = Label(root, text=var.get()).pack()

# var = IntVar()

var = StringVar()

c = Checkbutton(root, text='Check this box if you wanna sit for placements', variable = var, onvalue="You'll be sitting for the placements", offvalue="You'll not be sitting for the placements, are you sure?").pack()






myButton = Button(root, text="Get Selection", command=show).pack()

mainloop()


# Use this section later on to generate a message for multiple checkboxes

'''
# def getText():
#     # result = str()
#     global CP, DEV
#     DEV = BooleanVar()
#     CP = BooleanVar()
#     # CP = BooleanVar()
#     # global cp
#     # global dev
#     dev = Checkbutton(root, text="Check this box for dev", variable = DEV).pack()
#     cp = Checkbutton(root, text="Check this button for CP", var=CP).pack()
#     cp = cp.get()
#     dev = dev.get()
#     if(cp and not dev):
#         return "CP only"
#     if(dev and not cp):
#         return "dev only"
#     if(dev and cp):
#         return "Both dev and CP"
#     return "Not available for interview"
'''
