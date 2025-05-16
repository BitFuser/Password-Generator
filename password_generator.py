import random
import string
import tkinter as tk
from tkinter import ttk, messagebox
import pyperclip

# Auto-install pyperclip if missing
try:
    import pyperclip
except ImportError:
    import subprocess, sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyperclip"])
    import pyperclip

def generate_password():
    length = int(length_var.get())
    use_upper = upper_var.get()
    use_digits = digit_var.get()
    use_symbols = symbol_var.get()

    charset = list(string.ascii_lowercase)
    if use_upper:
        charset += list(string.ascii_uppercase)
    if use_digits:
        charset += list(string.digits)
    if use_symbols:
        charset += list("!@#$%^&*()-_=+")

    if not charset:
        messagebox.showerror("Error", "Please select at least one character type.")
        return

    password = ''.join(random.choice(charset) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# GUI setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("350x250")
root.resizable(False, False)

frame = ttk.Frame(root, padding=20)
frame.pack()

ttk.Label(frame, text="Password Length:").grid(row=0, column=0, sticky="w")
length_var = tk.StringVar(value="16")
length_spin = ttk.Spinbox(frame, from_=4, to=64, textvariable=length_var, width=5)
length_spin.grid(row=0, column=1)

upper_var = tk.BooleanVar(value=True)
ttk.Checkbutton(frame, text="Include Uppercase", variable=upper_var).grid(row=1, columnspan=2, sticky="w")

digit_var = tk.BooleanVar(value=True)
ttk.Checkbutton(frame, text="Include Numbers", variable=digit_var).grid(row=2, columnspan=2, sticky="w")

symbol_var = tk.BooleanVar(value=True)
ttk.Checkbutton(frame, text="Include Symbols", variable=symbol_var).grid(row=3, columnspan=2, sticky="w")

ttk.Button(frame, text="Generate Password", command=generate_password).grid(row=4, columnspan=2, pady=10)

password_entry = ttk.Entry(frame, width=40)
password_entry.grid(row=5, columnspan=2)

root.mainloop()
