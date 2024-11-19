import tkinter as tk
from PIL import Image, ImageTk

class Widget:
    def __init__(self, canvas:tk.Canvas):
        self.canvas = canvas
        self.element = None

    def delete(self):
        return self.canvas.delete(self.element)


class CanvasButton(Widget):
    def __init__(self, canvas:tk.Canvas, x, y, width, height, fill, onclick:int, **kwargs) -> int:
        """tkinter.Canvasにボタンをかけるようにする
            options:
                path - fill="img"を指定した時のファイルパス
                anchor - どこを基準にして表示するか tkinter.NWなどで指定
        """

        super().__init__(canvas)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.fill = fill
        self.onclick = onclick

        if fill == "img":
            #画像のとき
            self.imagepath = kwargs["path"]
            image = Image.open(self.imagepath)
            image = keepAspectResize(image, self.width, self.height)
            self.image = ImageTk.PhotoImage(image)
            self.widget = self.canvas.create_image(self.x + self.width / 2, self.y + self.height / 2, image=self.image)
        else:
            #図形のとき
            self.element = self.canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, fill = self.fill)

        canvas.bind("<Button-1>", self._check)

    def _check(self, event):
        #マウスが触れているか調べる
        if self.x < event.x < self.x + self.width and self.y < event.y < self.y + self.height:
            self.onclick()

def keepAspectResize(image:Image, width, height) -> Image:
    """アスペクト比を維持してリサイズ"""

    ratio = min(width / image.width, height / image.height)
    resize_size = (round(ratio * image.width), round(ratio * image.height))
    resized_image = image.resize(resize_size)

    return resized_image
