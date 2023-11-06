import os
import pygame
from tkinter import *
from tkinter.filedialog import askdirectory
from mutagen.id3 import ID3

# Create and configure the Tkinter window
root = Tk()
root.title("Music Player")
root.geometry("400x400")
root.configure(bg="#e0e0e0")

# Initialize variables
listofsongs = []
realnames = []

v = StringVar()
songlabel = Label(root, textvariable=v, width=35, font=("Helvetica", 12), bg="#e0e0e0")

index = 0

# Function to choose a directory and load songs
def directorychooser():
    directory = askdirectory()

    if directory:
        os.chdir(directory)

        for files in os.listdir(directory):
            if files.endswith(".mp3"):
                realdir = os.path.realpath(files)
                audio = ID3(realdir)
                realnames.append(audio['TIT2'].text[0])
                listofsongs.append(os.path.join(directory, files))

        pygame.mixer.init()
        pygame.mixer.music.load(listofsongs[0])
        pygame.mixer.music.play()

directorychooser()

# Function to update the song label
def updatelabel():
    global index
    v.set(realnames[index])

# Function to play the next song
def nextsong(event):
    global index
    index += 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()

# Function to play the previous song
def prevsong(event):
    global index
    index -= 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()

# Function to unpause the song
def unpausesong(event):
    pygame.mixer.music.unpause()
    v.set("Song unpaused")

# Function to pause the song
def pausesong(event):
    pygame.mixer.music.pause()
    v.set("Song Paused")

# Function to stop the music
def stopsong(event):
    pygame.mixer.music.stop()
    v.set("")

# Create and configure labels, listbox, and buttons with styling
label = Label(root, text='Music Player', font=("Helvetica", 16, "bold"), bg="#e0e0e0")
label.pack(pady=10)

listbox = Listbox(root, font=("Helvetica", 12), selectbackground="#a6a6a6", selectforeground="#ffffff", bg="#d9d9d9")
listbox.pack(pady=10, fill=BOTH, expand=True)

for items in realnames:
    listbox.insert(END, items)

buttons_frame = Frame(root, bg="#e0e0e0")
buttons_frame.pack(pady=10)

nextbutton = Button(buttons_frame, text='Next Song', font=("Helvetica", 12), bg="#4caf50", fg="#ffffff")
nextbutton.grid(row=0, column=0, padx=10)

previousbutton = Button(buttons_frame, text='Previous Song', font=("Helvetica", 12), bg="#4caf50", fg="#ffffff")
previousbutton.grid(row=0, column=1, padx=10)

pausebutton = Button(buttons_frame, text='Pause Song', font=("Helvetica", 12), bg="#ff9800", fg="#ffffff")
pausebutton.grid(row=0, column=2, padx=10)

unpausebutton = Button(buttons_frame, text='Unpause Song', font=("Helvetica", 12), bg="#ff9800", fg="#ffffff")
unpausebutton.grid(row=0, column=3, padx=10)

stopbutton = Button(buttons_frame, text='Stop Music', font=("Helvetica", 12), bg="#f44336", fg="#ffffff")
stopbutton.grid(row=0, column=4, padx=10)

# Bind buttons to their respective functions
nextbutton.bind("<Button-1>", nextsong)
previousbutton.bind("<Button-1>", prevsong)
pausebutton.bind("<Button-1>", pausesong)
unpausebutton.bind("<Button-1>", unpausesong)
stopbutton.bind("<Button-1>", stopsong)

songlabel.pack()

# Start the Tkinter main loop
root.mainloop()