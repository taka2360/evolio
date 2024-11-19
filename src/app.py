import tkinter as tk
import configparser
import logging
import time
import _tkinter

from .titlemenubar import TitleMenuBar

class App:
    def __init__(self) -> None:

        #config読み込み
        self.config = configparser.ConfigParser()
        self.config.read(r"config.ini", encoding="utf-8")

        #logger設定
        std_handler = logging.StreamHandler()
        file_handler = logging.FileHandler("logs.txt", encoding="utf-8")

        handlers = list()
        if self.config.getboolean("Dev", "log_on_console"):
            handlers.append(std_handler)
        if self.config.getboolean("Dev", "log_on_file"):
            handlers.append(file_handler)

        logging.basicConfig(
            format="%(levelname)s [%(asctime)s, in %(name)s] %(message)s",
            level=self.config.get("Dev", "log_level"),
            handlers=handlers,
        )
        self.logger = logging.getLogger(__name__)

        self.MAX_FPS = self.config.getint("Window", "max_fps")
        self.fullscreen = self.config.getboolean("Window", "fullscreen")

        #window設定
        self.root = tk.Tk()
        self.root.configure(bg="black")
        self.root.title("evolio")
        self.window_width = self.root.winfo_screenwidth()
        self.window_height = self.root.winfo_screenheight()
        self.root.geometry(f"{self.window_width}x{self.window_height}")
        
        if self.fullscreen:
            self.root.attributes("-fullscreen", True)

        #メインのキャンバス
        self.canvas = tk.Canvas(
            self.root,
            width=self.window_width,
            height=self.window_height,
            borderwidth=0,
            highlightthickness=0,
            bg="#303030",
        )
        self.canvas.pack()

        #タイトルのメニューバー
        self.titlemenubar = TitleMenuBar(self.canvas, self.window_width, self.window_height)

        self.root.update()
    
    def update(self):
        return self.root.update()
    
    def mainloop(self):
        
        while True:
            try:
                self.update()
            except _tkinter.TclError:
                self.logger.info("ウィンドウが閉じられました")
                break
            time.sleep(1 / self.MAX_FPS)
