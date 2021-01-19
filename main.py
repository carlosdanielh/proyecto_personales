import tkinter as tk
from class_window import Window
from class_label import Labels
from class_button import Buttons


# ----------------------------------constant----------------------------------#
FONT_TITLE = ('Open Sans', 20, 'bold')

# --------------------------------- window -----------------------------------#
window = Window(800, 600)
window.title('today\'s study..')
# --------------------------------frames--------------------------------------#
frame_top = tk.Frame(window, pady=15)
frame_top.pack()

frame_middle_top = tk.Frame(window)
frame_middle_top.pack()

frame_left = tk.Frame(window, width=200, height=300, bg='lightblue')
frame_left.pack(side=tk.LEFT, padx=20)

frame_right = tk.Frame(window, width=500, height=300, bg='lightblue')
frame_right.pack(side=tk.RIGHT, padx=20)

frame_bottom = tk.Frame(window, width=500, height=40, bg='lightblue')
frame_bottom.pack(side=tk.BOTTOM, pady=5)

# --------------------------------labels--------------------------------------#
label_title = Labels(frame_top)
label_title.big_title('IT\'S TIME TO STUDY')

label_method = Labels(frame_middle_top)
label_method.middle_label('METHOD')

# --------------------------------Buttons-------------------------------------#
button_method = Buttons(frame_middle_top)
button_method.randon_button('seek random')

button_save = tk.Button(frame_bottom, text='save')
button_save.pack()

# --------------------------------Listbox-------------------------------------#
list_box = tk.Listbox(frame_left, height=20, width=40, borderwidth=6, relief=tk.SUNKEN)
list_box.grid(column=0, row=0)
# --------------------------------Textbox-------------------------------------#
text_box = tk.Text(frame_right, height=20, width=50, borderwidth=6, relief=tk.SUNKEN)
text_box.grid(column=0, row=0)

window.resizable(False, False)
window.mainloop()