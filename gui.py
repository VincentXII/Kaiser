import subprocess, sys, os, shutil, tkinter
from tkinter import *

class Kaiser(Frame):
    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.pack()

root = Tk()

kaiser = Kaiser(master=root)
kaiser.master.title("Kaiser GUI v0.1")

f= Frame(root, height=150, width=360)
f.pack_propagate(0)
f.pack()

L = Label(root, anchor=NE, text="Kaiser GUI v0.1")
L.pack()

def exit():
    global root
    root.quit()

def currentdir():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(os.getcwd())

currentdir = Button(root, text="Get Current Directory", command=currentdir)
currentdir.pack() 

exit = Button(root, text="Exit Kaiser", command=exit)
exit.pack(fill=BOTH, expand=1)

mainloop()

