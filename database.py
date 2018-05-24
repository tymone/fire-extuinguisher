#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
import time
import datetime
from tkinter import messagebox
from treeview import Treeview

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

    def add(self):
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
            self.view_records()

        else:
            messagebox.showinfo('info', 'Nie wszystkie pola zostały wypełnione poprawnie.')

        
        
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

    def delete(self):
        try:
            name = self.tree.item(self.tree.selection())['values'][0]
            print(name)
        except IndexError as e:
            messagebox.showinfo('info', 'Nie wybrano przedmiotu. Zaznacz przedmiot i spróbuj ponownie.')
            return

        name = self.tree.item(self.tree.selection())['values'][0]
        print(name)
        query = 'DELETE FROM equipment WHERE indeks = ?'
        self.initialize_db_connection(query, (name, ))
        messagebox.showinfo('info', 'Przedmiot został usunięty.')
        self.view_records()

    def edit(self):

        self.indeks_old = self.tree.item(self.tree.selection())['values'][0]
        self.udt_old = self.tree.item(self.tree.selection())['values'][1]
        self.tank_num_old = self.tree.item(self.tree.selection())['values'][2]
        self.type_old = self.tree.item(self.tree.selection())['values'][3]
        self.size_old = self.tree.item(self.tree.selection())['values'][4]
        self.inside_old = self.tree.item(self.tree.selection())['values'][5]
        self.area_old = self.tree.item(self.tree.selection())['values'][6]
        self.localize_old = self.tree.item(self.tree.selection())['values'][7]
        self.person_old = self.tree.item(self.tree.selection())['values'][8]
        self.data_old = self.tree.item(self.tree.selection())['values'][9]

    def edit_rec(self, n_indeks_var, indeks_old, n_udt_var, udt_old, n_nr_tank_var, tank_num_old, n_type_var,\
                    type_old, n_size_var, size_old, n_inside_var, inside_old, n_area_var, area_old, n_localize_var,\
                    localize_old, n_controller_var, person_old, n_data_var, data_old):

        query = """UPDATE equipment SET indeks = ?, udt = ?, tank = ?, type = ?, size = ?, inside = ?, area = ?,
                    localize = ?, dateadd = ?, person = ? WHERE indeks = ? AND udt = ? AND tank = ? AND 
                    type = ? AND size = ? AND inside = ? AND area = ? AND localize = ? AND dateadd = ? AND person = ?"""

        parameters = (n_indeks_var, n_udt_var, n_nr_tank_var, n_type_var, n_size_var, n_inside_var, n_area_var,\
                      n_localize_var, n_controller_var, n_data_var, indeks_old, udt_old, tank_num_old, type_old,\
                      size_old, inside_old, area_old, localize_old, person_old, data_old)

        self.initialize_db_connection(query, parameters)
        self.wind.destroy()
        messagebox.showinfo('info', 'Zapisano zmiany')

        self.view_records()

    def find(self):
      records = self.tree.get_children()
      for item in records:
          self.tree.delete(item)
      query = 'SELECT * FROM equipment WHERE indeks LIKE ?'
      name = self.find_var.get()
      db_rows = self.initialize_db_connection(query, (name,))
      cpt = 1
      for row in db_rows:
        self.tree.insert('', 'end', text=str(cpt),
          values=(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))
        cpt += 1
    

    
        


