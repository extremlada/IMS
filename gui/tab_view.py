import customtkinter as ctk
from gui.tree_frame import TreeFrame
from gui.product_management_frame import ProductManagementFrame
from gui.dropdown_buttons import DropdownButtons
from gui.button_frame import ButtonFrame
from gui.Chatroom import Chatapp

class MyTabView(ctk.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.add("raktár")
        self.add("Chatroom")
        self.add("áru kezelés")

        self.tree_frame = TreeFrame(master=self.tab("raktár"))
        self.dropdown_button_frame = DropdownButtons(master=self.tab("raktár"))
        self.button_frame = ButtonFrame(master=self.tab("raktár"), tree_frame=self.tree_frame, dropdown_buttons_instance=self.dropdown_button_frame)

        self.tree_frame.grid(row=0, column=0, pady=10, padx=20)
        self.dropdown_button_frame.grid(row=1, column=0, pady=10, padx=20)
        self.button_frame.grid(row=2, column=0, pady=10, padx=20)

        self.product_management_frame = ProductManagementFrame(master=self.tab("áru kezelés"))
        self.product_management_frame.grid(row=0, column=0, pady=10, padx=20, sticky="nsew")

        self.chat = Chatapp(master=self.tab("Chatroom"))
        self.chat.pack(expand=1)
