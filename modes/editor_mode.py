from ast import Lambda
import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from rembg import remove
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from core.shared import *

#try:
#    from tkinterdnd2 import DND_FILES, TkinterDnD
#    DND_OK = True
#except Exception:
#    DND_OK = False
PREVIEW_SIZE = 512

class EditorMode(tb.Frame):
    def __init__(self,master):
        super(). __init__(master, padding=10)

        self.source_img = None
        self.overlay_img = None
        self.preview_tk = None
        self.drag_start = None


        self.bg_mode = tk.StringVar(value='transparent')
        self.bg_color = '#ffffff'
        self.size_var = tk.IntVar(value=512)

        top = tb.Frame(self)
        top.pack(fill=X, pady=5)
        self._build_ui()

    def _build_ui(self):
        top = tb.Frame(self, padding=10)
        top.pack(fill=X)

        tb.Button(top, text='Selecionar Imagem', bootstyle=PRIMARY, command=lambda: open_image(self)).pack(side=LEFT, padx=4)
        tb.Button(top, text='Remover Fundo IA', bootstyle=WARNING, command=lambda: auto_remove_bg(self)).pack(side=LEFT, padx=4)
        tb.Button(top, text='Adicionar Overlay', bootstyle=INFO, command=self.add_overlay).pack(side=LEFT, padx=4)
        tb.Button(top, text='Salvar PNG', bootstyle=SUCCESS, command=self.save_editor).pack(side=LEFT, padx=4)

        body = tb.Frame(self, padding=10)
        body.pack(fill=BOTH, expand=True)

        left = tb.Labelframe(body, text='Preview', padding=10)
        left.pack(side=LEFT, fill=BOTH, expand=True, padx=(0,10))

        self.canvas = tk.Canvas(left, bg='#f5f5f5', highlightthickness=0)
        self.canvas.bind('<Configure>', lambda e: self.refresh_preview())
        self.canvas.bind('<ButtonPress-1>', self.start_drag)
        self.canvas.bind('<B1-Motion>', self.do_drag)
        self.canvas.bind('<ButtonRelease-1>', self.stop_drag)
        self.canvas.pack(fill=BOTH, expand=True)

        enable_dragdrop(self.canvas, lambda e: on_drop(self, e))

        self.canvas.create_text(500, 300, text='     Modo de edição\nSelecione uma imagem', font=('Segoe UI', 18), fill='#666')


    #def open_image(self):
    #    path = filedialog.askopenfilename(filetypes=[('Images','*.png;*.jpg;*.jpeg;*.webp')])
    #    if path:
    #        self.base_img = Image.open(path).convert('RGBA')
    #        #self.refresh_preview()
    #        self.load_image(path)

    #def on_drop(self, event):
    #    path = event.data.strip().strip('{').strip('}')
    #    if os.path.isfile(path):
    #        self.load_image(path)

    #def load_image(self, path):
    #    self.current_path = path
    #    self.source_img = Image.open(path).convert('RGBA')
    #    self.refresh_preview()

    #def remove_bg(self):
    #    if self.base_img:
    #        self.base_img = remove(self.base_img)
    #        self.refresh_preview()

    def add_overlay(self):
        path = filedialog.askopenfilename(filetypes=[('Images','*.png;*.jpg;*.jpeg;*.webp')])
        if path:
            self.overlay_img = Image.open(path).convert('RGBA')
            self.refresh_preview()

    def refresh_preview(self):
    #    if not self.base_img:
        if not self.source_img:
            return
        img = self.source_img.copy()
        img.thumbnail((900, 650))

        if self.overlay_img:
            ov = self.overlay_img.copy()
            ov.thumbnail((300,300))
            img.alpha_composite(ov, (self.ov_x, self.ov_y))

        self.preview_tk = ImageTk.PhotoImage(img)
        self.canvas.delete('all')
        self.canvas.create_image(self.canvas.winfo_width()//2, self.canvas.winfo_height()//2, image=self.preview_tk)

    def start_drag(self, event):
        self.drag_start = (event.x, event.y)

    def do_drag(self, event):
        if not self.drag_start or not self.overlay_img:
             return
        dx = event.x - self.drag_start[0]
        dy = event.y - self.drag_start[1]
        self.ov_x += dx
        self.ov_y += dy
        self.drag_start = (event.x, event.y)
        self.refresh_preview()

    def stop_drag(self, event):
        self.drag_start = None

    def make_image(self, size):
        if not self.source_img:
            return None
    
        img = self.source_img.copy()
    
        if self.bg_mode.get() == "solid":
            rgb = tuple(int(self.bg_color[i:i+2], 16) for i in (1,3,5))
            base = Image.new("RGBA", img.size, rgb + (255,))
            base.alpha_composite(img)
            img = base
    
        if self.overlay_img:
            ov = self.overlay_img.copy()
            img.alpha_composite(ov, (self.ov_x, self.ov_y))
    
        return img

    def save_editor(self):
        if not self.source_img:
            return
        size = self.size_var.get()
        img = self.make_image(size)
        save_image(self, img, 2)
