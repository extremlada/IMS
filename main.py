import customtkinter
from MySQL import *
from income_calculation import *
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)

mydb = connection_mysql()

calculate_income(mydb)
calculate_spend(mydb)
calculate_net_income(mydb)

def income():
    mydb = connection_mysql()
    print("Total Income:", calculate_income(mydb))
    print("Total Spend:", calculate_spend(mydb))
    print("Net Income:", calculate_net_income(mydb))
    mydb.close()

def check_for_normal_state(dropdown_buttons_instance):
    if dropdown_buttons_instance.dropdown_button.cget("state") == "normal":
        return True


def display_data(tree_frame, dropdown_buttons_instance):
    if check_for_normal_state(dropdown_buttons_instance):
        choice=dropdown_buttons_instance.dropdown_button.get()
        mydb = connection_mysql()
        print(choice)
        data = orders_by_date(mydb, [choice])

        for item in tree_frame.tree.get_children():
            tree_frame.tree.delete(item)

        for row in data:
            tree_frame.tree.insert("", "end", values=row)
        mydb.close()
    else:
        # Perform normal display data operation
        mydb = connection_mysql()
        data = Get_data_orders(mydb)

        for item in tree_frame.tree.get_children():
            tree_frame.tree.delete(item)

        for row in data:
            tree_frame.tree.insert("", "end", values=row)
        mydb.close()

def dropdown_options_date():
    mydb = connection_mysql()
    data = Get_orders_date(mydb)
    options = [str(row[0]) for row in data]
    return options
    mydb.close()

def radio_button_pressed(dropdown_buttons_instance):
    if dropdown_buttons_instance.radio_var.get() == "on":
        dropdown_buttons_instance.dropdown_button.configure(state="normal")
        dropdown_buttons_instance.dropdown_button_suppliers.configure(state="normal")
    else:
        dropdown_buttons_instance.dropdown_button.configure(state="disabled")
        dropdown_buttons_instance.dropdown_button_suppliers.configure(state="disabled")
def dropdown_options_company():
    mydb = connection_mysql()
    data = Get_suppliers_info(mydb)
    options = [str(row[0]) for row in data]
    return options
    mydb.close()


def tabs():
    tabs = ctk.CTkTabview()
    tabs.pack(pady=10)
    raktar_tab = tabs.add(name="raktár")


class LoginWindow(ctk.CTk):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Login")
        self.geometry("300x200")

        self.username_entry = ctk.CTkEntry(self, )
        self.username_entry.pack(pady=10)

        self.password_entry = ctk.CTkEntry(self, show="*")
        self.password_entry.pack(pady=10)

        self.login_button = ctk.CTkButton(self, text="Login", command=self.login)
        self.login_button.pack(pady=10)

    def login(self):
        # Add your login logic here
        # For simplicity, let's just check if the username and password are "admin"
        mydb = connection_mysql()
        username = self.username_entry.get()
        password = self.password_entry.get()
        if login(mydb, username, password):
            # If login is successful, open the main application window
            mydb.close()
            self.destroy()
            app = App()
            app.mainloop()


class MyTabView(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # create tabs
        self.add("raktár")
        self.add("pénzügy")
        self.add("tab 3")

        class tree_Frame(ctk.CTkFrame):
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



        class dropdown_buttons(ctk.CTkFrame):
            def __init__(self, master, **kwargs):
                super().__init__(master, **kwargs)

                self.dropdown_button = ctk.CTkOptionMenu(self, state="disabled", values=dropdown_options_date(),
                                                         command=lambda choice: choice)
                self.dropdown_button.grid(row=1, column=1, pady=5, padx=10)
                self.dropdown_button_suppliers = ctk.CTkOptionMenu(self, state="disabled", values=dropdown_options_company())
                self.dropdown_button_suppliers.grid(row=1, column=0, pady=5, padx=10)
                self.radio_var = ctk.StringVar(value="on")
                self.radio_button = ctk.CTkCheckBox(self, text="press for query", offvalue="off", onvalue="on",
                                                    variable=self.radio_var, command=lambda: radio_button_pressed(self))
                self.radio_button.grid(row=1, column=3, pady=5, padx=10)


        class button_frame1(ctk.CTkFrame):
            def __init__(self, master, tree_frame, dropdown_buttons_instance, **kwargs):
                super().__init__(master, **kwargs)

                button1 = ctk.CTkButton(self, text="Display data", command=lambda: display_data(tree_frame, dropdown_buttons_instance))
                button1.grid(row=1, column=1, pady=5, padx=10)
                button2 = ctk.CTkButton(self, text="Income calculation", command=lambda: income())
                button2.grid(row=1, column=2, pady=5, padx=10)
                income_label = ctk.CTkLabel(self, text=calculate_income(mydb), bg_color="#9097E1", )
                income_label.grid(row=2, column=1, pady=5, padx=10)


        self.idk = tree_Frame(master=self.tab("raktár"))
        self.idk.grid(row=0, column=0, pady=10, padx=20)
        self.dropdown_button_fram = dropdown_buttons(master=self.tab("raktár"))
        self.dropdown_button_fram.grid(row=1, column=0, pady=10, padx=20)
        self.button_fram = button_frame1(master=self.tab("raktár"), tree_frame=self.idk,
                                         dropdown_buttons_instance=self.dropdown_button_fram)
        self.button_fram.grid(row=2, column=0, pady=10, padx=20)




class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)


        self.tab_view = MyTabView(master=self)
        self.tab_view.grid(row=0, column=0, padx=10, pady=10)

        #self.buttonchangeframe = change_frame_button(master=self)
        #self.buttonchangeframe.grid(row=1, column=0, padx=0, pady=5, sticky='nsew', rowspan=3)
#
        #self.dropdown_buttonsframe = dropdown_buttons(master=self)
        #self.dropdown_buttonsframe.grid(row=2, column=1, padx=20, pady=5, sticky='nsew')
#
        #self.buttonframe = button_frame1(master=self, tree_frame=self.my_frame, dropdown_buttons_instance=self.dropdown_buttonsframe)
        #self.buttonframe.grid(row=3, column=1, padx=20, pady=5, sticky='nsew')




if __name__ == "__main__":
    login_window = LoginWindow(None)
    login_window.mainloop()
