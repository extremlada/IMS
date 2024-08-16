import customtkinter as ctk
import tkinter as tk
from tkinter import ttk

class TreeFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.tree = ttk.Treeview(self, columns=("c1", "c2", "c3", "c4", "c5"), show='headings')
        self.tree.column("#1", anchor=tk.CENTER)
        self.tree.heading("#1", text="order_id")
        self.tree.column("#2", anchor=tk.CENTER)
        self.tree.heading("#2", text="product_id")
        self.tree.column("#3", anchor=tk.CENTER)
        self.tree.heading("#3", text="supplier_id")
        self.tree.column("#4", anchor=tk.CENTER)
        self.tree.heading("#4", text="quantity")
        self.tree.column("#5", anchor=tk.CENTER)
        self.tree.heading("#5", text="order_date")
        self.tree.grid(row=0, column=1, pady=5, padx=10)

    def display_data(self, data):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for row in data:
            self.tree.insert("", "end", values=row)
