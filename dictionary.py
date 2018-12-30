'''
This is the main UI for the dictionary
A built in UI library from Python called Tkinter
used of the dictionary UI

'''

import definition as define
from Tkinter import *

def view_meaning():
    listbox.delete(0,END)
    meaning = define.word(txtBox.get())
    print ("MEANING:   ", meaning)
    for m in define.organizer(meaning):
        listbox.insert(END, m)

window = Tk()
window.geometry("530x250")

b1 = Button(window, text = "Definitions", command = view_meaning)
b1.grid(row = 1, column = 1)

label1 = Label(window, text = "Word")
label1.grid(row = 0, column = 0)

label2 = Label(window, text = "Meaning")
label2.grid(row = 0, column = 2)

txtBox = Entry(window)
txtBox.grid(row = 1, column = 0,padx=(10, 10))

sb1 = Scrollbar(window)
sb1.grid(row=1, column = 3, rowspan = 6)

sb2 = Scrollbar(window,orient=HORIZONTAL)
sb2.grid(row=2, column = 2)

listbox = Listbox(window, width = 45)
listbox.grid(row = 1, rowspan = 1, column = 2, padx = (10,10))

listbox.configure(yscrollcommand = sb1.set, xscrollcommand = sb2.set)
sb1.configure(command = listbox.yview)
sb2.configure(command = listbox.xview)




window.mainloop()
