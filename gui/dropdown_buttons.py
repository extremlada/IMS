import customtkinter as ctk
from MySQL import connection_mysql, Get_orders_date, Get_suppliers_info

def dropdown_options_date():
    mydatab = connection_mysql()
    data = Get_orders_date(mydatab)
    options = [str(row[0]) for row in data]
    return options

def dropdown_options_company():
    mydatab = connection_mysql()
    data = Get_suppliers_info(mydatab)
    options = [str(row[0]) for row in data]
    return options
def radio_button_pressed(dropdown_buttons_instance):
    if dropdown_buttons_instance.radio_var.get() == "on":
        dropdown_buttons_instance.dropdown_button.configure(state="normal")
        dropdown_buttons_instance.dropdown_button_suppliers.configure(state="normal")
    else:
        dropdown_buttons_instance.dropdown_button.configure(state="disabled")
        dropdown_buttons_instance.dropdown_button_suppliers.configure(state="disabled")

class DropdownButtons(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.dropdown_button = ctk.CTkOptionMenu(self, state="disabled", values=dropdown_options_date())
        self.dropdown_button.grid(row=1, column=1, pady=5, padx=10)
        self.dropdown_button_suppliers = ctk.CTkOptionMenu(self, state="disabled", values=dropdown_options_company())
        self.dropdown_button_suppliers.grid(row=1, column=0, pady=5, padx=10)
        self.radio_var = ctk.StringVar(value="on")
        self.radio_button = ctk.CTkCheckBox(self, text="press for query", offvalue="off", onvalue="on", variable=self.radio_var, command=lambda: radio_button_pressed(self))
        self.radio_button.grid(row=1, column=3, pady=5, padx=10)
