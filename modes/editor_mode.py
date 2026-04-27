import ttkbootstrap as tb
from ttkbootstrap.constants import *

class EditorMode(tb.Frame):
    def __init__(self, master):
        super().__init__(master, padding=20)

        tb.Label(self, text='Editor Mode', font=('Segoe UI', 24, 'bold')).pack(pady=20)
        tb.Label(self, text='Em construção...\nÁrea reservada para o futuro editor de imagens.',
                 font=('Segoe UI', 12)).pack()