import random 
import string 
import tkinter as tk 
from tkinter import ttk 
from tkinter import messagebox
from ttkthemes import ThemedTk

# Function to generate the password
def generate_password(): 
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for i in range(var.get()))
    output.config(text=password)
    output.config(text=password, font=("Ubuntu", 20), justify='center')

# Function to copy the password to clipboard
def copy_to_clipboard(): 
    root.clipboard_clear()
    root.clipboard_append(output['text'])
    messagebox.showinfo("Notification", "Text copied to clipboard successfully!")

# Create themed tkinter window 
root = ThemedTk(theme="aqua")
root.title("Password Generator")
root.geometry("300x300")

# Variable to hold the minimum number of characters in the password
var = tk.IntVar()
var.set(8)

# Create a dropdown menu for the number of characters
dropdown = ttk.Combobox(root, textvariable=var, values=[8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
dropdown.pack(pady=20)

#Create a consistent style for the buttons 
style = ttk.Style()
style.configure("TButton", font=("Ubuntu", 14))

# Create a generate button with increased font size
generate_button = ttk.Button(root, text="Generate", command=generate_password, style = "TButton")
generate_button.pack(pady=20)


# Create a copy button with increased font size
copy_button = ttk.Button(root, text="Copy", command=copy_to_clipboard, style = "TButton")
copy_button.pack(pady=20)


# Create an output field
output = ttk.Label(root)
output.pack(pady=20)

# Run the main function 
root.mainloop()
