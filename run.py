#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
from layout import Gui
from database import Database

class Application(Gui, Database):
    def __init__(self, root):
        Gui.init_gui(self)
        Database.view_records(self)

if __name__ == '__main__':
    root = Tk()
    root.geometry('1420x800')
    root.title('Gaśnica')
    run = Application(root)
    root.mainloop()
    Database.conn.close()
    exit()
