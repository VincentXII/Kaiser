import subprocess, sys, os, shutil, tkinter
from tkinter import Tk, Label, Button


class Kaiser:
    def __init__(self, master):
        self.master = master
        master.title("Kaiser GUI v0.1")

        self.label = Label(master, text="Please Select an Option")
        self.label.pack()

        self.directory_button = Button(master, text="See Current Directory", command=self.directory)
        self.directory_button.pack()

        self.exit_button = Button(master, text="Exit", command=master.quit)
        self.exit_button.pack()

    def directory(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        print(os.getcwd())


root = Tk()
my_gui = Kaiser(root)
root.mainloop()