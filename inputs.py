from tkinter import *

root = Tk()

nameInput = Entry(root)
'''
    Parameters in Entry:
        1. width        : width of the input box
        2. fg           : foreground of the input box
        3. bg           : foreground  of the input box
        4. borderwidth  : width of the borders
        5. 
'''
nameInput.pack()
nameOfCandidate = nameInput.get()


# def SayHi(registrationStatus):
    # if(not registrationStatus):
    #     conform = Label(root, text="You have been registered!")
    #     registrationStatus=True
    #     conform.pack()
    # else:
    #     conform = Label(root, text = "You are already registered!")
    #     conform.pack()
    # return

def SayHi():
    reg = f"{nameInput.get()} has been registered!"
    conform = Label(root, text=reg)
    conform.pack()
    return

# def main():
# registrationStatus = False

# validName = False
wave = Button(root, text="Click to register", command=SayHi)
wave.pack()
# if(nameOfCandidate):
    # SayHi(nameOfCandidate, registrationStatus=registrationStatus)
    # wave=Button(root, text="Register", command=SayHi(nameOfCandidate, registrationStatus))
    # wave.event_add(COMMAND, SayHi(nameOfCandidate, registrationStatus=registrationStatus))
    

root.mainloop()
# return

# if __name__ == "__main__":
# main()
