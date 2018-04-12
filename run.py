#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
from layout import Gui
from database import Database

class Application(Gui, Database):
    def __init__(self, root):
        Gui.init_gui(self)
        Database.initialize_db_connection(self)

if __name__ == '__main__':
    root = Tk()
    root.geometry('1200x800')
    root.title('Gaśnica')
    run = Application(root)
    root.mainloop()
    exit()
