import tkinter as tk
from tkinter import messagebox
import time

def show_message():
    messagebox.showwarning("Warning", "Your computer has been infected!")
    time.sleep(120) 
    show_message()

root = tk.Tk()
root.withdraw()  
show_message()
root.mainloop()