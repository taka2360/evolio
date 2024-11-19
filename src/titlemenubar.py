import tkinter as tk
from .utils import *

class TitleMenuBar:
    def __init__(self, canvas:tk.Canvas, root_width, root_height):
        self.canvas = canvas
        self.root_width = root_width
        self.root_height = root_height

        bg_width = 400
        bg_height = 600

        self.canvas.create_rectangle(self.root_width / 2 - bg_width / 2, self.root_height / 2 + bg_height / 2, self.root_width / 2 + bg_width / 2, self.root_height / 2 - bg_height / 2, fill="gray")

        button_width = 300
        button_height = 180

        self.newgamebutton = CanvasButton(self.canvas, self.root_width / 2 - button_width / 2, self.root_height / 2 + button_height / 2, button_width, button_height, "black", lambda:print("Ok"))
        