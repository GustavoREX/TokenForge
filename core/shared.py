import os
from tkinter import filedialog, colorchooser, messagebox
from rembg import remove
from PIL import Image
import traceback
from PIL import Image, ImageTk, ImageOps, ImageDraw

try:
    from tkinterdnd2 import DND_FILES
    DND_OK = True
except:
    DND_OK = False


def enable_dragdrop(widget, callback):
    if not DND_OK:
        return

    try:
        widget.drop_target_register(DND_FILES)
        widget.dnd_bind("<<Drop>>", callback)
    except Exception:
        messagebox.showerror("DnD Error", traceback.format_exc())


def open_image(obj):
    path = filedialog.askopenfilename(
        filetypes=[("Images", "*.png;*.jpg;*.jpeg;*.webp")]
    )
    if path:
        load_image(obj, path)


def on_drop(obj, event):
    try:
        path = obj.tk.splitlist(event.data)[0]
        if os.path.isfile(path):
            load_image(obj, path)
    except Exception:
        messagebox.showerror("Drop Error", traceback.format_exc())


def load_image(obj, path):
    obj.current_path = path
    obj.source_img = Image.open(path).convert("RGBA")
    obj.refresh_preview()


def auto_remove_bg(obj):
    if getattr(obj, "source_img", None):
        obj.source_img = remove(obj.source_img)
        obj.refresh_preview()


def pick_color(obj):
    c = colorchooser.askcolor()[1]
    if c:
        obj.bg_color = c
        obj.refresh_preview()


def save_image(obj, img, mode_id=1):
    base = "image"
    initialdir = os.path.abspath(".")

    if getattr(obj, "current_path", None):
        name = os.path.splitext(
            os.path.basename(obj.current_path)
        )[0]

    if mode_id == 1:
        base = name + "_token"
    else:
        base = name + "_edited"

    initialdir = os.path.dirname(obj.current_path)

    path = filedialog.asksaveasfilename(
        initialfile=base + ".png",
        initialdir=initialdir,
        defaultextension=".png",
        filetypes=[("PNG", "*.png")]
    )

    if path:
        img.save(path)