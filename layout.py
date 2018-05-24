#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from database import Database
from treeview import Treeview
from edit_wind import Edit_wind

class Gui:
    def init_gui(self):

        self.find_var = StringVar()
        self.udt_var = StringVar()
        self.tankNum_var = StringVar()
        self.typeEq_var = StringVar()
        self.sizeEq_var = StringVar()
        self.typeIn_var = StringVar()
        self.area_var = StringVar()
        self.numEq_var = StringVar()
        self.localization_var = StringVar()
        self.date_var = StringVar()
        self.person_var = StringVar()

        self.find_lab = ttk.Label(text='Wyszukaj:').grid(column=0, row=0, columnspan=3)
        self.add_lab = ttk.Label(text='Dodaj sprzęt:').grid(column=0, row=3, columnspan=4)
        self.udt_lab = ttk.Label(text='UDT:').grid(column=0, row=4)
        self.tankNum_lab = ttk.Label(text='Nr. Zbiornika:').grid(column=0, row=5)
        self.typeEq_lab = ttk.Label(text='Typ gaśnicy: ').grid(column=0, row=6)
        self.sizeEq_lab = ttk.Label(text='Pojemność:').grid(column=0, row=7)
        self.typeIn_lab = ttk.Label(text='Środek gaśniczy: ').grid(column=0, row=8) 
        self.area_lab = ttk.Label(text='Rejon').grid(column=0, row=9)
        self.numEq_lab = ttk.Label(text='Wybierz numer: ').grid(column=0, row=10)
        self.localization_lab = ttk.Label(text='Lokalizacja:').grid(column=0, row=11)
        self.date_lab = ttk.Label(text='Data kontroli:').grid(column=0, row=12)
        self.person_lab = ttk.Label(text='Osoba kontruląca:').grid(column=0, row=13)

        self.find_ent = tk.Entry(width=15, textvariable=self.find_var)
        self.udt_ent = ttk.Entry(width=15, textvariable=self.udt_var)
        self.tankNum_ent = ttk.Entry(width=15, textvariable=self.tankNum_var)
        self.numEq_ent = ttk.Entry(width=15, textvariable=self.numEq_var)
        self.localization_ent = ttk.Entry(width=15, textvariable=self.localization_var)
        self.date_ent = ttk.Entry(width=15, textvariable=self.date_var) 
        self.person_ent = ttk.Entry(width=15, textvariable=self.person_var)

        self.find_but = Button(text='Szukaj', command=self.find).grid(column=0, row=2, columnspan=3)
        self.add_but = Button(text='Zapisz w bazie', command=self.add).grid(column=0, row=14)
        self.delete_but = Button(text='Usuń z bazy', command=self.delete).grid(column=1, row=14) 
        self.edit_but = Button(text='Edytuj', command=self.edit_wind).grid(column=2, row=14)
        self.quit_but = Button(text='Wyjście', command=exit).grid(column=0, row=15, columnspan=3)
            
        self.typeEq_cob = ttk.Combobox(width=13, textvariable=self.typeEq_var, state='readonly')
        self.typeEq_cob['values'] = ('X', 'Z')
        self.typeEq_cob.grid(column=1, row=6, columnspan=2)
        
        self.sizeEq_cob = ttk.Combobox(width=13, textvariable=self.sizeEq_var, state='readonly')
        self.sizeEq_cob['values'] = ('6', '12')
        self.sizeEq_cob.grid(column=1, row=7, columnspan=2)
        
        self.typeIn_cob = ttk.Combobox(width=13, textvariable=self.typeIn_var, state='readonly')
        self.typeIn_cob['values'] = ('proszek', 'płyn')
        self.typeIn_cob.grid(column=1, row=8, columnspan=2)
        
        self.area_cob = ttk.Combobox(width=13, textvariable=self.area_var, state='readonly')
        self.area_cob['values'] = ('Rejon 1', 'Rejon 2')
        self.area_cob.grid(column=1, row=9, columnspan=2)

        self.find_ent.grid(column=0, row=1, columnspan=3)
        self.udt_ent.grid(column=1, row=4, columnspan=2)
        self.tankNum_ent.grid(column=1, row=5, columnspan=2)
        self.numEq_ent.grid(column=1, row=10, columnspan=2)
        self.localization_ent.grid(column=1, row=11, columnspan=2)
        self.date_ent.grid(column=1, row=12, columnspan=2)
        self.person_ent.grid(column=1, row=13, columnspan=2)




        # ---------- treeview ----------
        self.treeview()        

    def exit():
        destroy()

