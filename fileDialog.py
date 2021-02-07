# Import the libraries
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

# Tkinter root 
root = Tk()
root.title('File Dialog box') # Name of the window

# root.fileName = filedialog.askopenfilename(initialdir="./images", title='Select a file to open', filetypes=(("png files", "*.png"), ("all files", "*.*")))
 
# selectedImage  = ImageTk.PhotoImage(Image.open(root.fileName))
# selectedImageLabel = Label(image = selectedImage).pack()
# myLabel = Label(root, text=root.fileName).pack()

# Function to open a file
def openNewFile():
    global selectedImage
    root.fileName = filedialog.askopenfilename(initialdir="./images", title='Select a file to open', filetypes=(("png files", "*.png"), ("all files", "*.*")))
 
    selectedImage  = ImageTk.PhotoImage(Image.open(root.fileName))
    selectedImageLabel = Label(image = selectedImage).pack()
    myLabel = Label(root, text=root.fileName).pack()

# Button to ask user if they want to open a file
myButton = Button(root, text="Open another file", command=openNewFile).pack()


mainloop()