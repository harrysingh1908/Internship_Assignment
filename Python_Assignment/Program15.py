import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

class FileManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple File Manager")

        # Create the main frame
        self.frame = tk.Frame(root)
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Create the directory label and entry
        self.dir_label = tk.Label(self.frame, text="Current Directory:")
        self.dir_label.pack(anchor="w")
        self.dir_entry = tk.Entry(self.frame, width=80)
        self.dir_entry.pack(fill=tk.X, padx=5, pady=5)
        self.dir_entry.insert(0, os.getcwd())

        # Create the listbox to display files and directories
        self.file_listbox = tk.Listbox(self.frame, selectmode=tk.SINGLE)
        self.file_listbox.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.file_listbox.bind('<Double-1>', self.on_double_click)

        # Create the buttons for file operations
        self.button_frame = tk.Frame(self.frame)
        self.button_frame.pack(fill=tk.X, padx=5, pady=5)
        self.copy_button = tk.Button(self.button_frame, text="Copy", command=self.copy_file)
        self.copy_button.pack(side=tk.LEFT)
        self.move_button = tk.Button(self.button_frame, text="Move", command=self.move_file)
        self.move_button.pack(side=tk.LEFT)
        self.delete_button = tk.Button(self.button_frame, text="Delete", command=self.delete_file)
        self.delete_button.pack(side=tk.LEFT)
        self.refresh_button = tk.Button(self.button_frame, text="Refresh", command=self.refresh_list)
        self.refresh_button.pack(side=tk.LEFT)

        # Load the initial directory contents
        self.refresh_list()

    def refresh_list(self):
        """Refresh the listbox with the contents of the directory."""
        current_dir = self.dir_entry.get()
        self.file_listbox.delete(0, tk.END)
        try:
            for item in os.listdir(current_dir):
                self.file_listbox.insert(tk.END, item)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def on_double_click(self, event):
        """Handle double-click event on the listbox items."""
        selection = self.file_listbox.curselection()
        if selection:
            selected_item = self.file_listbox.get(selection[0])
            path = os.path.join(self.dir_entry.get(), selected_item)
            if os.path.isdir(path):
                self.dir_entry.delete(0, tk.END)
                self.dir_entry.insert(0, path)
                self.refresh_list()

    def copy_file(self):
        """Copy a selected file to a new location."""
        self.perform_file_operation(shutil.copy)

    def move_file(self):
        """Move a selected file to a new location."""
        self.perform_file_operation(shutil.move)

    def delete_file(self):
        """Delete the selected file or directory."""
        selection = self.file_listbox.curselection()
        if selection:
            selected_item = self.file_listbox.get(selection[0])
            path = os.path.join(self.dir_entry.get(), selected_item)
            if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete '{selected_item}'?"):
                try:
                    if os.path.isdir(path):
                        shutil.rmtree(path)
                    else:
                        os.remove(path)
                    self.refresh_list()
                except Exception as e:
                    messagebox.showerror("Error", str(e))

    def perform_file_operation(self, operation):
        """Perform a file operation like copy or move."""
        selection = self.file_listbox.curselection()
        if selection:
            selected_item = self.file_listbox.get(selection[0])
            src_path = os.path.join(self.dir_entry.get(), selected_item)
            dest_path = filedialog.askdirectory()
            if dest_path:
                try:
                    operation(src_path, dest_path)
                    self.refresh_list()
                except Exception as e:
                    messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = FileManager(root)
    root.geometry("600x400")
    root.mainloop()
