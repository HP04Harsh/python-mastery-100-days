import tkinter as tk

def greet():
    label.config(text="Welcome to Tkinter!")

root = tk.Tk()

label = tk.Label(root, text="Click Button")
label.pack()

tk.Button(root, text="Click Me", command=greet).pack()

root.mainloop()