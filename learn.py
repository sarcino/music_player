from tkinter import *

root = Tk()

# play image - show in the default window
play = PhotoImage(file="play.png")
# play button is localized in middleframe, image variable play, function play music
playBtn = Button(root, image=play)
playBtn.grid(row=0, column=0)

# stop image - show in the default window
stop = PhotoImage(file="stop.png")
stopBtn = Button(root, image=stop)
stopBtn.grid(row=0, column=2)

# pause image
pause = PhotoImage(file="pause.png")
pauseBtn = Button(root, image=pause)
pauseBtn.grid(row=0, column=1)

root.mainloop()

