import tkinter as tk


BG_COLOR_ENTRY = '#C5C8CF'


class CustomText():
    def __init__(self, master):
        self.master = master

    def With_vertical_scroll(self):
        self.text_box = tk.Text(self.master,
                                height=20,
                                width=79,
                                borderwidth=6,
                                relief=tk.SUNKEN,
                                bg=BG_COLOR_ENTRY)
        self.scrollbar = tk.Scrollbar(self.master)
        self.scrollbar.configure(command=self.text_box.yview)
        self.text_box.configure(yscrollcommand=self.scrollbar.set)
        self.text_box.grid(column=2, row=0, sticky=tk.W)
        self.scrollbar.grid(column=3, row=0, sticky=tk.N+tk.S)

    def is_empty(self):
        if len(self.text_box.get('1.0', tk.END)) == 1:
            return True
        return False

    def clear_texbox(self):
        self.text_box.delete('0.0', tk.END)
