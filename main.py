import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from modes.token_mode import TokenMode
from modes.editor_mode import EditorMode

class App(tb.Window):
    def __init__(self):
        super().__init__(themename='flatly')
        self.title('TokenForge Studio')
        self.geometry('1180x760')
        self.minsize(1000, 700)

        sidebar = tb.Frame(self, padding=10)
        sidebar.pack(side=LEFT, fill=Y)

        content = tb.Frame(self, padding=10)
        content.pack(side=RIGHT, fill=BOTH, expand=True)
        self.content = content

        tb.Button(sidebar, text='Token Forge', bootstyle=PRIMARY, width=18,
                  command=lambda: self.show(TokenMode)).pack(pady=4)
        tb.Button(sidebar, text='Editor', bootstyle=INFO, width=18,
                  command=lambda: self.show(EditorMode)).pack(pady=4)

        self.current = None
        self.show(TokenMode)

    def show(self, frame_cls):
        if self.current:
            self.current.destroy()
        self.current = frame_cls(self.content)
        self.current.pack(fill=BOTH, expand=True)

if __name__ == '__main__':
    app = App()
    app.mainloop()