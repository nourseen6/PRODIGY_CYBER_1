import tkinter as tk
from tkinter import messagebox


def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def encrypt_text():
    msg = message_entry.get()
    try:
        shift = int(shift_entry.get())
        encrypted = encrypt(msg, shift)
        output_label.config(text="Encrypted: " + encrypted)
    except:
        messagebox.showerror("Error", "Shift must be a number")

def decrypt_text():
    msg = message_entry.get()
    try:
        shift = int(shift_entry.get())
        decrypted = decrypt(msg, shift)
        output_label.config(text="Decrypted: " + decrypted)
    except:
        messagebox.showerror("Error", "Shift must be a number")


window = tk.Tk()
window.title("Caesar Cipher Tool")
window.geometry("500x350")  

font_large = ("Arial", 14)
font_medium = ("Arial", 12)


tk.Label(window, text="Enter Message:", font=font_large).pack(pady=(20, 5))
message_entry = tk.Entry(window, width=50, font=font_medium)
message_entry.pack(pady=5)

tk.Label(window, text="Enter Shift:", font=font_large).pack(pady=(15, 5))
shift_entry = tk.Entry(window, width=10, font=font_medium)
shift_entry.pack(pady=5)

tk.Button(window, text="Encrypt", command=encrypt_text, font=font_medium, width=15, bg="#4CAF50", fg="white").pack(pady=10)
tk.Button(window, text="Decrypt", command=decrypt_text, font=font_medium, width=15, bg="#2196F3", fg="white").pack()

output_label = tk.Label(window, text="", font=font_large, fg="purple", wraplength=480, justify="center")
output_label.pack(pady=20)

window.mainloop()
