from tkinter import *
from tkinter import messagebox

ws =Tk()
ws.title("Python Guides")
ws.geometry("300x250")

def about():
    messagebox.showinfo('PythonGuides', 'Python Guides aims at providing best practical tutorials')

menubar = Menu(ws, foreground='black', activebackground='white', activeforeground='black')
file = Menu(menubar, tearoff=1, foreground='black')
file.add_command(label="Nowy")
file.add_command(label="Nowe okno")
file.add_command(label="Otwórz..")
file.add_command(label="Zapisz")
file.add_separator()
file.add_command(label="Exit", command=ws.quit)
menubar.add_cascade(label="Plik", menu=file)

ws.config(menu=menubar)
ws.mainloop()
