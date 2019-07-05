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
    statusBar["text"] = filename


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
# root.geometry("500x300")
# title of the window
root.title("sarcino music_player")
# icon, r = raw string
root.iconbitmap(r"icon.ico")

# Label widget. Every widget needs to be packed
text = Label(root, text = "Let the music play!")
text.pack(pady=10)

# play button = play image
def play_music():
    # is paused initialized?
    try:
        paused
        # if paused is not initialized, try...
    except NameError:
        try:
            mixer.music.load(filename)
            mixer.music.play()
            statusBar["text"] = "Playing " + os.path.basename(filename)
        except:
            tkinter.messagebox.showerror("Not Found", "music_player couldn't find a file. Please check again.")
    # if paused was initialized, unpause music
    else:
        mixer.music.unpause()

# stop button = stop image
def stop_music():
    mixer.music.stop()
    statusBar["text"] = "Playback Stopped"

def pause_music():
    global paused
    paused = TRUE
    mixer.music.pause()
    statusBar["text"] = "Playback Paused"

def rewind_music():
    play_music()


def set_vol(val):
    # value is string, must be converted into integer
    volume = int(val) / 100
    # set_volume function takes value from 0 to 1 only
    mixer.music.set_volume(volume)

# by default is not False
muted = False

def mute_music():
    global muted
    # if muted is true
    if muted:
        # set default values = unmute music
        mixer.music.set_volume(0.25)
        volumeBtn.configure(image=volume)
        scale.set(25)
        muted = False
    else:
        #mute the music
        mixer.music.set_volume(0)
        # once I clicked on the volume picture, it changes to the mute picture
        volumeBtn.configure(image=mute)
        # scale bar will show 0
        scale.set(0)
        muted = True



# creating frame for buttons - to be able to align them in one row
middleframe = Frame(root)
middleframe.pack(pady=10, padx=30)

bottomframe = Frame(root)
bottomframe.pack(pady=10, padx=30)


# play image - show in the default window
play = PhotoImage(file="play.png")
# play button is localized in middleframe, image variable play, function play music
playBtn = Button(middleframe, image=play, command=play_music)
playBtn.grid(row=0, column=0, padx=3)

# stop image - show in the default window
stop = PhotoImage(file="stop.png")
stopBtn = Button(middleframe, image=stop, command=stop_music)
stopBtn.grid(row=0, column=1, padx=3)

# pause image
pause = PhotoImage(file="pause.png")
pauseBtn = Button(middleframe, image=pause, command=pause_music)
pauseBtn.grid(row=0, column=2, padx=3)

# rewind button
rewind = PhotoImage(file="rewind.png")
rewindBtn = Button(middleframe, image=rewind, command=rewind_music)
rewindBtn.grid(row=0, column=3, padx=3)

# mute/ unmute button
mute = PhotoImage(file="mute.png")
volume = PhotoImage(file="volume.png")
volumeBtn = Button(bottomframe, image=volume, command=mute_music)
volumeBtn.grid(row=0, column=2, padx=3)

# volume control
scale = Scale(bottomframe, from_=0, to=100, orient=HORIZONTAL, cursor="hand2", command_=set_vol)
# default volume value when you open the player
# show 25
scale.set(25)
# play 25 volume value
mixer.music.set_volume(0.25)
scale.grid(row=0, column=0, pady=20, padx=20)

# anchor = align of text, W is for west, left
statusBar = Label(root, text="Welcome to music_player", relief=SUNKEN, anchor=W)
statusBar.pack(side=BOTTOM, fill=X)


# start the program
root.mainloop()