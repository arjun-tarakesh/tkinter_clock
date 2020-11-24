from tkinter import *
from tkinter.ttk import *

from time import strftime 
# coverts the time format tuple into a string

root = Tk()

# To initialize tkinter, we have to create a Tk root widget, which is a window with a title bar and 
# other decoration provided by the window manager. 
# The root widget has to be created before any other widgets and there can only be one root widget.

myBg = '#192A56'
myfg = "#E83350"

def Time():
    t = strftime('%H:%M:%S %p')
    label.config(text=t)
    label.after(1000, Time)
    

label = Label(root, font=("ds digital",80), background = myBg, foreground = myfg)
label.pack(anchor='center')
# Anchors are used to define where text is positioned relative to a reference point.
Time()

mainloop()
# tk.mainloop() blocks. What that means is that execution of your python program halts there. 