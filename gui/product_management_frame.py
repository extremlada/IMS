import customtkinter as ctk
import tkinter as tk
from tkinter import ttk

class ProductManagementFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Left side labels and entries
        self.product_id_label = ctk.CTkLabel(self, text="Product ID:")
        self.product_id_entry = ctk.CTkEntry(self)
        self.product_name_label = ctk.CTkLabel(self, text="Product Name:")
        self.product_name_entry = ctk.CTkEntry(self)
        self.product_category_label = ctk.CTkLabel(self, text="Category:")
        self.product_category_entry = ctk.CTkEntry(self)
        self.product_stock_label = ctk.CTkLabel(self, text="Stock:")
        self.product_stock_entry = ctk.CTkEntry(self)

        # Buttons
        self.add_product_button = ctk.CTkButton(self, text="Add Product")
        self.update_product_button = ctk.CTkButton(self, text="Update Product")
        self.delete_product_button = ctk.CTkButton(self, text="Delete Product")

        # Grid layout for labels and entries
        self.product_id_label.grid(row=0, column=0, padx=10, pady=5, sticky='w')
        self.product_id_entry.grid(row=0, column=1, padx=10, pady=5, sticky='w')
        self.product_name_label.grid(row=1, column=0, padx=10, pady=5, sticky='w')
        self.product_name_entry.grid(row=1, column=1, padx=10, pady=5, sticky='w')
        self.product_category_label.grid(row=2, column=0, padx=10, pady=5, sticky='w')
        self.product_category_entry.grid(row=2, column=1, padx=10, pady=5, sticky='w')
        self.product_stock_label.grid(row=3, column=0, padx=10, pady=5, sticky='w')
        self.product_stock_entry.grid(row=3, column=1, padx=10, pady=5, sticky='w')

        self.add_product_button.grid(row=4, column=0, padx=10, pady=5, sticky='w')
        self.update_product_button.grid(row=4, column=1, padx=10, pady=5, sticky='w')
        self.delete_product_button.grid(row=4, column=2, padx=10, pady=5, sticky='w')

        # Treeview for product list on the right side
        self.tree = ttk.Treeview(self, columns=("c1", "c2", "c3", "c4", "c5"), show='headings')
        self.tree.column("#1", anchor=tk.CENTER)
        self.tree.heading("#1", text="product_id")
        self.tree.column("#2", anchor=tk.CENTER)
        self.tree.heading("#2", text="name")
        self.tree.column("#3", anchor=tk.CENTER)
        self.tree.heading("#3", text="description")
        self.tree.column("#4", anchor=tk.CENTER)
        self.tree.heading("#4", text="price")
        self.tree.column("#5", anchor=tk.CENTER)
        self.tree.heading("#5", text="quantity")

        # Place the tree on the right side of the form
        self.tree.grid(row=0, column=3, rowspan=5, pady=5, padx=10, sticky='nsew')

        # Ensure the right side expands properly
        self.grid_columnconfigure(3, weight=1)
        self.grid_rowconfigure(5, weight=1)
