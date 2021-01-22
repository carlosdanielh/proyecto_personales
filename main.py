import tkinter as tk
from tkinter import messagebox as msg
from class_window import Window
from class_label import CustomLabel
from class_button import Buttons
from class_listbox import CustomListbox
from class_text import CustomText
from remenber_method import *
import random


# ---------------------------------click seek---------------------------------#
def click_seek():
    global structure
    estructura_aleatoria = random.choice(list(structure.keys()))
    label_method.set_text(estructura_aleatoria)
    fill_listbox(estructura_aleatoria)
    button_method.disable_button()
    msg.showinfo('Info', 'Remenber you must exercise each method in the list,'
                 'once you save each of them you\'r done. Good luck!')


# ---------------------------------fill list----------------------------------#
def fill_listbox(selection):
    list_all_structure_values = structure[selection]
    set_method = set()
    set_is_full = False
    while not set_is_full:
        method = random.choice(list_all_structure_values)
        set_method.add(method)
        if len(set_method) == 5:
            set_is_full = True
    list_box.delete_all_items()
    list_box.insert_list(set_method)

    if list_box.has_items():
        button_save.enable_button()


# ---------------------------------save button--------------------------------#
def save():
    if text_box.is_empty():
        msg.showinfo('Info', 'You can\'t save an empty textbox')
    else:
        answer = msg.askyesno('Sure?', 'Are you sure you want to save this'
                              'data?')
        if answer:
            if list_box.has_items():
                list_box.delete_first_item()
                text_box.clear_texbox()
                if not list_box.has_items():
                    button_save.disable_button()
                    msg.showinfo('Info', 'Congratulations you\'ve finished the'
                                 'job for today, see you tomorrow...')


# ----------------------------------constant----------------------------------#
FONT_TITLE = ('Open Sans', 20, 'bold')
BG_COLOR_ENTRY = '#C5C8CF'


# --------------------------------- window -----------------------------------#
window = Window(840, 600)
window.title('today\'s study..')
# --------------------------------frames--------------------------------------#
frame_top = tk.Frame(window, pady=15)
frame_top.pack()

frame_middle_top = tk.Frame(window)
frame_middle_top.pack()

frame_left = tk.Frame(window, width=200, height=300, bg='lightblue')
frame_left.pack(side=tk.LEFT, padx=18)

# frame_right = tk.Frame(window, width=500, height=300, bg='blue')
# frame_right.pack(side=tk.RIGHT, padx=20)

frame_bottom = tk.Frame(window, width=500, height=40, bg='red')
frame_bottom.pack(side=tk.BOTTOM, pady=5)

# --------------------------------Label---------------------------------------#
label_title = CustomLabel(frame_top)
label_title.big_title('IT\'S TIME TO STUDY')

label_method = CustomLabel(frame_middle_top)
label_method.middle_label('METHOD')
# --------------------------------Buttons-------------------------------------#
button_method = Buttons(frame_middle_top)
button_method.create_large_button('seek random', click_seek)

button_save = Buttons(frame_left)
button_save.create_medium_button('save', save)
button_save.disable_button()


list_box = CustomListbox(frame_left)
list_box.with_vertical_scroll()
# --------------------------------Textbox-------------------------------------#
text_box = CustomText(frame_left)
text_box.With_vertical_scroll()

window.resizable(False, False)
window.mainloop()
