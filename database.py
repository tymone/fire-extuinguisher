#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
import time
import datetime
import random
from tkinter import messagebox

class Database:
    db_name = 'equipment.db'

    def initialize_db_connection(self, query, parameters = ()):
        with sqlite3.connect(self.db_name) as con:
            cur = con.cursor()
            cur.execute(""" CREATE TABLE IF NOT EXISTS equipment(id INTEGER PRIMARY KEY ASC, 
                                                                    indeks INTEGER, udt TEXT, tank TEXT, type TEXT,
                                                                    size INTEGER, inside TEXT, area INTEGER, 
                                                                    localize TEXT, dateadd TEXT, person TEXT)""")
            query_result = cur.execute(query, parameters)
            con.commit()
        return query_result

    def view_records(self):
        records = self.tree.get_children()
        for item in records:
            self.tree.delete(item)
        query = 'SELECT * FROM equipment ORDER BY indeks ASC'
        db_rows = self.initialize_db_connection(query)
        cpt = 1
        for row in db_rows:
            self.tree.insert('', 'end', text=str(cpt),
                             values=(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))
            cpt += 1

    def validation(self):
        return len(self.numEq_var.get()) != 0 \
               or len(self.typeEQ_var.get()) != 0 \
               or len(self.udt_var.get()) != 0 \
               or len(self.tankNum_var.get()) !=0 \
               or len(self.sizeEq_var.get()) != 0 \
               or len(self.typeIn_var.get()) != 0 \
               or len(self.area_var.get()) !=0 \
               or len(self.localization_var.get()) !=0 \
               or len(self.person_var.get()) != 0 \
               or len(self.date_var.get() != 0)

    def adding(self):
        if self.validation():
            query = 'INSERT INTO equipment VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
            parameters = (self.numEq_var.get(), self.udt_var.get(), self.tankNum_var.get(), self.typeEq_var.get(), \
                          self.sizeEq_var.get(), self.typeIn_var.get(), self.area_var.get(), \
                          self.localization_var.get(), self.person_var.get(), self.date_var.get())
            self.initialize_db_connection(query, parameters)
            messagebox.showinfo('Info', 'Pomyślnie dodano sprzęt do bazy danych!')
            self.numEq_ent.delete (1, 1)
            self.udt_ent.delete (2, 2)
            self.tankNum_ent.delete (3, 3)
            self.typeEq_cob.delete (4, 4)
            self.sizeEq_cob.delete (5, 5)
            self.typeIn_cob.delete (6, 6)
            self.area_cob.delete (7, 7)
            self.localization_ent.delete (8, 8)
            self.person_ent.delete (9, 9)
            self.date_ent.delete (10, 10)

        else:
            messagebox.showinfo('info', 'Nie wszystkie pola zostały wypełnione poprawnie.')

        self.view_records()

    def deleting(self):
        try:
            self.tree.item(self.tree.selection())['values'][1]
        except IndexError as e:
            messagebox.showinfo('info', 'Nie wybrano przedmiotu. Zaznacz przedmiot i spróbuj ponownie.')
            return

        name = self.tree.item(self.tree.selection())['text']
        query = 'DELETE FROM equipment WHERE indeks = ?'
        self.initialize_db_connection(query, (name, ))
        messagebox.showinfo('info', 'Przedmiot został usunięty.')
        self.view_records()

