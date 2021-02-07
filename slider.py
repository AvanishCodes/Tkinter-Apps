# Import the libraries
from tkinter import *

# Tkinter root 
root = Tk()
root.title('Using slider  widgets') # Name of the window
root.geometry("400x400")

def slide():
    # myLabel = Label(root, text=horizontalSlider.get()).pack() 
    # root.geometry(str(horizontalSlider.get()) + "x400")
    # myLabel = Label(root, text=verticalSlider.get()).pack() 
    size = str(horizontalSlider.get()) + "x" + str(verticalSlider.get())
    myLabel = Label(root, text=size).pack()
    root.geometry(str(horizontalSlider.get()) + "x" + str(verticalSlider.get()))
    

verticalSlider = Scale(root, from_=100, to=400, orient=VERTICAL)
verticalSlider.pack()

horizontalSlider = Scale(root, from_=100, to=400, orient=HORIZONTAL)
horizontalSlider.pack()

def getSize():
    return f"{horizontalSlider.get()} x {verticalSlider.get()}"

myLabel = Label(root, text=getSize).pack()

myButton = Button(root, text="Click Me!", command=slide).pack()


mainloop()