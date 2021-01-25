import tkinter as tk


BG_COLOR_ENTRY = '#C5C8CF'


class CustomListbox(tk.Listbox):
    def __init__(self, master):
        super().__init__()
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

    def insert_list(self, lista):
        for index, method in enumerate(lista):
            self.listbox.insert(index, method)

    def delete_all_items(self):  
        self.listbox.delete(0, tk.END)

    def has_items(self):
        if self.listbox.size():
            return True
        return False

    def delete_first_item(self):
        self.listbox.delete(0, 0)

    def get_all_items(self):
        return list(self.listbox.get(0, tk.END))
