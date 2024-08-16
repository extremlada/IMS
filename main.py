from gui.login_window import LoginWindow
import argparse
from gui.tab_view import MyTabView
import customtkinter as ctk


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Application")
        self.geometry("1100x600")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.tab_view = MyTabView(master=self)
        self.tab_view.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

def main(host, port, username):
    app = App()
    tab_view = MyTabView(master=app)
    tab_view.grid(row=0, column=0, sticky="nsew")
    try:
        tab_view.chat.functionality(port, host, username)
        app.mainloop()
    except:
        app.mainloop()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Chatroom Client")
    parser.add_argument('host', nargs='?', default='localhost', help='Interface the client connects to')
    parser.add_argument('-p', metavar='PORT', type=int, default=55555, help='TCP port (default 1060)')
    args = parser.parse_args()

    login_window = LoginWindow(None)
    login_window.mainloop()

    username = login_window.username
    if username:
        main(args.host, args.p, username)
    else:
        print("Login failed or was cancelled.")
