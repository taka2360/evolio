import tkinter as tk
import math
from PIL import Image, ImageTk, ImageDraw


class Widget:
    def __init__(self, canvas: tk.Canvas):
        self.canvas = canvas
        self.element = None

    def delete(self):
        return self.canvas.delete(self.element)


type


class CanvasButton(Widget):
    """tkinter.Canvasにボタンをかけるようにする

    x, y はpythonのtkinterと同じく左上基準

    :param path: fill="img"の時に参照する画像のパス
    :param button_type: ボタンの形を指定します type="circle"で丸ボタン
    """

    def __init__(
        self,
        canvas: tk.Canvas,
        x,
        y,
        width,
        height,
        fill,
        onclick: int,
        button_type="square",
        text="",
        **kwargs
    ) -> int:

        super().__init__(canvas)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.fill = fill
        self.onclick = onclick
        self.button_type = button_type

        if fill == "img":
            # 画像のとき
            self.imagepath = kwargs["path"]
            image = Image.open(self.imagepath)
            image = keepAspectResize(image, self.width, self.height)

            if self.button_type == "circle":
                # 丸に切り取る
                image = mask_circle(image)

            self.image = ImageTk.PhotoImage(image)
            self.widget = self.canvas.create_image(
                self.x + self.width / 2, self.y + self.height / 2, image=self.image
            )
        else:
            # 図形のとき
            self.element = self.canvas.create_rectangle(
                self.x,
                self.y,
                self.x + self.width,
                self.y + self.height,
                fill=self.fill,
            )

        canvas.bind("<Button-1>", self._check)

    def _check(self, event):
        # マウスが触れているか調べる
        if self.button_type == "circle":
            #丸の時
            if (
                math.sqrt(
                    (self.x + (self.width / 2) - event.x) ** 2
                    + (self.y + (self.width / 2) - event.y) ** 2
                )
                < self.width / 2
            ):
                self.onclick()
        else:
            #四角の時
            if (
                self.x < event.x < self.x + self.width
                and self.y < event.y < self.y + self.height
            ):
                self.onclick()


def keepAspectResize(image: Image, width, height) -> Image:
    """アスペクト比を維持してリサイズ"""

    ratio = min(width / image.width, height / image.height)
    resize_size = (round(ratio * image.width), round(ratio * image.height))
    resized_image = image.resize(resize_size)

    return resized_image


def mask_circle(img):
    """画像を丸く切り取る"""

    mask = Image.new("L", img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, img.size[0], img.size[1]), fill=255)
    result = img.copy()
    result.putalpha(mask)
    return result
