# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 00:47:03 2020

@author: Admin
"""

import tkinter as tk

window = tk.Tk()
window.title("String Patterns")
pad = 5

stringInput = tk.Entry(window, width=30)

buttonFrame = tk.Frame()
stringToNum = tk.Button(buttonFrame, text="To Number")
diffFromSelf = tk.Button(buttonFrame, text="Diff Self")

# grid
# stringInput.grid(column=0, row=0, padx=pad, pady=pad)
# stringInputButton.grid(column=0, row=1, padx=pad, pady=pad)
stringInput.pack()
buttonFrame.pack()
stringToNum.pack(side="left")
diffFromSelf.pack(side="left")

window.mainloop()