from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox

class Gui():
    def init_gui(self):
        self.find_lab = ttk.Label(text='Wyszukaj:')
        self.find_lab.grid(column=0, row=0, columnspan=2)

        self.find_var = StringVar()
        self.find_ent = tk.Entry()
        self.find_ent.grid(column=0, row=1, columnspan=2)

        self.find_but = Button(text='Szukaj')
        self.find_but.grid(column=0, row=2, columnspan=2)

        self.area_lab = ttk.Label(text='Rejon:')
        self.area_lab.grid(column=0, row=3, columnspan=2)

        self.area1_var = IntVar()
        self.area1_chb = tk.Checkbutton(text='Rejon 1', variable=self.area1_var)
        self.area1_chb.grid(column=0, row=4, columnspan=1, rowspan=1)

        self.area2_var = IntVar()
        self.area2_chb = tk.Checkbutton(text='Rejon 2', variable=self.area2_var)
        self.area2_chb.grid(column=1, row=4, columnspan=1, rowspan=1)

        self.sort_lab = ttk.Label(text='Sortuj wg:')
        self.sort_lab.grid(column=0, row=5, columnspan=2)

        self.num_rab = tk.Radiobutton(text='numeru')
        self.num_rab.grid(column=0, row=6, columnspan=1, rowspan=1)

        self.localization_rab = tk.Radiobutton(text='lokalizacji')
        self.localization_rab.grid(column=1, row=6, columnspan=1, rowspan=1)

        self.add_lab = ttk.Label(text='Dodaj sprzęt')
        self.add_lab.grid(column=0, row=7, columnspan=2)

        self.typeEq_lab = ttk.Label(text='Typ gaśnicy: ')
        self.typeEq_lab.grid(column=0, row=8, columnspan=2)

        self.typeEq_var = StringVar()
        self.typeEq_cob = ttk.Combobox(width=10, textvariable=self.typeEq_var)
        self.typeEq_cob['values'] = ('X', 'Z')
        self.typeEq_cob.current(0)
        self.typeEq_cob.grid(column=0, row=9, columnspan=2)

        self.sizeEq_lab = ttk.Label(text='Pojemność:')
        self.sizeEq_lab.grid(column=0, row=10, columnspan=2)

        self.sizeEq_var = StringVar()
        self.sizeEq_cob = ttk.Combobox(width=10, textvariable=self.sizeEq_var)
        self.sizeEq_cob['values'] = ('6', '12')
        self.sizeEq_cob.grid(column=0, row=11, columnspan=2)

        self.typeIn_lab = ttk.Label(text='Środek gaśniczy: ')
        self.typeIn_lab.grid(column=0, row=12, columnspan=2)

        self.typeIn_var = StringVar()
        self.typeIn_cob = ttk.Combobox(width=10, textvariable=self.typeIn_var)
        self.typeIn_cob['values'] = ('proszek', 'płyn')
        self.typeIn_cob.grid(column=0, row=13, columnspan=2)

        self.area_lab = ttk.Label(text='Rejon')
        self.area_lab.grid(column=0, row=14, columnspan=2)

        self.area_var = StringVar()
        self.area_cob = ttk.Combobox(width=10, textvariable=self.area_var)
        self.area_cob['values'] = ('Rejon 1', 'Rejon 2')
        self.area_cob.grid(column=0, row=15, columnspan=2)

        self.localization_lab = ttk.Label(text='Lokalizacja:')
        self.localization_lab.grid(column=0, row=16, columnspan=2)

        self.localization_var = StringVar()
        self.localization_ent = ttk.Entry(width=10, textvariable=self.localization_var)
        self.localization_ent.grid(column=0, row=17, columnspan=2)

        self.numEq_lab = ttk.Label(text='Wybierz numer: ')
        self.numEq_lab.grid(column=0, row=18, columnspan=2)

        self.numEq_var = StringVar()
        self.numEq_ent = ttk.Entry(width=10, textvariable=self.numEq_var)
        self.numEq_ent.grid(column=0, row=19, columnspan=2)

        self.add_but = Button(text='Zapisz w bazie', command=self.save_settings)
        self.add_but.grid(column=0, row=20)

        self.quit_but = Button(text='Wyjście', command=exit)
        self.quit_but.grid(column=1, row=20)

        # ---------- treeview ----------

        self.tree = ttk.Treeview(height=30, columns=('Nr. gaśnicy', 'Typ gaśnicy', 'Pojemność', 'Środek', 'Rejon',
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

    def exit():
        destroy()