import os
import threading
import time
import tkinter.messagebox
from tkinter import *
from tkinter import filedialog

from tkinter import ttk
from pygame import mixer

import mutagen
from mutagen.mp3 import MP3
from mutagen.flac import FLAC



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
    tkinter.messagebox.showinfo(
        "sarcino music_player", "Created by @sarcino", )


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
root.iconbitmap(r"images/icon.ico")

# showing total length of song which is playing right now
lenghtlabel = Label(root, text="")
lenghtlabel.pack(pady=5)

currenttimelabel = Label(root, text="")
currenttimelabel.pack(pady=5)


def show_details():
    # spliting name of the file from extension
    file_data = os.path.splitext(filename)

    if file_data[1] == ".mp3":
        audio = MP3(filename)
        total_length = audio.info.length

        global bitrate

        bitrate = audio.info.bitrate   
        bitrate = round(bitrate / 1000)

    elif file_data[1] == ".flac":
        audio = FLAC(filename)
        total_length = audio.info.length

        bitrate = audio.info.bitrate
        bitrate = round(bitrate / 1000)
        print(bitrate)

    else:
        # loading the sound and store it into variable
        a = mixer.Sound(filename)
        # get the length of stored sound in seconds
        total_length = a.get_length()

    # take totallength and calculating remainder
    mins, secs = divmod(total_length, 60)
    # rounding
    mins = round(mins)
    secs = round(secs)

    global timeformat
    # showing minutes and seconds in 2 digits format
    timeformat = "{:02d}:{:02d}".format(mins, secs)
    lenghtlabel["text"] = "Total lenght: " + timeformat

    # THREADING - first argument function, arguments - argument of the function
    t1 = threading.Thread(target=start_count, args=(total_length,))
    # + calling it
    t1.start()

# counting current time of playing song
# t is our total_length

def start_count(t):
    global paused
    current_time = 0
    # mixer.music.get_busy() - returns false when we press stop button or music stops playing
    while current_time <= t and mixer.music.get_busy():
        if paused:
            continue
        else:
            current_mins, current_secs = divmod(current_time, 60)
            current_mins = round(current_mins)
            current_secs = round(current_secs)

            global timeformat_current

            timeformat_current = "{:02d}:{:02d}".format(current_mins, current_secs)
            currenttimelabel['text'] = "Current Time: " + timeformat_current
            # sleep for one second and continue += 1 second
            time.sleep(1)
            current_time = current_time + 1


# play button = play image
def play_music():

    global paused
    # if paused button is true, unpause this
    if paused:
        # playback resumed
        mixer.music.unpause()
        statusBar["text"] = os.path.basename(filename) + " | " + "duration: " + timeformat
        # paused button is false again
        paused = False
    else:
        try:            
            mixer.music.load(filename)                    
            mixer.music.play()  
            show_details()            
            statusBar["text"] = os.path.basename(
                filename) + " | " + "duration: " + timeformat

        except:
            tkinter.messagebox.showerror(
                "Not Found", "music_player couldn't find a file. Please check again.")


# stop button = stop image
def stop_music():
    mixer.music.stop()
    statusBar["text"] = "Playback Stopped"


paused = False


def pause_music():
    global paused
    paused = True
    mixer.music.pause()
    statusBar["text"] = "playback paused"


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
        # mute the music
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
play = PhotoImage(file="images/play.png")
# play button is localized in middleframe, image variable play, function play music
playBtn = Button(middleframe, image=play, command=play_music)
playBtn.grid(row=0, column=0, padx=3)

# stop image - show in the default window
stop = PhotoImage(file="images/stop.png")
stopBtn = Button(middleframe, image=stop, command=stop_music)
stopBtn.grid(row=0, column=1, padx=3)

# pause image
pause = PhotoImage(file="images/pause.png")
pauseBtn = Button(middleframe, image=pause, command=pause_music)
pauseBtn.grid(row=0, column=2, padx=3)

# rewind button
rewind = PhotoImage(file="images/rewind.png")
rewindBtn = Button(middleframe, image=rewind, command=rewind_music)
rewindBtn.grid(row=0, column=3, padx=3)

# mute/ unmute button
mute = PhotoImage(file="images/mute.png")
volume = PhotoImage(file="images/volume.png")
volumeBtn = Button(bottomframe, image=volume, command=mute_music)
volumeBtn.grid(row=0, column=2, padx=3)

# volume control
scale = Scale(bottomframe, from_=0, to=100, orient=HORIZONTAL,
              cursor="hand2", command_=set_vol)
# default volume value when you open the player
# show 25
scale.set(25)
# play 25 volume value
mixer.music.set_volume(0.25)
scale.grid(row=0, column=0, pady=20, padx=20)



# anchor = align of text, W is for west, left
statusBar = Label(root, text="Welcome to music_player",
                  relief=SUNKEN, anchor=W)
statusBar.pack(side=BOTTOM, fill=X)


# start the program
root.mainloop()