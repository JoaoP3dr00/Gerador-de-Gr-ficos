import ttkbootstrap as ttkb
import tkinter as tk

root = ttkb.Window()

ttkb.Label(text="oi").pack(padx=2, pady=2)
tk.Label(text="oi", padx=2, pady=2).pack()

root.mainloop()
