import functions
import os
import tkinter as tk
from tkinter import filedialog

def open_file_dialog():
    file_path = filedialog.askopenfilename(title="Select File(s)", filetypes=[("All files", "*.*"), ("MP3 files", "*.mp3"), ])
    if file_path:
        selected_file_label.config(text=f"Selected File: {file_path}")
        process_file(file_path)

def process_file(file_path):
    return
    

#Tkinter GUI
root = tk.Tk()
root.title("File Dialog Example")

open_button = tk.Button(root, text="Open", command=open_file_dialog)
open_button.pack(padx=20, pady=20)

selected_file_label = tk.Label(root, text="Selected File:")
selected_file_label.pack()

file_text = tk.Text(root, wrap=tk.WORD, height=10, width=40)
file_text.pack(padx=20, pady=20)

root.mainloop()


