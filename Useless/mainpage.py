import tkinter as tk 
from tkinter import *

window = tk.Tk()

window.geometry("800x480") 
window.title ("main screen ")

stopimage = PhotoImage(file="roadsigns\stopsign.png")

label1 = Label(image=stopimage).place(x=200, y=180)


window.mainloop()

