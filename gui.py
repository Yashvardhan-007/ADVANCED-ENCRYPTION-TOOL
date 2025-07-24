import tkinter as tk
from tkinter import filedialog, messagebox
from aes_tool import encrypt_file, decrypt_file

def select_file():
    file_path.set(filedialog.askopenfilename())

def encrypt_action():
    try:
        encrypt_file(file_path.get(), password.get())
        messagebox.showinfo("Success", "File Encrypted Successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def decrypt_action():
    try:
        decrypt_file(file_path.get(), password.get())
        messagebox.showinfo("Success", "File Decrypted Successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

app = tk.Tk()
app.title("AES-256 File Encryption Tool")
app.geometry("400x200")

file_path = tk.StringVar()
password = tk.StringVar()

tk.Label(app, text="Select File:").pack()
tk.Entry(app, textvariable=file_path, width=50).pack()
tk.Button(app, text="Browse", command=select_file).pack(pady=5)

tk.Label(app, text="Enter Password:").pack()
tk.Entry(app, textvariable=password, show='*').pack(pady=5)

tk.Button(app, text="Encrypt", command=encrypt_action).pack(pady=5)
tk.Button(app, text="Decrypt", command=decrypt_action).pack()

app.mainloop()
