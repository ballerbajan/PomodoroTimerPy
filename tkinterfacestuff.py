import tkinter as tk
from tkinter import ttk

mainWin = tk.Tk()
mainWin.title("test")
mainWin.geometry("3000x2000")
newLabel = ttk.Label(master = mainWin, text = "test", font = ("Comic Sans MS", 60))
newLabel.pack()

def exitFunction():
    mainWin.destroy()

button = tk.Button(mainWin, text= "Exit",font= "35", command= exitFunction)
button.pack()
mainWin.mainloop()