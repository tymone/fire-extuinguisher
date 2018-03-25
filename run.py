#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
import tkinter as tk
import sqlite3
import time
#import datatime
import random
from tkinter import messagebox
import subprocess as s


class Application(Text):

    def __init__(self, master):
        Text.__init__(self, master)

        #---------- buttons ----------

        self.add_button = Button(master, text='dodaj sprzęt', command=self.add_equip, )
        self.quit = Button(master, text='Wyjście', command=master.destroy)

        self.add_button.grid(column=0, row=0, columnspan=2, rowspan=1)
        self.quit.grid(column=0, row=5, columnspan=2, rowspan=1)

        # ---------- label ----------

        self.show_area = ttk.Label(master, text='Rejon:')
        self.sort = ttk.Label(master, text='Sortuj wg:')

        self.show_area.grid(column=0, row=1, columnspan=2)
        self.sort.grid(column=0, row=3, columnspan=2)

        #---------- check buttons ----------

        self.area1_var = IntVar()
        self.area1 = tk.Checkbutton(master, text='Rejon 1', variable=self.area1_var)

        self.area2_var = IntVar()
        self.area2 = tk.Checkbutton(master, text='Rejon 2', variable=self.area2_var)

        self.area1.grid(column=0, row=2, columnspan=1, rowspan=1)
        self.area2.grid(column=1, row=2, columnspan=1, rowspan=1)

        #---------- radio buttons ----------

        self.num = tk.Radiobutton(master, text='numeru')
        self.localization = tk.Radiobutton(master, text='lokalizacji',)

        self.num.grid(column=0, row=4, columnspan=1, rowspan=1)
        self.localization.grid(column=1, row=4, columnspan=1, rowspan=1)

        #---------- treeview ----------

        self.tree = ttk.Treeview(master, height=30)

        self.tree['columns'] = ('one', 'two', 'three', 'four', 'five', 'six')
        self.tree.column('one', width=100)
        self.tree.column('two', width=100)
        self.tree.column('three', width=100)
        self.tree.column('four', width=100)
        self.tree.column('five', width=100)
        self.tree.column('six', width=100)

        self.tree['show'] = 'headings' #delete first column
        self.tree.heading('one', text='Index')
        self.tree.heading('two', text='Nr. gaśnicy')
        self.tree.heading('three', text='Rejon')
        self.tree.heading('four', text='lokalizacja')
        self.tree.heading('five', text='data kontroli')
        self.tree.heading('six', text='data następnej kontroli')

    #tree.insert('', 0, text='line 1', values=('1A', '1B'))

    #id2 = tree.insert('', 1, 'dir2', text='dir 2')
    #tree.insert(id2, 'end', 'dir 2', text='sub dir 2', values=('2A', '2B'))


        self.tree.grid(column=2, row=0, columnspan=2, rowspan=20)


    def add_equip(self):
        class Add_file(Text):
            def __init__(self, master2):
                Text.__init__(self, master2)

                # ---------- labels ----------
                self.typeEq = ttk.Label(master2, text='Typ gaśnicy: ')
                self.sizeEq = ttk.Label(master2, text='Pojemność: ')
                self.typeIn = ttk.Label(master2, text='rodzaj gaśnicy: ')
                self.numEq = ttk.Label(master2, text='Wybierz numer: ')

                self.typeEq.grid(column=0, row=0)
                self.sizeEq.grid(column=0, row=1)
                self.typeIn.grid(column=0, row=2)
                self.numEq.grid(column=0, row=3)

                # ---------- Comboboxes ----------
                self.typeEq = StringVar()
                self.sizeEq = StringVar()
                self.typeIn = StringVar()
                self.numEq = StringVar()

                self.typeEq_entries = ttk.Combobox(master2, width=10, textvariable=self.typeEq)
                self.typeEq_entries['values'] = ('X', 'Z')
                self.typeEq_entries.current(0)

                self.sizeEq_entries = ttk.Combobox(master2, width=10, textvariable=self.sizeEq)
                self.sizeEq_entries['values'] = ('6', '12')

                self.typeIn_entries = ttk.Combobox(master2, width=10, textvariable=self.typeIn)
                self.typeIn_entries['values'] = ('proszek', 'płyn')

                self.numEq_entries = ttk.Combobox(master2, width=10, textvariable=self.numEq)
                self.numEq_entries['values'] = ('z db')

                self.typeEq_entries.grid(column=1, row=0)
                self.sizeEq_entries.grid(column=1, row=1)
                self.typeIn_entries.grid(column=1, row=2)
                self.numEq_entries.grid(column=1, row=3)

                #---------- Buttons ----------

                self.quit = Button(master2, text='Wyjście', command=master2.destroy)
                self.quit.grid(column=1, row=4, columnspan=2)


            #----------destroy button ----------

            def master_exit(self):
                master.destroy()


        #---------- add_equip window look ----------

        root2 = Tk()
        root.geometry('800x600')
        root.title('Dodaj Sprzęt')
        c = Add_file(root2)
        root2.mainloop()

#---------- window look options -----------
root = Tk()
root.geometry('800x600')
root.title('Gaśnica')

b = Application(root)
root.mainloop()

exit()
