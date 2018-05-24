#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
from layout import Gui
from database import Database
from treeview import Treeview
from edit_wind import Edit_wind

class Application(Gui, Database, Treeview, Edit_wind):
    def __init__(self, root):
        Gui.init_gui(self)
        Database.view_records(self)
        Treeview.treeview(self)

if __name__ == '__main__':
    root = Tk()
    root.geometry('1240x660')
    root.title('Gaśnica')
    run = Application(root)
    root.mainloop()
    Database.conn.close()
    exit()
