import tkinter as tk
from src import utils

root = tk.Tk()
root.geometry("1000x1000")
canvas = tk.Canvas(root, width=1000, height=1000)
canvas.pack()
b1 = utils.CanvasButton(canvas, 0, 0, 200, 200, fill="img", onclick=lambda:print("ok"), path=r"dog.jpg")
root.mainloop()