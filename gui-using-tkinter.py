import tkinter as tk
from tkinter import ttk

#   Creating a Window:

window = tk.Tk()
window.title('Windows')
window.geometry('450x300')

#   Title:

title_label = ttk.Label(
    master = window, 
    text = "Linux.", 
    font = 'Times New Roman 22 bold'
    )
title_label.pack()

#   Run:

window.mainloop()