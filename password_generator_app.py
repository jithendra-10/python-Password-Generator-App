import random
import string
import tkinter as tk
from tkinter import messagebox
import pyperclip
def generate_password():
    length=len_slider.get()
    use_digits=dig_var.get()
    use_special=spl_var.get()
    chars=string.ascii_letters
    if use_digits:
        chars+=string.digits
    if use_special:
        chars+=string.punctuation
    password=''.join(random.choice(chars) for _ in range(length))
    password_entry.delete(0,tk.END)
    password_entry.insert(0,password)
    pyperclip.copy(password)
    messagebox.showinfo("Password Copied","Password copied to clipboard!")
root=tk.Tk()
root.title("Password Generator 🔑 ")
root.geometry("400x300")
root.config(bg="#f4f4f4")
tk.Label(root , text="Random Password Generator",font=("Arial", 14,"bold"), bg="#f4f4f4").pack(pady=10)
tk.Label(root, text="Password Length:", font=("Arial", 12), bg="#f4f4f4").pack()
len_slider = tk.Scale(root, from_=4, to=32, orient="horizontal", font=("Arial", 10))
len_slider.set(12)
len_slider.pack()
dig_var=tk.BooleanVar(value=True)
spl_var=tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Include Numbers", variable=dig_var, bg="#f4f4f4", font=("Arial", 10)).pack()
tk.Checkbutton(root, text="Include Special Characters", variable=spl_var, bg="#f4f4f4", font=("Arial", 10)).pack()

generate_btn = tk.Button(root, text="Generate Password", font=("Arial", 12), command=generate_password)
generate_btn.pack(pady=10)
password_entry = tk.Entry(root, font=("Arial", 12), width=30, justify="center")
password_entry.pack(pady=5)
root.mainloop()