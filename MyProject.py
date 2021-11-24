import tkinter as tk

window = tk.Tk()
window.title('Data Mahasiswa')
window.geometry('500x400')

def create():
    nama = inputNama.get()
    tk.Label(window, text="Nama : " + nama).grid(row=5, column=1)
    nim = inputNim.get()
    tk.Label(window, text="Nim: " + nim).grid(row=7, column=1)
    alamat = inputAlamat.get()
    tk.Label(window, text="Alamat: " + alamat).grid(row=8, column=1)
    jeniskelamin = inputJenisKelamin.get()
    tk.Label(window, text="Jenis Kelamin: " + jeniskelamin).grid(row=9, column=1)
    tanggallahir = inputTanggalLahir.get()
    

inputNama = tk.Entry(window)
inputNim = tk.Entry(window)
inputAlamat = tk.Entry(window)
inputJenisKelamin = tk.Entry(window)
inputTanggalLahir = tk.Entry(window)

tk.Label(window, text="Nama : ").grid(row=0, column=0)
tk.Label(window, text="Nim  : ").grid(row=1, column=0)
tk.Label(window, text="Alamat : ").grid(row=2, column=0)
tk.Label(window, text="Jenis Kelamin : ").grid(row=3, column=0)
tk.Label(window, text="Tanggal Lahir : ").grid(row=4, column=0)

inputNama.grid(row=0, column=1)
inputNim.grid(row=1, column=1)
inputAlamat.grid(row=2, column=1)
inputJenisKelamin.grid(row=3, column=1)
inputTanggalLahir.grid(row=4, column=1)

tk.Button(window, text="submit", command=create).grid(row=4, column=1)
window.mainloop()