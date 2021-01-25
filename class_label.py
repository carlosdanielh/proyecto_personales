import tkinter as tk


FONT_TITLE = ('Open Sans', 25, 'bold')
FONT_METHOD = ('Open Sans', 16, 'bold')


class CustomLabel(tk.Label):
    def __init__(self, master):
        super().__init__()
        self.master = master

    def big_title(self, texto):
        self.label = tk.Label(self.master,
                              text=texto,
                              borderwidth=2,
                              relief=tk.RAISED,
                              font=FONT_TITLE)
        self.label.pack()

    def middle_label(self, texto):
        self.label = tk.Label(self.master,
                              text=texto,
                              borderwidth=1,
                              relief=tk.SOLID,
                              font=FONT_METHOD,
                              width=16)
        self.label.pack()

    def time_label(self, texto):
        self.label = tk.Label(self.master,
                              text=f'Date : {texto}',
                              borderwidth=1,
                              relief=tk.SOLID,
                              font=FONT_METHOD,
                              width=16)
        self.label.grid(column=2, row=1, sticky=tk.E)

    def set_text(self, text):
        self.label.configure(text=text, width=16)

    def get_text(self):
        return self.label.cget('text')
