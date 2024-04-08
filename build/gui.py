from MySQL import *
from pathlib import Path
from tkinter import *
from main import *
mydb = connection_mysql()
import customtkinter


root = customtkinter.CTk()
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

def date_picking():
    output_label.configure(text=Dates_combo.get())
def Date_picker(choice):
    output_label.configure(text=choice)

button1 = customtkinter.CTkButton(root, text="raktár")
button1.pack(pady=10)

Date_label = customtkinter.CTkLabel(root, text="pick a date")
Date_label.pack(pady=40)

Dates = ["2002", "2012", "2022"]
Dates_combo = customtkinter.CTkComboBox(root, values=Dates)
Dates_combo.pack(pady=50)

button_sender = customtkinter.CTkButton(root, text="select a date", command=date_picking)
button_sender.pack(pady=30)
#output label
output_label = customtkinter.CTkLabel(root, text="")
output_label.pack(pady=20)

root.mainloop()

