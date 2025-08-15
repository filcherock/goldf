import os

from tkinter import *
from customtkinter import *

catalog = os.getcwd()

app = Tk()

def __init__():
    app.title(f"goldf: {catalog}")
    app.geometry("1200x700")

if __name__ == '__main__':
    __init__()
    app.mainloop()