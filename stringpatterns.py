# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 00:47:03 2020

@author: Admin
"""

import tkinter as tk

def doSomething():
    output.delete(1.0, tk.END)
    inp = stringInput.get()
    if inp.find("->") != -1:
       strings = inp.split('->')
       strings[0] = strings[0].strip()
       strings[1] = strings[1].strip()
       for i in range(len(strings[0])):
           output.insert(tk.END, ord(strings[1][i]) - ord(strings[0][i]))
           output.insert(tk.END, ' ')
    else:
        for i in range(len(inp)):
            if inp[i] != ' ':
                output.insert(tk.END, ord(inp[i]) - ord('A') + 1)
                output.insert(tk.END, ' ')
            else:
                output.insert(tk.END, ', ')
            

window = tk.Tk()
window.title("String Patterns")
pad = 5

stringInput = tk.Entry(window, width=50)
buttonFrame = tk.Frame()
stringToNum = tk.Button(buttonFrame, text="To Number", command=doSomething)
diffFromSelf = tk.Button(buttonFrame, text="Diff Self")
output = tk.Text(window, width=50, height=1)

# grid
stringInput.pack(pady=pad, padx=pad)
buttonFrame.pack(pady=pad)
stringToNum.pack(side="left", padx=pad)
diffFromSelf.pack(side="left")
output.pack(pady=pad)

window.mainloop()