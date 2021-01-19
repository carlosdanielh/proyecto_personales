import tkinter as tk


BG_COLOR_BUTTON = '#3C63B8'
FG_COLOR_BUTTON = 'white'
FONT_BUTTON = ('Open Sans', 9, 'bold')


class Buttons(tk.Button):
    def __init__(self, master):
        super().__init__()
        self.master = master
    
    def randon_button(self, texto):
        self.button = tk.Button(self.master,
                                width=25,
                                text=texto,
                                font=FONT_BUTTON,
                                bg=BG_COLOR_BUTTON,
                                fg=FG_COLOR_BUTTON)
        self.button.pack(pady=5)
