# Import the required libraries
from tkinter import *
from PIL import ImageTk, Image
import os

# root Tkinter
root = Tk()
root.title('My favorite Image') # Title of the window
# root.iconbitmap('.//images/ /sampleIcon.ico')
# img = PhotoImage(file='./images/sampleIcon.ico')
# root.tk.call('wm', 'iconphoto', root._w, img)

files = ['images/AvanishGUPTA.png']
# global currentFileNo
currentFileNo = 0

imageDirectory = './images'
imageFormats = ('.jpg', '.jpeg', '.png', '.jfif')
for file in os.listdir(imageDirectory):
    if(os.path.splitext(file)[1].lower() in imageFormats):
        print(os.path.splitext(file)[1].lower())
        files.append('images/' + file)

# print(files)
for file in files:
    print(file)

myImage = ImageTk.PhotoImage(Image.open(files[0]))
# myLabel = Label()
myLabel = Label(image=myImage)
myLabel.grid(row=0, column=0, columnspan=3)
# myLabel.pack()

# Fine till here

def forward():
#     # myImage = ImageTk.PhotoImage(Image.open(newImage))
    global myLabel
    global buttonForward
    global buttonQuit
    global buttonBack
    global currentFileNo
    global newImage
    # global files
    myLabel.grid_forget() 
    # newImage = files[(currentFileNo+1)%len(files)]
    currentFileNo += 1
    if(currentFileNo > len(files)-1):
        currentFileNo = 0
    print(currentFileNo)
    # print(newImage)
    # zoom = 1.8
    # newImage = Image.open(newImage)
    # pixels_x, pixels_y = tuple([int(zoom * x)  for x in newImage.size])
    # newImage = ImageTk.PhotoImage(Image.open(newImage).resize((pixels_x, pixels_y)))
    # newImage = ImageTk.PhotoImage(Image.open(newImage).resize(512, 512))
    # newImageName = str(newImage)
    # newImage = ImageTk.PhotoImage(Image.open(f"{newImageName}"))
    newImage = ImageTk.PhotoImage(Image.open(files[currentFileNo]))
    myLabel = Label(image=newImage)
    myLabel.grid(row=0, column=0, columnspan=3)
    buttonBack = Button(root, text="<<", command=back)
    buttonQuit = Button(root, text="End the image display", command=root.quit)
    buttonForward = Button(root, text=">>", command= forward)
    buttonBack.grid(row=1, column=0)
    buttonQuit.grid(row=1, column=1)
    buttonForward.grid(row=1, column=2)

#     # # Label(image=myImage)
#     # myLabel.pack()
    return

def back():
#     # 'images/firstYearCP.png'
    # myImage = ImageTk.PhotoImage(Image.open(newImage))
    global myLabel
    global buttonForward
    global buttonQuit
    global buttonBack
    # global files
    global newImage
    global currentFileNo
    print(currentFileNo)
    myLabel.grid_forget() 
    newImage = files[(currentFileNo-1)%len(files)]
    currentFileNo -= 1
    if(currentFileNo < 0):
        currentFileNo = len(files) - 1
    print(newImage)
    # zoom = 1.8
    # pixels_x, pixels_y = tuple([int(zoom * x)  for x in image.size])
    # newImage = ImageTk.PhotoImage(Image.open(newImage).resize((pixels_x, pixels_y)))
    newImage = ImageTk.PhotoImage(Image.open(newImage))
    myLabel = Label(image=newImage)
    
    buttonBack = Button(root, text="<<", command=back)
    buttonQuit = Button(root, text="End the image display", command=root.quit)
    buttonForward = Button(root, text=">>", command= forward)
    buttonBack.grid(row=1, column=0)
    buttonQuit.grid(row=1, column=1)
    buttonForward.grid(row=1, column=2)
    myLabel.grid(row=0, column=0, columnspan=3)

#     # #  Label(image=myImage)
#     # myLabel.pack()
    return

buttonBack = Button(root, text="<<", command=back)
buttonQuit = Button(root, text="End the image display", command=root.quit)
buttonForward = Button(root, text=">>", command= forward)

buttonBack.grid(row=1, column=0)
buttonQuit.grid(row=1, column=1)
buttonForward.grid(row=1, column=2)

# # buttonForward.pack()
# # buttonQuit.pack()
# # buttonBack.pack()
# # myLabel.pack()

root.mainloop()