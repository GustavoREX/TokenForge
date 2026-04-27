import os
import sys
import math
import tkinter as tk
from tkinter import filedialog, colorchooser
from PIL import Image, ImageTk, ImageOps, ImageDraw
from rembg import remove
import ttkbootstrap as tb
from ttkbootstrap.constants import *

try:
    from tkinterdnd2 import DND_FILES, TkinterDnD
    DND_OK = True
except Exception:
    DND_OK = False

APP_TITLE = 'TokenForge'
def resource_path(relative):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(os.path.abspath('.'), relative)

BORDER_DIR = resource_path('borders')
USER_BORDER_DIR = os.path.join(os.path.abspath('.'), 'borders')
PREVIEW_SIZE = 320
EXPORT_SIZE = 512

class TokenForge(TkinterDnD.Tk):
    def __init__(self):
        super().__init__()
        self.style = tb.Style('flatly')
        self.title(APP_TITLE)
        self.geometry('980x700')
        self.minsize(920, 640)

        self.source_img = None
        self.current_path = None
        self.border_img = None
        self.preview_tk = None
        self.bg_mode = tk.StringVar(value='transparent')
        self.bg_color = '#ffffff'
        self.size_var = tk.IntVar(value=512)
        self.border_choice = tk.StringVar(value='(none)')
        self.img_zoom = tk.DoubleVar(value=1.0)
        self.border_zoom = tk.DoubleVar(value=1.0)
        self.crop_scale = tk.DoubleVar(value=1.0)
        self.offset_x = 0
        self.offset_y = 0
        self.drag_start = None

        self._build_ui()
        self.load_borders()

    def _build_ui(self):
        top = tb.Frame(self, padding=10)
        top.pack(fill=X)

        tb.Button(top, text='Selecionar Imagem', bootstyle=PRIMARY, command=self.open_image).pack(side=LEFT, padx=4)
        tb.Button(top, text='Salvar Token', bootstyle=SUCCESS, command=self.save_token).pack(side=LEFT, padx=4)
        tb.Button(top, text='Escolher Cor Fundo', bootstyle=INFO, command=self.pick_color).pack(side=LEFT, padx=4)
        tb.Button(top, text='Auto Remove Fundo', bootstyle=WARNING, command=self.auto_remove_bg).pack(side=LEFT, padx=4)

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
        self.canvas.create_text(160, 160, text='Arraste uma imagem aqui\nou clique em Selecionar', font=('Segoe UI', 14), fill='#666')

        right = tb.Labelframe(body, text='Opções', padding=10)
        right.pack(side=RIGHT, fill=Y)

        tb.Label(right, text='Borda').pack(anchor=W)
        self.border_combo = tb.Combobox(right, textvariable=self.border_choice, state='readonly', width=24)
        self.border_combo.pack(fill=X, pady=(0,10))
        self.border_combo.bind('<<ComboboxSelected>>', lambda e: self.apply_border())

        tb.Label(right, text='Fundo').pack(anchor=W)
        for mode, txt in [('transparent','Transparente'), ('solid','Cor sólida')]:
            tb.Radiobutton(right, text=txt, variable=self.bg_mode, value=mode, command=self.refresh_preview).pack(anchor=W)

        tb.Label(right, text='Zoom Imagem').pack(anchor=W, pady=(10,0))
        tb.Scale(right, from_=0.5, to=2.5, variable=self.img_zoom, orient=HORIZONTAL, command=lambda e: self.refresh_preview()).pack(fill=X)

        tb.Label(right, text='Zoom Borda').pack(anchor=W, pady=(10,0))
        tb.Scale(right, from_=0.5, to=2.0, variable=self.border_zoom, orient=HORIZONTAL, command=lambda e: self.refresh_preview()).pack(fill=X)

        tb.Label(right, text='Área de Corte').pack(anchor=W, pady=(10,0))
        tb.Scale(right, from_=0.5, to=1.3, variable=self.crop_scale, orient=HORIZONTAL, command=lambda e: self.refresh_preview()).pack(fill=X)

        tb.Label(right, text='Tamanho exportação').pack(anchor=W, pady=(10,0))
        tb.Spinbox(right, from_=128, to=2048, increment=64, textvariable=self.size_var, width=10, command=self.refresh_preview).pack(anchor=W)

        if DND_OK:
            try:
                self.drop_target_register(DND_FILES)
                self.dnd_bind('<<Drop>>', self.on_drop)
            except Exception:
                pass

    def load_borders(self):
        os.makedirs(USER_BORDER_DIR, exist_ok=True)
        files = ['(none)']
        found = set()
        for folder in [BORDER_DIR, USER_BORDER_DIR]:
            if os.path.exists(folder):
                for f in os.listdir(folder):
                    if f.lower().endswith(('.png','.webp')) and f not in found:
                        files.append(f)
                        found.add(f)
        self.border_combo['values'] = files
        self.border_combo.current(0)

    def open_image(self):
        path = filedialog.askopenfilename(filetypes=[('Images','*.png;*.jpg;*.jpeg;*.webp')])
        if path:
            self.load_image(path)

    def on_drop(self, event):
        path = event.data.strip().strip('{').strip('}')
        if os.path.isfile(path):
            self.load_image(path)

    def load_image(self, path):
        self.current_path = path
        self.source_img = Image.open(path).convert('RGBA')
        self.refresh_preview()

    def apply_border(self):
        choice = self.border_choice.get()
        if choice == '(none)':
            self.border_img = None
        else:
            for folder in [USER_BORDER_DIR, BORDER_DIR]:
                p = os.path.join(folder, choice)
                if os.path.exists(p):
                    self.border_img = Image.open(p).convert('RGBA')
                    break
        self.refresh_preview()

    def auto_remove_bg(self):
        if not self.source_img:
            return
        self.source_img = remove(self.source_img)
        self.refresh_preview()

    def pick_color(self):
        c = colorchooser.askcolor()[1]
        if c:
            self.bg_color = c
            self.refresh_preview()

    def make_token(self, size):
        img = self.source_img.copy()
        zoom = self.img_zoom.get()
        img.thumbnail((size*1.4*zoom, size*1.4*zoom), Image.Resampling.LANCZOS)
        layer = Image.new('RGBA', (size, size), (0,0,0,0))
        px = int((size - img.width)/2 + self.offset_x * (size/PREVIEW_SIZE))
        py = int((size - img.height)/2 + self.offset_y * (size/PREVIEW_SIZE))
        layer.paste(img, (px, py), img)
        img = layer

        mask = Image.new('L', (size, size), 0)
        draw = ImageDraw.Draw(mask)
        cs = self.crop_scale.get()
        margin = int((size - size*cs)/2)
        draw.ellipse((margin, margin, size-margin, size-margin), fill=255)

        base = Image.new('RGBA', (size, size), (0,0,0,0))
        if self.bg_mode.get() == 'solid':
            rgb = tuple(int(self.bg_color[i:i+2],16) for i in (1,3,5))
            base = Image.new('RGBA', (size,size), rgb + (255,))

        base.paste(img, (0,0), mask)

        if self.border_img:
            bz = self.border_zoom.get()
            bsize = int(size * bz)
            border = self.border_img.resize((bsize,bsize), Image.Resampling.LANCZOS)
            temp = Image.new('RGBA', (size,size), (0,0,0,0))
            bp = ((size-bsize)//2, (size-bsize)//2)
            temp.paste(border, bp, border)
            border = temp
            base.alpha_composite(border)

        return base

    def refresh_preview(self):
        if not self.source_img:
            return
        img = self.make_token(PREVIEW_SIZE)
        self.preview_tk = ImageTk.PhotoImage(img)
        self.canvas.delete('all')
        w = self.canvas.winfo_width()
        h = self.canvas.winfo_height()
        r = PREVIEW_SIZE // 2
        self.canvas.create_oval(w//2-r-4, h//2-r-4, w//2+r+4, h//2+r+4, fill='', outline='#d0d0d0', width=2)
        self.canvas.create_image(w//2, h//2, image=self.preview_tk)

    def start_drag(self, event):
        self.drag_start = (event.x, event.y)

    def do_drag(self, event):
        if not self.drag_start or not self.source_img:
            return
        dx = event.x - self.drag_start[0]
        dy = event.y - self.drag_start[1]
        self.offset_x += dx
        self.offset_y += dy
        self.drag_start = (event.x, event.y)
        self.refresh_preview()

    def stop_drag(self, event):
        self.drag_start = None

    def save_token(self):
        if not self.source_img:
            return
        size = self.size_var.get()
        img = self.make_token(size)
        base = 'token'
        initialdir = os.path.abspath('.')
        if self.current_path:
            base = os.path.splitext(os.path.basename(self.current_path))[0] + '_token'
            initialdir = os.path.dirname(self.current_path)
        path = filedialog.asksaveasfilename(initialfile=base + '.png', initialdir=initialdir, defaultextension='.png', filetypes=[('PNG','*.png')])
        if path:
            img.save(path)

if __name__ == '__main__':
    app = TokenForge()
    app.mainloop()
