import tkinter as tk

master = tk.TK()
master.title("First UI Code")
master.geometry("300x300")

tk.Label(master, text="Nama : ").grid(row=0, column=0)

tk.mainloop()