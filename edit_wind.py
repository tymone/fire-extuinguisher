from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from database import Database
from treeview import Treeview

class Edit_wind:
    def edit_wind(self):
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError:
            messagebox.showinfo('info', 'Nie zaznaczono przediomtu. Wybierz przedmiot i spróbuj ponownie')
            return

        self.edit()

        self.wind = Tk()
        self.wind.geometry('800x600')
        self.wind.title('Edycja')

        self.n_indeks_var = StringVar()
        self.n_udt_var = StringVar()
        self.n_nr_tank_var = StringVar()
        self.n_type_var = StringVar()
        self.n_size_var = StringVar()
        self.n_type_in_var = StringVar()
        self.n_area_var = StringVar()
        self.n_localize_var = StringVar()
        self.n_controller_var = StringVar()
        self.n_data_var = StringVar()

        self.old_lab = ttk.Label(self.wind, text= 'Obecnie')
        self.new_lab = ttk.Label(self.wind, text='Nowy')
        self.indeks_lab = ttk.Label(self.wind, text='numer:')
        self.indeks_old_lab = ttk.Label(self.wind, text=self.indeks_old)
        self.udt_lab = ttk.Label(self.wind, text='UDT:')
        self.udt_old_lab = ttk.Label(self.wind, text=self.udt_old)
        self.nr_tank_lab = ttk.Label(self.wind, text='Nr. zbiornika:')
        self.tank_num_old_lab = ttk.Label(self.wind, text=self.tank_num_old)
        self.type_lab = ttk.Label(self.wind, text='Typ gaśnicy:')
        self.type_old_lab = ttk.Label(self.wind, text=self.type_old)
        self.size_lab = ttk.Label(self.wind, text='Pojemność:')
        self.size_old_lab = ttk.Label(self.wind, text=self.size_old)
        self.inside_lab = ttk.Label(self.wind, text='Środek gaśniczy:')
        self.inside_old_lab = ttk.Label(self.wind, text=self.inside_old)
        self.area_lab = ttk.Label(self.wind, text='Rejon:')
        self.area_old_lab = ttk.Label(self.wind, text=self.area_old)
        self.localize_lab = ttk.Label(self.wind, text='Lokalizacja:')
        self.localize_old_lab = ttk.Label(self.wind, text=self.localize_old)
        self.controller_lab = ttk.Label(self.wind, text='Osoba kontrolująca:')
        self.person_old_lab = ttk.Label(self.wind, text=self.person_old)
        self.data_lab = ttk.Label(self.wind, text='Data kontroli:')
        self.data_old_lab = ttk.Label(self.wind, text=self.data_old)

        self.n_indeks_ent = ttk.Entry(self.wind, textvariable=self.n_indeks_var)
        self.n_udt_ent = ttk.Entry(self.wind, textvariable=self.n_udt_var)
        self.n_nr_tank_ent = ttk.Entry(self.wind, textvariable=self.n_nr_tank_var)
        self.n_localize_ent = ttk.Entry(self.wind, textvariable=self.n_localize_var)
        self.n_controller_ent = ttk.Entry(self.wind, textvariable=self.n_controller_var)
        self.n_data_ent = ttk.Entry(self.wind, textvariable=self.n_data_var)

        self.save_but = ttk.Button(self.wind, text='Zapisz', command= lambda: 
        self.edit_rec(self.n_indeks_ent.get(), self.indeks_old, self.n_udt_ent.get(), self.udt_old, 
            self.n_nr_tank_ent.get(), self.tank_num_old, self.n_type_cob.get(), self.type_old, self.n_size_cob.get(), 
            self.size_old, self.n_type_in_cob.get(), self.inside_old, self.n_area_cob.get(), self.area_old, 
            self.n_localize_ent.get(), self.localize_old, self.n_controller_ent.get(), self.person_old, 
            self.n_data_ent.get(), self.data_old))

        self.n_type_cob = ttk.Combobox(self.wind, width=19, textvariable=self.n_type_var, state='readonly')
        self.n_type_cob['values'] = ('X', 'Z')
        
        self.n_size_cob = ttk.Combobox(self.wind, width=19, textvariable=self.n_size_var, state='readonly')
        self.n_size_cob['values'] = ('6', '12')
                                
        self.n_type_in_cob = ttk.Combobox(self.wind, width=19, textvariable=self.n_type_in_var, state='readonly')
        self.n_type_in_cob['values'] = ('proszek', 'płyn')
                                
        self.n_area_cob = ttk.Combobox(self.wind, width=19, textvariable=self.n_area_var, state='readonly')
        self.n_area_cob['values'] = ('Rejon 1', 'Rejon 2')

        self.old_lab.grid(column=1, row=0) 
        self.new_lab.grid(column=2, row=0) 
        self.indeks_lab.grid(column=0, row=1)
        self.indeks_old_lab.grid(column=1, row=1)
        self.n_indeks_ent.grid(column=2, row=1)
        self.udt_lab.grid(column=0, row=2)
        self.udt_old_lab.grid(column=1, row=2)
        self.n_udt_ent.grid(column=2, row=2)
        self.nr_tank_lab.grid(column=0, row=3)
        self.tank_num_old_lab.grid(column=1, row=3)
        self.n_nr_tank_ent.grid(column=2, row=3)
        self.type_lab.grid(column=0, row=4)
        self.type_old_lab.grid(column=1, row=4)
        self.n_type_cob.grid(column=2, row=4)
        self.size_lab.grid(column=0, row=5) 
        self.size_old_lab.grid(column=1, row=5) 
        self.n_size_cob.grid(column=2, row=5) 
        self.inside_lab.grid(column=0, row=6) 
        self.inside_old_lab.grid(column=1, row=6) 
        self.n_type_in_cob.grid(column=2, row=6) 
        self.area_lab.grid(column=0, row=7) 
        self.area_old_lab.grid(column=1, row=7) 
        self.n_area_cob.grid(column=2, row=7) 
        self.localize_lab.grid(column=0, row=8)
        self.localize_old_lab.grid(column=1, row=8)
        self.n_localize_ent.grid(column=2, row=8)
        self.controller_lab.grid(column=0, row=9)
        self.person_old_lab.grid(column=1, row=9)
        self.n_controller_ent.grid(column=2, row=9)
        self.data_lab.grid(column=0, row=10)
        self.data_old_lab.grid(column=1, row=10)
        self.n_data_ent.grid(column=2, row=10)
        self.save_but.grid(column=0, row=11, columnspan=3)

        self.wind.mainloop()