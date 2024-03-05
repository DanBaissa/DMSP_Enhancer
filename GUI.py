import tkinter as tk
from tkinter import ttk, filedialog, messagebox

class EnhanceGUI:
    def __init__(self, master, countries, enhance_callback):
        self.master = master
        master.title("DMSP Data Enhancement")

        self.enhance_callback = enhance_callback

        self.dmsp_folder = None

        self.country_var = tk.StringVar(master)
        self.country_combobox = ttk.Combobox(master, textvariable=self.country_var, values=countries, state="readonly")
        self.country_combobox.set("Select a Country")
        self.country_combobox.pack()

        self.dmsp_button = tk.Button(master, text="Select DMSP Data Folder", command=self.select_dmsp_folder)
        self.dmsp_button.pack()

        self.enhance_button = tk.Button(master, text="Enhance Data", command=self.on_enhance)
        self.enhance_button.pack()

    def select_dmsp_folder(self):
        self.dmsp_folder = filedialog.askdirectory()
        print("DMSP Data Folder Selected:", self.dmsp_folder)

    def on_enhance(self):
        if not self.dmsp_folder or self.country_var.get() == "Select a Country":
            messagebox.showwarning("Warning", "Please select a DMSP data folder and a country.")
            return
        self.enhance_callback(self.dmsp_folder, self.country_var.get())
