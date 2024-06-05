"""
##### Task 1
Create entry widets to allow user to enter their:
* name
* student number
* grade

Create a button so that when they click on the button, it states all of the information in a 4th entry widget
"""
import tkinter as tk 

def run(e):
    print("This does not show up on your gui")
    print(f"The details of the event are {e}")
    data = e1.get()
    data = e2.get()
    data = e3.get()
    l1.config(text=data)
    e4.delete(0,tk.END)
    e4.insert(0,data)

win = tk.Tk()
e1 = tk.Entry(win,width=15)
b1 = tk.Button(win, text="Click to change the text")
e2 = tk.Entry(win, width=15)
e3 = tk.Entry(win, width=15)
e4 = tk.Entry(win,width=15)
l1 = tk.Label(win, width=15, text="Original Text")


b1.bind("<Button-1>",run)


e1.pack()
l1.pack()
b1.pack()
e2.pack()
win.mainloop()