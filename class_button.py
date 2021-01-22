import tkinter as tk
from class_label import CustomLabel

BG_COLOR_BUTTON = '#3C63B8'
FG_COLOR_BUTTON = 'white'
FONT_BUTTON = ('Open Sans', 9, 'bold')


class Buttons(tk.Button):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

    def create_large_button(self, texto, function):
        self.button = tk.Button(self.master,
                                width=25,
                                text=texto,
                                font=FONT_BUTTON,
                                bg=BG_COLOR_BUTTON,
                                fg=FG_COLOR_BUTTON,
                                command=function)
        self.button.pack(pady=5)

    def create_medium_button(self,text,function):
        self.button = tk.Button(self.master,
                                width=6,
                                font=FONT_BUTTON,
                                bg=BG_COLOR_BUTTON,
                                fg=FG_COLOR_BUTTON,
                                command=function,
                                text=text)
        self.button.grid(column=2, row=1, sticky=tk.W)

    def disable_button(self):
        self.button.configure(state=tk.DISABLED)

    def enable_button(self):
        self.button.configure(state=tk.NORMAL)

