from tkinter import *


tk = Tk()

def km_to_miles():
    var = int(e1_value.get())
    var = var * 0,6
  
    t1.insert(END, var)

b1 = Button(tk, text = 'Execute', command = km_to_miles)
b1.grid(row = 0, column = 0)


e1_value = StringVar()
e1 = Entry(tk, textvariable = e1_value)
e1.grid(row = 0 , column = 1)


t1 = Text (tk, height = 1 , width = 20)
t1.grid(row =0 , column = 2)

tk.mainloop()