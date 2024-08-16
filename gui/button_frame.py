import customtkinter as ctk
from income_calculation import calculate_income
from MySQL import connection_mysql, Get_data_orders

def income():
    mydatab = connection_mysql()
    print("Total Income:", calculate_income(mydatab))
    mydatab.close()

def radio_button_pressed(dropdown_buttons_instance):
    if dropdown_buttons_instance.radio_var.get() == "on":
        dropdown_buttons_instance.dropdown_button.configure(state="normal")
        dropdown_buttons_instance.dropdown_button_suppliers.configure(state="normal")
    else:
        dropdown_buttons_instance.dropdown_button.configure(state="disabled")
        dropdown_buttons_instance.dropdown_button_suppliers.configure(state="disabled")

class ButtonFrame(ctk.CTkFrame):
    def __init__(self, master, tree_frame, dropdown_buttons_instance, **kwargs):
        super().__init__(master, **kwargs)
        self.tree_frame = tree_frame
        self.dropdown_buttons_instance = dropdown_buttons_instance

        button1 = ctk.CTkButton(self, text="Display data", command=self.display_data)
        button1.grid(row=1, column=1, pady=5, padx=10)

        button2 = ctk.CTkButton(self, text="Income calculation", command=income)
        button2.grid(row=1, column=2, pady=5, padx=10)

        income_label = ctk.CTkLabel(self, text="Total Income: ", bg_color="#9097E1")
        income_label.grid(row=2, column=1, pady=5, padx=10)

    def display_data(self):
        mydatab = connection_mysql()
        data = Get_data_orders(mydatab)
        self.tree_frame.display_data(data)
        mydatab.close()
