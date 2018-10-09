import subprocess, sys, os, shutil, tkinter
from tkinter import *

kaiser = Tk()

f= Frame(kaiser, height=150, width=360)
f.pack_propagate(0)
f.pack()

L = Label(kaiser, anchor=NE, text="Kaiser GUI v0.1")
L.pack()

def exit():
    global root
    kaiser.quit()



exit = Button(kaiser, text="Exit Kaiser", command=exit)
exit.pack(fill=BOTH, expand=1)

mainloop()

