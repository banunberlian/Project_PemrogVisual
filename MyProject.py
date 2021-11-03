import tkinter as tk

window = tk.Tk()
window.title('Data Mahasiswa')
window.geometry('600x400')

inputNama = tk.Entry(window)
inputNim = tk.Entry(window)
inputAlamat = tk.Entry(window)
inputJenisKelamin = tk.Entry(window)

tk.Label(window, text="Nama : ").grid(row=0, column=0)
tk.Label(window, text="Nim  : ").grid(row=1, column=0)
tk.Label(window, text="Alamat : ").grid(row=2, column=0)
tk.Label(window, text="Jenis Kelamin : ").grid(row=3, column=0)

inputNama.grid(row=0, column=1)
inputNim.grid(row=1, column=1)
inputAlamat.grid(row=2, column=1)
inputJenisKelamin.grid(row=3, column=1)

window.mainloop()