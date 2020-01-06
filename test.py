from tkinter import *
from tkinter import ttk

# event types - buttonpress, buttonrelease, enter, leave, motion, keypress, keyrelease, focusin, focusout

root = Tk()

def key_press(event):
    print("type: {}".format(event.type))
    print("widget: {}".format(event.widget))
    print("char: {}".format(event.char))
    print("keysym: {}".format(event.keysym))
    print("keycode: {}".format(event.keycode))


# bind has two paramenters - event, function callback

# root.bind("<KeyPress>", key_press)

def shortcut(action):
    print(action)

root.bind("<Control-c>", lambda e: shortcut("Copy"))
root.bind("<Control-v>", lambda e: shortcut("Paste"))

# combination - keyboard events - <KeyPress-Delete> - user pressed Delete key
# <a>, <space>, <less>, <1> -  a printable key
# <Shift_L>, <Control_R>, <F5>, <Up>
# <Return> - for pressing the Enter key!!!
# <Control-Alt-Next>

root.mainloop()