import os
from tkinter import *
from pygame import mixer
import tkinter.messagebox
from tkinter import filedialog

# creating new window
root = Tk()

# creating menu bar itself
menuBar = Menu(root)

# configuring of menu bar, get ready for sub-menu items
root.config(menu=menuBar)

# creating sub-menu File, using menuBar
subMenu = Menu(menuBar, tearoff=0)

def browse_file():
    # make fileName variable global
    global filename
    filename = filedialog.askopenfilename()
    print(filename)


menuBar.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Open", command=browse_file)
subMenu.add_command(label="Exit", command=root.destroy)

# About menu - opens new window with information: Title and Copy
def about():
    tkinter.messagebox.showinfo("sarcino music_player", "Created by @sarcino", )

# creating sub-menu Help, using menuBar
subMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Help", menu=subMenu)
subMenu.add_command(label="About", command=about)


# initialize mixer which allows us to play music files
mixer.init()


# size of the window after opening
root.geometry("800x400")
# title of the window
root.title("sarcino music_player")
# icon, r = raw string
root.iconbitmap(r"icon.ico")

# Label widget - every widget needs to be packed
text = Label(root, text = "Let the music play!")
text.pack()

# play button = play image
def play_music():
    try:
        mixer.music.load(filename)
        mixer.music.play()
        statusBar["text"] = "Playing " + os.path.basename(filename)
    except:
        tkinter.messagebox.showerror("Not Found", "music_player couldn't find a file. Please check again.")

# stop button = stop image
def stop_music():
    mixer.music.stop()
    statusBar["text"] = "Playback Stopped"

def set_vol(val):
    # value is string, must be converted into integer
    volume = int(val) / 100
    # set_volume function takes value from 0 to 1 only
    mixer.music.set_volume(volume)

# play image - show in the default window
play = PhotoImage(file="play.png")
playBtn = Button(root, image=play, command=play_music)
playBtn.pack()

# stop image - show in the default window
stop = PhotoImage(file="stop.png")
stopBtn = Button(root, image=stop, command=stop_music)
stopBtn.pack()

# volume control
scale = Scale(root, from_=0, to=100, orient=HORIZONTAL, cursor="hand2", command_=set_vol)
# default volume value when you open the player
# show 25
scale.set(25)
# play 25 volume value
mixer.music.set_volume(0.25)
scale.pack()

# anchor = align of text, W is for west, left
statusBar = Label(root, text="Welcome to music_player", relief=SUNKEN, anchor=W)
statusBar.pack(side=BOTTOM, fill=X)


# start the program
root.mainloop()