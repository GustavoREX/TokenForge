import multiprocessing
import tkinter as tk
from tkinter import ttk
from tkinterdnd2 import TkinterDnD
import ttkbootstrap as tb
from core.paths import ROOT
from core.ui import configure_style
from modes.token_mode import TokenMode
from modes.editor_mode import EditorMode


class App(TkinterDnD.Tk):
    def __init__(self):
        super().__init__()
        self.style = configure_style(self)
        self.title('TokenForge Studio')
        width = min(1280, self.winfo_screenwidth() - 50)
        height = min(880, self.winfo_screenheight() - 90)
        self.geometry(f'{width}x{height}')
        self.minsize(min(600, width), min(620, height))
        try:
            self.iconbitmap(str(ROOT / 'Token.ico'))
        except tk.TclError:
            pass
        header = ttk.Frame(self, padding=(18, 12))
        header.pack(fill='x')
        ttk.Label(header, text='TokenForge', style='Heading.TLabel').pack(side='left')
        ttk.Label(header, text='STUDIO', style='Muted.TLabel').pack(side='left', padx=10)
        navigation = ttk.Frame(self, padding=(18, 0, 18, 10))
        navigation.pack(fill='x')
        self.mode_var = tk.StringVar(value='token')
        for value, label in (('token', 'Token Forge'), ('editor', 'Editor de imagem')):
            tb.Radiobutton(navigation, text=label, value=value, variable=self.mode_var,
                           bootstyle='primary-toolbutton', command=self.show_selected).pack(side='left', padx=(0, 8))
        self.content = ttk.Frame(self, padding=(12, 0, 12, 10))
        self.content.pack(fill='both', expand=True)
        self.modes = {}
        self.current = None
        self.show_selected()

    def show_selected(self):
        self.show(TokenMode if self.mode_var.get() == 'token' else EditorMode)

    def show(self, frame_cls):
        if self.current is not None:
            self.current.pack_forget()
        if frame_cls not in self.modes:
            self.modes[frame_cls] = frame_cls(self.content)
        self.current = self.modes[frame_cls]
        self.current.pack(fill='both', expand=True)
        self.current.refresh_preview()


if __name__ == '__main__':
    multiprocessing.freeze_support()
    import sys
    if len(sys.argv) == 3 and sys.argv[1] == '--self-test':
        from core.diagnostics import run_self_test
        sys.exit(run_self_test(App, sys.argv[2]))
    App().mainloop()
