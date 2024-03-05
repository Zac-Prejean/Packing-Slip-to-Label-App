

import tkinter as tk  
from tkinter import ttk  
  
def create_tkinter_interface():  
    root = tk.Tk()  
    root.title("Scan to Print")  
  
    # Set the window size  
    root.geometry("800x600")  
    root.resizable(False, False)  
  
  
    mainframe = ttk.Frame(root, padding="10")  
    mainframe.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))  
  
    # Configure the columns and rows to expand  
    root.columnconfigure(0, weight=1)  
    root.rowconfigure(0, weight=1)  
    mainframe.columnconfigure(0, weight=1)  
    mainframe.columnconfigure(1, weight=1)  
    mainframe.rowconfigure(0, weight=1)  
    mainframe.rowconfigure(1, weight=1)  
    mainframe.rowconfigure(2, weight=1)  
  
    barcode_label = ttk.Label(mainframe, text="Barcode:", font=("Montserrat", 20))  
    barcode_label.grid(column=0, row=1, padx=5, pady=5, sticky=tk.E)  
  
    barcode_entry = ttk.Entry(mainframe, width=30, font=("Montserrat", 15))  
    barcode_entry.grid(column=1, row=1, padx=5, pady=5)  
    barcode_entry.focus()  
  
    result_text = tk.StringVar()  
    result_label = ttk.Label(mainframe, textvariable=result_text)  
    result_label.grid(column=0, row=3, columnspan=2, padx=5, pady=5)  
  
    # Create history window  
    history_label = ttk.Label(mainframe, text="Scan History:", font=("Montserrat", 15))  
    history_label.grid(column=0, row=4, padx=5, pady=5, sticky=tk.W)  
  
    history_frame = ttk.Frame(mainframe)  
    history_frame.grid(column=0, row=5, columnspan=2, padx=5, pady=6, sticky=(tk.W, tk.E, tk.N, tk.S))  
  
    scrollbar = tk.Scrollbar(history_frame)  
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)  
  
    history_listbox = tk.Listbox(history_frame, yscrollcommand=scrollbar.set, width=50, height=10)  
    history_listbox.pack(side=tk.LEFT, fill=tk.BOTH)  
  
    scrollbar.config(command=history_listbox.yview)  
  
    return root, barcode_entry, result_text, history_listbox  
 
