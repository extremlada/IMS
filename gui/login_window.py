import customtkinter as ctk
from MySQL import connection_mysql, login

class LoginWindow(ctk.CTk):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Login")
        self.geometry("300x200")

        self.username_entry = ctk.CTkEntry(self, placeholder_text="username")
        self.username_entry.pack(pady=10)

        self.password_entry = ctk.CTkEntry(self, show="*", placeholder_text="password")
        self.password_entry.pack(pady=10)

        self.login_button = ctk.CTkButton(self, text="Login", command=self.login)
        self.login_button.pack(pady=10)

        self.username = None

    def login(self):
        mydatab = connection_mysql()
        username = self.username_entry.get()
        password = self.password_entry.get()
        if login(mydatab, username, password):
            mydatab.close()
            self.username = username
            self.destroy()
