from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()
root.title('My favorite Image')
# root.iconbitmap('.//images/ /sampleIcon.ico')
# img = PhotoImage(file='./images/sampleIcon.ico')
# root.tk.call('wm', 'iconphoto', root._w, img)

files = ['images/AvanishGUPTA.png']
currentFileNo = 0

imageDirectory = './images'
imageFormats = ('.jpg', '.jpeg', '.png', '.jfif')
for file in os.listdir(imageDirectory):
    if(os.path.splitext(file)[1].lower() in imageFormats):
        files.append('images/' + file)

# print(files)
for file in files:
    print(file)

# myImage = ImageTk.PhotoImage(Image.open('images/AvanishGUPTA.png'))
myLabel = Label(image=files[0])
myLabel.grid(row=0, column=0, columnspan=3)
# myLabel.pack()

def forward():
    # newImage = files[(currentFileNo+1)%len(files)]
    # print(newImage)
    # myImage = ImageTk.PhotoImage(Image.open(newImage))
    # global myLabel
    # global buttonForward
    # global buttonBack
    # myLabel.grid_forget() 
    # myLabel = Label(image=newImage)
    # # Label(image=myImage)
    # myLabel.pack()
    return

def back():
    # 'images/firstYearCP.png'
    # newImage = files[(currentFileNo-1)%len(files)]
    # print(newImage)
    # myImage = ImageTk.PhotoImage(Image.open(newImage))
    # global myLabel
    # global buttonForward
    # global buttonBack
    # myLabel.grid_forget() 
    # myLabel = Label(image=newImage)
    # #  Label(image=myImage)
    # myLabel.pack()
    return

# myImage = ImageTk.PhotoImage(Image.open('//home//avanish//Pictuers//HackBash.jpeg'))

buttonBack = Button(root, text="<<", command=back)
buttonQuit = Button(root, text="End the image display", command=root.quit)
buttonForward = Button(root, text=">>", command=forward)

buttonBack.grid(row=1, column=0)
buttonQuit.grid(row=1, column=1)
buttonForward.grid(row=1, column=2)

# buttonForward.pack()
# buttonQuit.pack()
# buttonBack.pack()
# myLabel.pack()

root.mainloop()