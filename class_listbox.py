import tkinter as tk


BG_COLOR_ENTRY = '#C5C8CF'


class CustomListbox():
    def __init__(self, master):
        self.master = master

    def with_vertical_scroll(self):
        self.listbox = tk.Listbox(self.master,
                                  height=20,
                                  width=18,
                                  borderwidth=6,
                                  relief=tk.SUNKEN,
                                  bg=BG_COLOR_ENTRY)

        self.scrollbar = tk.Scrollbar(self.master)
        self.scrollbar.configure(command=self.listbox.yview)
        self.listbox.configure(yscrollcommand=self.scrollbar.set)
        self.listbox.grid(column=0, row=0)
        self.scrollbar.grid(column=1, row=0, sticky=tk.W+tk.E+tk.N+tk.S)
