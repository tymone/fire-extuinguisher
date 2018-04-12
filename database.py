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
import sys

class Database():
    def initialize_db_connection(self):
        con = sqlite3.connect('equipment.db')
        con.row_factory = sqlite3.Row
        cur = con.cursor()

        cur.execute("""
                            CREATE TABLE IF NOT EXISTS equipment(id INTEGER PRIMARY KEY ASC,
                            indeks INTEGER, type TEXT, size INTEGER, inside TEXT, area INTEGER, localize TEXT,
                            dateadd TEXT, person TEXT)""")

        cur.execute('SELECT * FROM equipment')
        rows = cur.fetchall()
        cpt = 1
        for row in rows:
            self.tree.insert('', 'end', text=str(cpt), values=(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
            cpt += 1


    def save_settings(self):

        indeks = self.numEq_var.get()
        type = self.typeEq_var.get()
        size = self.sizeEq_var.get()
        inside = self.typeIn_var.get()
        area = self.area_var.get()
        localize = self.localization_var.get()
        person = self.person_var.get()

        dateadd = datetime.date.today()
        datacontrol = datetime.date.today()
        if len(type) == 0 or len(size) == 0 or len(inside) == 0:
            print('Nie wszystkie pola zostały wypełnione prawidłowo, spróbuj ponownie!')
            messagebox.showwarning('Nie wszystkie pola zostały wypłnione prawidłowo, spróbuj ponownie!')

        else:
            con = sqlite3.connect('equipment.db')
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute('INSERT INTO equipment (indeks, type, size, inside, area, localize, dateadd, person) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                        (indeks, type, size, inside, area, localize, dateadd, person))
            con.commit()
            messagebox.showinfo('Info', 'Pomyślnie dodano sprzęt do bazy danych!')


        # polaczenie z baza danych
        # + trzymanie tego w obiekcie
        # self.con =

    #def create_schema(db_connection):
        # check if equipment.db exists, return true
        # create empty file
        # init db conn
        # create tables
        #pass
