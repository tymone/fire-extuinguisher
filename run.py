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

        self.find_lab = ttk.Label(master, text='Wyszukaj:')
        self.find_lab.grid(column=0, row=0, columnspan=2)

        self.find_var = StringVar()
        self.find_ent = tk.Entry(master, textvariable=self.find_var)
        self.find_ent.grid(column=0, row=1, columnspan=2)

        self.find_but = Button(master, text='Szukaj', command=self.load_settings)
        self.find_but.grid(column=0, row=2, columnspan=2)

        self.area_lab = ttk.Label(master, text='Rejon:')
        self.area_lab.grid(column=0, row=3, columnspan=2)

        self.area1_var = IntVar()
        self.area1_chb = tk.Checkbutton(master, text='Rejon 1', variable=self.area1_var)
        self.area1_chb.grid(column=0, row=4, columnspan=1, rowspan=1)

        self.area2_var = IntVar()
        self.area2_chb = tk.Checkbutton(master, text='Rejon 2', variable=self.area2_var)
        self.area2_chb.grid(column=1, row=4, columnspan=1, rowspan=1)

        self.sort_lab = ttk.Label(master, text='Sortuj wg:')
        self.sort_lab.grid(column=0, row=5, columnspan=2)

        self.num_rab = tk.Radiobutton(master, text='numeru')
        self.num_rab.grid(column=0, row=6, columnspan=1, rowspan=1)

        self.localization_rab = tk.Radiobutton(master, text='lokalizacji')
        self.localization_rab.grid(column=1, row=6, columnspan=1, rowspan=1)

        self.add_lab = ttk.Label(master, text='Dodaj sprzęt')
        self.add_lab.grid(column=0, row=7, columnspan=2)

        self.typeEq_lab = ttk.Label(master, text='Typ gaśnicy: ')
        self.typeEq_lab.grid(column=0, row=8, columnspan=2)

        self.typeEq_var = StringVar()
        self.typeEq_cob = ttk.Combobox(master, width=10, textvariable=self.typeEq_var)
        self.typeEq_cob['values'] = ('X', 'Z')
        self.typeEq_cob.current(0)
        self.typeEq_cob.grid(column=0, row=9, columnspan=2)

        self.sizeEq_lab = ttk.Label(master, text='Pojemność:')
        self.sizeEq_lab.grid(column=0, row=10, columnspan=2)

        self.sizeEq_var = StringVar()
        self.sizeEq_cob = ttk.Combobox(master, width=10, textvariable=self.sizeEq_var)
        self.sizeEq_cob['values'] = ('6', '12')
        self.sizeEq_cob.grid(column=0, row=11, columnspan=2)

        self.typeIn_lab = ttk.Label(master, text='Środek gaśniczy: ')
        self.typeIn_lab.grid(column=0, row=12, columnspan=2)

        self.typeIn_var = StringVar()
        self.typeIn_cob = ttk.Combobox(master, width=10, textvariable=self.typeIn_var)
        self.typeIn_cob['values'] = ('proszek', 'płyn')
        self.typeIn_cob.grid(column=0, row=13, columnspan=2)

        self.area_lab = ttk.Label(master, text='Rejon')
        self.area_lab.grid(column=0, row=14, columnspan=2)

        self.area_var = StringVar()
        self.area_cob = ttk.Combobox(master, width=10, textvariable=self.area_var)
        self.area_cob['values'] = ('Rejon 1', 'Rejon 2')
        self.area_cob.grid(column=0, row=15, columnspan=2)

        self.localization_lab = ttk.Label(master, text='Lokalizacja:')
        self.localization_lab.grid(column=0, row=16, columnspan=2)

        self.localization_var = StringVar()
        self.localization_ent = ttk.Entry(master, width=10, textvariable=self.localization_var)
        self.localization_ent.grid(column=0, row=17, columnspan=2)

        self.numEq_lab = ttk.Label(master, text='Wybierz numer: ')
        self.numEq_lab.grid(column=0, row=18, columnspan=2)

        self.numEq_var = StringVar()
        self.numEq_ent = ttk.Entry(master, width=10, textvariable=self.numEq_var)
        self.numEq_ent.grid(column=0, row=19, columnspan=2)

        self.add_but = Button(master, text='Zapisz w bazie', command=self.save_settings)
        self.add_but.grid(column=0, row=20)

        self.quit_but = Button(master, text='Wyjście', command=master.destroy)
        self.quit_but.grid(column=1, row=20)

        #---------- treeview ----------

        self.tree = ttk.Treeview(height=30, columns=('Nr. gaśnicy', 'Typ gaśnicy','Pojemność','Środek', 'Rejon',
                                                     'lokalizacja', 'data kontroli', 'Osoba kontrolująca'))
        self.tree.grid(column=2, row=0, rowspan=20)
        self.tree.heading('#0', text='Index', anchor=W)
        self.tree.heading('Nr. gaśnicy', text='Nr. gaśnicy', anchor=W)
        self.tree.heading('Typ gaśnicy', text='Typ gaśnicy', anchor=W)
        self.tree.heading('Pojemność', text='Pojemność', anchor=W)
        self.tree.heading('Środek', text='Środek', anchor=W)
        self.tree.heading('Rejon', text='Rejon', anchor=W)
        self.tree.heading('lokalizacja', text='lokalizacja', anchor=W)
        self.tree.heading('data kontroli', text='data kontroli', anchor=W)
        self.tree.heading('Osoba kontrolująca', text='Osoba kontrolująca', anchor=W)

        self.tree.column('#0', stretch=tk.NO, width=50)
        self.tree.column('Nr. gaśnicy', stretch=tk.NO, width=70)
        self.tree.column('Typ gaśnicy', stretch=tk.NO, width=70)
        self.tree.column('Pojemność', stretch=tk.NO, width=70)
        self.tree.column('Środek', stretch=tk.NO, width=70)
        self.tree.column('Rejon', stretch=tk.NO, width=50)
        self.tree.column('lokalizacja', stretch=tk.YES, minwidth=50, width=300)
        self.tree.column('data kontroli', stretch=tk.NO, width=150)
        self.tree.column('Osoba kontrolująca', stretch=tk.NO, width=150)


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

        indeks = self.numEq_var.get()
        type = self.typeEq_var.get()
        size = self.sizeEq_var.get()
        inside = self.typeIn_var.get()
        dateadd = datetime.date.today()
        datacontrol = datetime.date.today()
        if len(type) == 0 or len(size) == 0 or len(inside) == 0:
            print('Nie wszystkie pola zostały wypełnione prawidłowo, spróbuj ponownie!')
            messagebox.showwarning('Nie wszystkie pola zostały wypłnione prawidłowo, spróbuj ponownie!')

        else:
            cur.execute('INSERT INTO equipment (indeks, type, size, inside, dateadd) VALUES (?, ?, ?, ?, ?)',
                (indeks, type, size, inside, dateadd))
            con.commit()
            messagebox.showinfo('Info', 'Pomyślnie dodano sprzęt do bazy danych!')

    def load_settings(self):

        con = sqlite3.connect('equipment.db')
        con.row_factory = sqlite3.Row
        cur = con.cursor()

        findies = self.find_var.get()
        cur.execute('SELECT * FROM equipment WHERE indeks LIKE ?',(findies,))

        equip = cur.fetchall()
        for item in equip:
                print(item['indeks'], item['type'], item['size'], item['inside'], item['dateadd'])


    def viewing_records(self):
        conn = sqlite3.connect('equipment.db')
        cur = conn.cursor()
        cur.execute('SELECT * FROM equipment')
        rows = cur.fetchall()
        cpt = 1
        for row in rows:
            self.tree.insert('', 'end', text=str(cpt), values=(row[1], row[2], row[3], row[4],'' ,'' ,row[5]))
            cpt += 1
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
