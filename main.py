import tkinter as tk
from class_window import Window
from class_label import CustomLabel
from class_button import Buttons
from class_listbox import CustomListbox
from class_text import CustomText

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

# frame_bottom = tk.Frame(window, width=500, height=40, bg='red')
# frame_bottom.pack(side=tk.BOTTOM, pady=5)

# --------------------------------Label---------------------------------------#
label_title = CustomLabel(frame_top)
label_title.big_title('IT\'S TIME TO STUDY')

label_method = CustomLabel(frame_middle_top)
label_method.middle_label('METHOD')

# --------------------------------Buttons-------------------------------------#
button_method = Buttons(frame_middle_top)
button_method.randon_button('seek random')

# button_save = tk.Button(frame_bottom, text='save')
# button_save.pack()

list_box = CustomListbox(frame_left)
list_box.with_vertical_scroll()
# --------------------------------Textbox-------------------------------------#
text_box = CustomText(frame_left)
text_box.With_vertical_scroll()

window.resizable(False, False)
window.mainloop()
