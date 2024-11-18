import tkinter as tk

class TitleMenuBar:
    def __init__(self, canvas:tk.Canvas, root_width, root_height):
        self.canvas = canvas
        self.root_width = root_width
        self.root_height = root_height

        bg_width = 400
        bg_height = 600

        self.canvas.create_rectangle(self.root_width / 2 - bg_width / 2, self.root_height / 2 + bg_height / 2, self.root_width / 2 + bg_width / 2, self.root_height / 2 - bg_height / 2, fill="gray")

        self.canvas.cre
        