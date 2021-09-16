from tkinter import *
import pygame
import os

root = Tk()  # In order to create an empty window
# Passing Root to MusicPlayer Class


class MusicPlayer():
    def __init__(self, root):
        self.root = root
        # Title of the window
        self.root.title("MusicPlayer")
        # Window Geometry
        self.root.geometry("1000x200+200+200")
        # Initiating Pygame
        pygame.init()
        # Initiating Pygame Mixer
        pygame.mixer.init()
        # Declaring track Variable
        self.track = StringVar()
        # Declaring Status Variable
        self.status = StringVar()

        # Creating the Track Frames for Song label & status label
        trackframe = LabelFrame(self.root, text="Song Track", font=(
            "times new roman", 15, "bold"), bg="Navyblue", fg="white", bd=5, relief=GROOVE)
        trackframe.place(x=0, y=0, width=600, height=100)
        # Inserting Song Track Label
        songtrack = Label(trackframe, textvariable=self.track, width=20, font=(
            "times new roman", 24, "bold"), bg="Orange", fg="gold").grid(row=0, column=0, padx=10, pady=5)
        # Inserting Status Label
        trackstatus = Label(trackframe, textvariable=self.status, font=(
            "times new roman", 24, "bold"), bg="orange", fg="gold").grid(row=0, column=1, padx=10, pady=5)

        # Creating Button Frame
        buttonframe = LabelFrame(self.root, text="Control Panel", font=(
            "times new roman", 15, "bold"), bg="grey", fg="white", bd=5, relief=GROOVE)
        buttonframe.place(x=0, y=100, width=600, height=100)
        # Inserting Play Button
        playbtn = Button(buttonframe, text="PLAYSONG", command=self.playsong, width=10, height=1, font=(
            "times new roman", 16, "bold"), fg="navyblue", bg="pink").grid(row=0, column=0, padx=10, pady=5)
        # Inserting Pause Button
        playbtn = Button(buttonframe, text="PAUSE", command=self.pausesong, width=8, height=1, font=(
            "times new roman", 16, "bold"), fg="navyblue", bg="pink").grid(row=0, column=1, padx=10, pady=5)
        # Inserting Unpause Button
        playbtn = Button(buttonframe, text="UNPAUSE", command=self.unpausesong, width=10, height=1, font=(
            "times new roman", 16, "bold"), fg="navyblue", bg="pink").grid(row=0, column=2, padx=10, pady=5)
        # Inserting Stop Button
        playbtn = Button(buttonframe, text="STOPSONG", command=self.stopsong, width=10, height=1, font=(
            "times new roman", 16, "bold"), fg="navyblue", bg="pink").grid(row=0, column=3, padx=10, pady=5)

        # Creating Playlist Frame
        songsframe = LabelFrame(self.root, text="Song Playlist", font=(
            "times new roman", 15, "bold"), bg="grey", fg="white", bd=5, relief=GROOVE)
        songsframe.place(x=600, y=0, width=400, height=200)
        # Inserting scrollbar
        scrol_y = Scrollbar(songsframe, orient=VERTICAL)
        # Inserting Playlist listbox
        self.playlist = Listbox(songsframe, yscrollcommand=scrol_y.set, selectbackground="gold", selectmode=SINGLE, font=(
            "times new roman", 12, "bold"), bg="silver", fg="navyblue", bd=5, relief=GROOVE)
        # Applying Scrollbar to listbox
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.playlist.yview)
        self.playlist.pack(fill=BOTH)
        # Changing Directory for fetching Songs
        os.chdir("C:\\Users\\Avanish Gupta\\Music\\Audio Songs")
        # Fetching Songs
        songtracks = os.listdir()
        # Inserting Songs into Playlist
        for track in songtracks:
            self.playlist.insert(END, track)


    def playsong(self):
        # Displaying Selected Song title
        self.track.set(self.playlist.get(ACTIVE))
        # Displaying Status
        self.status.set("-Playing")
        # Loading Selected Song
        pygame.mixer.music.load(self.playlist.get(ACTIVE))
        # Playing Selected Song
        pygame.mixer.music.play()


    def stopsong(self):
        # Displaying Status
        self.status.set("-Stopped")
        # Stopped Song
        pygame.mixer.music.stop()


    def pausesong(self):
        # Displaying Status
        self.status.set("-Paused")
        # Paused Song
        pygame.mixer.music.pause()


    def unpausesong(self):
        # It will Display the  Status
        self.status.set("-Playing")
        # Playing back Song
        pygame.mixer.music.unpause()

MusicPlayer(root)

root.mainloop()
