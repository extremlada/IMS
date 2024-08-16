import customtkinter as ctk
from gui.tab_view import MyTabView

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Application")
        self.geometry("1100x600")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.tab_view = MyTabView(master=self)
        self.tab_view.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
