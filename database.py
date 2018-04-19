#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
import time
import datetime
import random
from tkinter import messagebox

class Database():
    def initialize_db_connection(self):
        con = sqlite3.connect('equipment.db')
        con.row_factory = sqlite3.Row
        cur = con.cursor()

        cur.execute("""
                            CREATE TABLE IF NOT EXISTS equipment(id INTEGER PRIMARY KEY ASC,
                            indeks INTEGER, udt TEXT, tank TEXT, type TEXT, size INTEGER, inside TEXT, area INTEGER, localize TEXT,
                            dateadd TEXT, person TEXT)""")

        cur.execute('SELECT * FROM equipment')
        cur.execute('SELECT * FROM equipment ORDER BY indeks ASC')
        rows = cur.fetchall()
        cpt = 1
        for row in rows:
            self.tree.insert('', 'end', text=str(cpt),
                             values=(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[10], row[9]))
            cpt += 1

    def save_settings(self):

        indeks = self.numEq_var.get()
        udt = self.udt_var.get()
        tank = self.tankNum_var.get()
        type = self.typeEq_var.get()
        size = self.sizeEq_var.get()
        inside = self.typeIn_var.get()
        area = self.area_var.get()
        localize = self.localization_var.get()
        person = self.person_var.get()
        dateadd = self.date_var.get()
        datacontrol = datetime.date.today()
        if len(type) == 0 or len(udt) == 0 or len(tank) ==0 or len(size) == 0 or len(inside) == 0 or len(area) ==0 or len(localize) ==0 or len(person) == 0:
            print('Nie wszystkie pola zostały wypełnione prawidłowo, spróbuj ponownie!')
            messagebox.showwarning('Nie wszystkie pola zostały wypłnione prawidłowo, spróbuj ponownie!')

        else:
            con = sqlite3.connect('equipment.db')
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("""
                            INSERT INTO equipment 
                            (indeks, udt, tank, type, size, inside, area, localize, dateadd, person) 
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                        (indeks, udt, tank, type, size, inside, area, localize, dateadd, person))

            messagebox.showinfo('Info', 'Pomyślnie dodano sprzęt do bazy danych!')

            con.commit()

    def delete(self):
        conn = sqlite3.connect("equipment.db")
        cur = conn.cursor()
        for selected_item in self.tree.selection():
            print(selected_item)  # it prints the selected row id
            cur.execute("DELETE FROM equipment WHERE id=?", (self.tree.set(selected_item, '#1'),))
            conn.commit()
            self.tree.delete(selected_item)

