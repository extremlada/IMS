import tkinter as tk
import customtkinter as ctk
import socket
import threading
import os
import sys

class Send(threading.Thread):
    def __init__(self, sock, name):
        super().__init__()
        self.sock = sock
        self.name = name

    def run(self):
        while True:
            print(f'{self.name}: ', end='')
            sys.stdout.flush()
            message = sys.stdin.readline()[:-1]

            if message == "Quit":
                self.sock.sendall(f'Server: {self.name} has left the chat'.encode('UTF-8'))
                break
            else:
                self.sock.sendall(f'{self.name}: {message}'.encode('UTF-8'))

        print('\nQuitting...')
        self.sock.close()
        os._exit(0)

class Receive(threading.Thread):
    def __init__(self, sock, name):
        super().__init__()
        self.sock = sock
        self.name = name
        self.messages = None

    def run(self):
        while True:
            message = self.sock.recv(1024).decode('UTF-8')
            if message:
                if self.messages:
                    self.messages.insert(tk.END, message)
                    print(f'\r{message}\n{self.name}: ', end='')
                else:
                    print(f'\r{message}\n{self.name}: ', end='')
            else:
                print('\nNo. We have lost connection to the server!')
                print('\nQuitting...')
                self.sock.close()
                os._exit(0)

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.name = None
        self.messages = None

    def start(self, name):
        self.name = name
        print(f'Trying to connect to {self.host}:{self.port}...')
        self.sock.connect((self.host, self.port))
        print(f'Successfully connected to {self.host}:{self.port}')

        print(f'Welcome, {self.name}! Getting ready to send and receive messages...')

        send = Send(self.sock, self.name)
        receive = Receive(self.sock, self.name)

        send.start()
        receive.start()

        self.sock.sendall(f'Server: {self.name} has joined the chat. Say hi'.encode('UTF-8'))
        print("\rReady! Leave the chatroom anytime by typing 'Quit'\n")
        print(f'{self.name}: ', end='')

        return receive

    def send(self, textInput):
        message = textInput.get()
        textInput.delete(0, tk.END)
        self.messages.insert(tk.END, f'{self.name}: {message}')

        if message == "Quit":
            self.sock.sendall(f'Server: {self.name} has left the chat'.encode('UTF-8'))
            print('\nQuitting...')
            self.sock.close()
            os._exit(0)
        else:
            self.sock.sendall(f'{self.name}: {message}'.encode('UTF-8'))


class Chatapp(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

    def functionality(self, port, host, name):
        client = Client(host, port)
        receive = client.start(name)

        # Configure grid layout for parent frame
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)

        # Messages listbox with scrollbar
        self.messages = ctk.CTkTextbox(self, wrap="word", width=800, height=500)

        self.messages.grid(row=0, column=0, columnspan=10, rowspan=10,  sticky="nsew")

        # Text input for messages
        self.textInput = ctk.CTkEntry(self)
        self.textInput.bind("<Return>", command=lambda x: client.send(self.textInput))
        self.textInput.insert(0, "Type your message here")
        self.textInput.grid(row=1, column=0, sticky="ew", pady=10, padx=(10, 2))

        client.messages = self.messages
        receive.messages = self.messages

        # Send button
        self.btnSend = ctk.CTkButton(self, text="Send", command=lambda: client.send(self.textInput))
        self.btnSend.grid(row=1, column=1, sticky="ew", pady=10, padx=(2, 10))
