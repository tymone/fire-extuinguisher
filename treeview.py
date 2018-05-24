#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
import tkinter as tk

class Treeview:
	def treeview(self):
		def treeview_sort_column(tv, col, reverse):#sort onclick head column
			l = [(tv.set(k, col), k) for k in tv.get_children('')]
			try:
				l.sort(key=lambda t: int(t[0]), reverse=reverse)
			except ValueError:
				l.sort(reverse=reverse)

			for index, (val, k) in enumerate(l):
				tv.move(k, '', index)

			tv.heading(col, command=lambda: treeview_sort_column(tv, col, not reverse))

		columns =('Nr. gaśnicy', 'UDT', 'Nr. Zbiornika', 'Typ gaśnicy', 'Pojemność',
					'Środek', 'Rejon', 'lokalizacja', 'Osoba kontrolująca', 'data kontroli')

		self.tree = ttk.Treeview(height=35, selectmode='browse', columns=columns, show='headings')

		for col in columns:
			self.tree.heading(col, text=col, command=lambda _col=col: treeview_sort_column(self.tree, _col, False))

		self.vsb = ttk.Scrollbar(orient="vertical", command=self.tree.yview)
		self.hsb = ttk.Scrollbar(orient="horizontal", command=self.tree.xview)
		self.vsb.grid(sticky=E)
		self.hsb.grid(sticky=S)

		self.tree.configure(yscrollcommand=self.vsb.set)
		self.tree.configure(xscrollcommand=self.hsb.set)

		self.tree.heading('#0', text='Index', anchor=W)
		self.tree.heading('Nr. gaśnicy', text='Nr. gaśnicy', anchor=W)
		self.tree.heading('UDT', text='UDT', anchor=W)
		self.tree.heading('Nr. Zbiornika', text='Nr. Zbiornika', anchor=W)
		self.tree.heading('Typ gaśnicy', text='Typ gaśnicy', anchor=W)
		self.tree.heading('Pojemność', text='Pojemność', anchor=W)
		self.tree.heading('Środek', text='Środek', anchor=W)
		self.tree.heading('Rejon', text='Rejon', anchor=W)
		self.tree.heading('lokalizacja', text='lokalizacja', anchor=W)
		self.tree.heading('Osoba kontrolująca', text='Osoba kontrolująca', anchor=W)
		self.tree.heading('data kontroli', text='data kontroli', anchor=W)

		self.tree.column('#0', stretch=tk.NO, width=50)
		self.tree.column('Nr. gaśnicy', stretch=tk.NO, width=70)
		self.tree.column('UDT', stretch=tk.NO, width=50)
		self.tree.column('Nr. Zbiornika', stretch=tk.NO, width=70)
		self.tree.column('Typ gaśnicy', stretch=tk.NO, width=70)
		self.tree.column('Pojemność', stretch=tk.NO, width=70)
		self.tree.column('Środek', stretch=tk.NO, width=60)
		self.tree.column('Rejon', stretch=tk.NO, width=60)
		self.tree.column('lokalizacja', stretch=tk.YES, minwidth=50, width=230)
		self.tree.column('Osoba kontrolująca', stretch=tk.NO, width=165)
		self.tree.column('data kontroli', stretch=tk.NO, width=85, anchor=CENTER)

		self.tree.grid(column=3, row=0, rowspan=30)

		self.view_records()