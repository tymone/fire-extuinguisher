from tkinter import *
from tkinter import ttk
import tkinter as tk

class Gui():
    def init_gui(self):
        self.find_lab = ttk.Label(text='Wyszukaj:')
        self.find_lab.grid(column=0, row=0, columnspan=3)

        self.find_var = StringVar()
        self.find_ent = tk.Entry()
        self.find_ent.grid(column=0, row=1, columnspan=3)

        self.find_but = Button(text='Szukaj')
        self.find_but.grid(column=0, row=2, columnspan=3)

        self.add_lab = ttk.Label(text='Dodaj sprzęt:')
        self.add_lab.grid(column=0, row=3, columnspan=4)

        self.udt_lab = ttk.Label(text='UDT:')
        self.udt_lab.grid(column=0, row=4)

        self.udt_var = StringVar()
        self.udt_ent = ttk.Entry(width=15, textvariable=self.udt_var)
        self.udt_ent.grid(column=1, row=4, columnspan=2)

        self.tankNum_lab = ttk.Label(text='Nr. Zbiornika:')
        self.tankNum_lab.grid(column=0, row=5)

        self.tankNum_var = StringVar()
        self.tankNum_ent = ttk.Entry(width=15, textvariable=self.tankNum_var)
        self.tankNum_ent.grid(column=1, row=5, columnspan=2)

        self.typeEq_lab = ttk.Label(text='Typ gaśnicy: ')
        self.typeEq_lab.grid(column=0, row=6)

        self.typeEq_var = StringVar()
        self.typeEq_cob = ttk.Combobox(width=13, textvariable=self.typeEq_var)
        self.typeEq_cob['values'] = ('X', 'Z')
        self.typeEq_cob.current(0)
        self.typeEq_cob.grid(column=1, row=6, columnspan=2)

        self.sizeEq_lab = ttk.Label(text='Pojemność:')
        self.sizeEq_lab.grid(column=0, row=7)

        self.sizeEq_var = StringVar()
        self.sizeEq_cob = ttk.Combobox(width=13, textvariable=self.sizeEq_var)
        self.sizeEq_cob['values'] = ('6', '12')
        self.sizeEq_cob.grid(column=1, row=7, columnspan=2)

        self.typeIn_lab = ttk.Label(text='Środek gaśniczy: ')
        self.typeIn_lab.grid(column=0, row=8)

        self.typeIn_var = StringVar()
        self.typeIn_cob = ttk.Combobox(width=13, textvariable=self.typeIn_var)
        self.typeIn_cob['values'] = ('proszek', 'płyn')
        self.typeIn_cob.grid(column=1, row=8, columnspan=2)

        self.area_lab = ttk.Label(text='Rejon')
        self.area_lab.grid(column=0, row=9)

        self.area_var = StringVar()
        self.area_cob = ttk.Combobox(width=13, textvariable=self.area_var)
        self.area_cob['values'] = ('Rejon 1', 'Rejon 2')
        self.area_cob.grid(column=1, row=9, columnspan=2)

        self.numEq_lab = ttk.Label(text='Wybierz numer: ')
        self.numEq_lab.grid(column=0, row=10)

        self.numEq_var = StringVar()
        self.numEq_ent = ttk.Entry(width=15, textvariable=self.numEq_var)
        self.numEq_ent.grid(column=1, row=10, columnspan=2)

        self.localization_lab = ttk.Label(text='Lokalizacja:')
        self.localization_lab.grid(column=0, row=11)

        self.localization_var = StringVar()
        self.localization_ent = ttk.Entry(width=15, textvariable=self.localization_var)
        self.localization_ent.grid(column=1, row=11, columnspan=2)

        self.date_lab = ttk.Label(text='Data kontroli:')
        self.date_lab.grid(column=0, row=12)

        self.date_var = StringVar()
        self.date_ent = ttk.Entry(width=15, textvariable=self.date_var)
        self.date_ent.grid(column=1, row=12, columnspan=2)

        self.person_lab = ttk.Label(text='Osoba kontruląca:')
        self.person_lab.grid(column=0, row=13)

        self.person_var = StringVar()
        self.person_ent = ttk.Entry(width=15, textvariable=self.person_var)
        self.person_ent.grid(column=1, row=13, columnspan=2)


        self.add_but = Button(text='Zapisz w bazie', command=self.save_settings)
        self.add_but.grid(column=0, row=14)

        self.delete_but = Button(text='Usuń z bazy', command=self.delete)
        self.delete_but.grid(column=1, row=14)

        self.quit_but = Button(text='Wyjście', command=exit)
        self.quit_but.grid(column=2, row=14)

        # ---------- treeview ----------
        def treeview_sort_column(tv, col, reverse):
            l = [(tv.set(k, col), k) for k in tv.get_children('')]
            l.sort(reverse=reverse)

            # rearrange items in sorted positions
            for index, (val, k) in enumerate(l):
                tv.move(k, '', index)

            # reverse sort next time
            tv.heading(col, command=lambda: \
                treeview_sort_column(tv, col, not reverse))

        columns =('Nr. gaśnicy', 'UDT', 'Nr. Zbiornika', 'Typ gaśnicy', 'Pojemność',
                    'Środek', 'Rejon', 'lokalizacja', 'data kontroli', 'Osoba kontrolująca')

        self.tree = ttk.Treeview(height=35, selectmode='browse', columns=columns, show='headings')
        for col in columns:
            self.tree.heading(col, text=col, command=lambda _col=col: \
                treeview_sort_column(self.tree, _col, False))

        self.tree.grid(column=3, row=0, rowspan=30)
        self.tree.heading('#0', text='Index', anchor=W)
        self.tree.heading('Nr. gaśnicy', text='Nr. gaśnicy', anchor=W)
        self.tree.heading('UDT', text='UDT', anchor=W)
        self.tree.heading('Nr. Zbiornika', text='Nr. Zbiornika', anchor=W)
        self.tree.heading('Typ gaśnicy', text='Typ gaśnicy', anchor=W)
        self.tree.heading('Pojemność', text='Pojemność', anchor=W)
        self.tree.heading('Środek', text='Środek', anchor=W)
        self.tree.heading('Rejon', text='Rejon', anchor=W)
        self.tree.heading('lokalizacja', text='lokalizacja', anchor=W)
        self.tree.heading('data kontroli', text='data kontroli', anchor=W)
        self.tree.heading('Osoba kontrolująca', text='Osoba kontrolująca', anchor=W)

        self.tree.column('#0', stretch=tk.NO, width=50)
        self.tree.column('Nr. gaśnicy', stretch=tk.NO, width=70)
        self.tree.column('UDT', stretch=tk.NO, width=60)
        self.tree.column('Nr. Zbiornika', stretch=tk.NO, width=90)
        self.tree.column('Typ gaśnicy', stretch=tk.NO, width=70)
        self.tree.column('Pojemność', stretch=tk.NO, width=70)
        self.tree.column('Środek', stretch=tk.NO, width=70)
        self.tree.column('Rejon', stretch=tk.NO, width=70)
        self.tree.column('lokalizacja', stretch=tk.YES, minwidth=50, width=250)
        self.tree.column('data kontroli', stretch=tk.NO, width=150)
        self.tree.column('Osoba kontrolująca', stretch=tk.NO, width=150, anchor=CENTER)


    def exit():
        destroy()

