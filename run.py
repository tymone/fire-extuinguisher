#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
import tkinter as tk
import sqlite3
import time
import datetime
import random
from tkinter import messagebox
import subprocess as s


class Application():
    def __init__(self, master):

        #---------- buttons ----------

        self.find = Button(master, text='Szukaj', command=self.load_settings)
        self.add = Button(master, text='Zapisz w bazie', command=self.save_settings)
        self.quit = Button(master, text='Wyjście', command=master.destroy)

        self.find.grid(column=0, row=2, columnspan=2)
        self.add.grid(column=0, row=16)
        self.quit.grid(column=1, row=16)

        # ---------- label ----------

        self.find = ttk.Label(master, text='Wyszukaj:')
        self.show_area = ttk.Label(master, text='Rejon:')
        self.sort = ttk.Label(master, text='Sortuj wg:')
        self.add = ttk.Label(master, text='Dodaj sprzęt')
        self.typeEq = ttk.Label(master, text='Typ gaśnicy: ')
        self.sizeEq = ttk.Label(master, text='Pojemność: ')
        self.typeIn = ttk.Label(master, text='rodzaj gaśnicy: ')
        self.numEq = ttk.Label(master, text='Wybierz numer: ')

        self.find.grid(column=0, row=0, columnspan=2)
        self.show_area.grid(column=0, row=3, columnspan=2)
        self.sort.grid(column=0, row=5, columnspan=2)
        self.add.grid(column=0, row=7, columnspan=2)
        self.typeEq.grid(column=0, row=8, columnspan=2)
        self.sizeEq.grid(column=0, row=10, columnspan=2)
        self.typeIn.grid(column=0, row=12, columnspan=2)
        self.numEq.grid(column=0, row=14, columnspan=2)

        #----------- Entries -----------

        self.findies = StringVar()
        self.find_entries = tk.Entry(master, textvariable=self.findies)

        self.find_entries.grid(column=0, row=1, columnspan=2)

        # ---------- Comboboxes ----------
        self.typeEq = StringVar()
        self.sizeEq = StringVar()
        self.typeIn = StringVar()
        self.numEq = StringVar()

        self.typeEq_entries = ttk.Combobox(master, width=10, textvariable=self.typeEq)
        self.typeEq_entries['values'] = ('X', 'Z')
        self.typeEq_entries.current(0)

        self.sizeEq_entries = ttk.Combobox(master, width=10, textvariable=self.sizeEq)
        self.sizeEq_entries['values'] = ('6', '12')

        self.typeIn_entries = ttk.Combobox(master, width=10, textvariable=self.typeIn)
        self.typeIn_entries['values'] = ('proszek', 'płyn')

        self.numEq_entries = ttk.Entry(master, width=10, textvariable=self.numEq)

        self.typeEq_entries.grid(column=0, row=9, columnspan=2)
        self.sizeEq_entries.grid(column=0, row=11, columnspan=2)
        self.typeIn_entries.grid(column=0, row=13, columnspan=2)
        self.numEq_entries.grid(column=0, row=15, columnspan=2)

        #---------- check buttons ----------

        self.area1_var = IntVar()
        self.area1 = tk.Checkbutton(master, text='Rejon 1', variable=self.area1_var)

        self.area2_var = IntVar()
        self.area2 = tk.Checkbutton(master, text='Rejon 2', variable=self.area2_var)

        self.area1.grid(column=0, row=4, columnspan=1, rowspan=1)
        self.area2.grid(column=1, row=4, columnspan=1, rowspan=1)

        #---------- radio buttons ----------

        self.num = tk.Radiobutton(master, text='numeru')
        self.localization = tk.Radiobutton(master, text='lokalizacji',)

        self.num.grid(column=0, row=6, columnspan=1, rowspan=1)
        self.localization.grid(column=1, row=6, columnspan=1, rowspan=1)

        #---------- treeview ----------

        self.tree = ttk.Treeview(height=30, columns=('Nr. gaśnicy', 'Typ gaśnicy','Pojemność','Środek', 'Rejon', 'lokalizacja', 'data kontroli', 'data następnej kontroli'))
        self.tree.grid(column=2, row=0, rowspan=20)
        self.tree.heading('#0', text='Index', anchor=W)
        self.tree.heading('Nr. gaśnicy', text='Nr. gaśnicy', anchor=W)
        self.tree.heading('Typ gaśnicy', text='Typ gaśnicy', anchor=W)
        self.tree.heading('Pojemność', text='Pojemność', anchor=W)
        self.tree.heading('Środek', text='Środek', anchor=W)
        self.tree.heading('Rejon', text='Rejon', anchor=W)
        self.tree.heading('lokalizacja', text='lokalizacja', anchor=W)
        self.tree.heading('data kontroli', text='data kontroli', anchor=W)
        self.tree.heading('data następnej kontroli', text='data następnej kontroli', anchor=W)

        self.tree.column('#0', stretch=tk.NO, width=50)
        self.tree.column('Nr. gaśnicy', stretch=tk.NO, width=70)
        self.tree.column('Typ gaśnicy', stretch=tk.NO, width=70)
        self.tree.column('Pojemność', stretch=tk.NO, width=70)
        self.tree.column('Środek', stretch=tk.NO, width=70)
        self.tree.column('Rejon', stretch=tk.NO, width=50)
        self.tree.column('lokalizacja', stretch=tk.YES, minwidth=50, width=300)
        self.tree.column('data kontroli', stretch=tk.NO, width=150)
        self.tree.column('data następnej kontroli', stretch=tk.NO, width=150)


        self.viewing_records()


    #---------- database ----------



    def save_settings(self):
        con = sqlite3.connect('equipment.db')
        con.row_factory = sqlite3.Row
        cur = con.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS equipment(id INTEGER PRIMARY KEY ASC,
             indeks TEXT, type TEXT, size TEXT, inside TEXT, dateadd TEXT)""")

        # ---------- adding items ---------

        indeks = self.numEq.get()
        type = self.typeEq.get()
        size = self.sizeEq.get()
        inside = self.typeIn.get()
        dateadd = datetime.date.today()
        datacontrol = datetime.date.today()
        if len(type) == 0 or len(size) == 0 or len(inside) == 0:
            print('Nie wszystkie pola zostały wypełnione prawidłowo, spróbuj ponownie!')
            messagebox.showwarning('Nie wszystkie pola zostały wypłnione prawidłowo, spróbuj ponownie!')

        else:
            cur.execute('INSERT INTO equipment (indeks, type, size, inside, dateadd) VALUES (?, ?, ?, ?, ?)',
                (indeks, type, size, inside, dateadd))
            con.commit()
            messagebox.showinfo('Pomyślnie dodano sprzęt do bazy danych!')

    def load_settings(self):

        con = sqlite3.connect('equipment.db')
        con.row_factory = sqlite3.Row
        cur = con.cursor()

        findies = self.findies.get()
        cur.execute('SELECT * FROM equipment WHERE indeks LIKE ?',(findies,))

        equip = cur.fetchall()
        for item in equip:
                print(item['indeks'], item['type'], item['size'], item['inside'], item['dateadd'])


    def viewing_records(self):
        conn = sqlite3.connect('equipment.db')
        cur = conn.cursor()
        cur.execute('SELECT * FROM equipment')
        rows = cur.fetchall()
        for row in rows:
            print(row)
            self.tree.insert('', tk.END, values=row)
        conn.close()


    # ----------destroy button ----------

    def master_exit(self):
        self.destroy()

if __name__ == '__main__':
    root = Tk()
    root.geometry('1200x700')
    root.title('Gaśnica')
    run = Application(root)
    root.mainloop()
    exit()
