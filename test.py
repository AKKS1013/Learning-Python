import tkinter as tk
root = tk.Tk()
def increment(var):
    var.set(var.get() + 1)

answer = tk.IntVar()
tk.Button(root, text="Click Me!", command=lambda: increment(answer)).pack()
tk.Label(root, textvariable=answer).pack()
root.mainloop()
