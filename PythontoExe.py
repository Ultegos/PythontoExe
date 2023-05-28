import tkinter as tk
from tkinter import filedialog
import subprocess

class FileConverter:
    def __init__(self, root):
        self.root = root

        self.setup_ui()

    def setup_ui(self):
        self.root.title("Python to Windows Executable Converter")

        # Create a label
        self.label = tk.Label(self.root, text="Select a Python file to convert:")
        self.label.pack(pady=10)

        # Create a button to select a file
        self.select_button = tk.Button(self.root, text="Select File", command=self.select_file)
        self.select_button.pack(pady=5)

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])

        if file_path:
            self.convert_to_executable(file_path)

    def convert_to_executable(self, file_path):
        # Convert the Python file to a Windows executable using PyInstaller
        command = ['pyinstaller', '--onefile', '--windowed', file_path]
        subprocess.call(command)

        self.label.configure(text="Conversion completed!")

    def close_window(self):
        self.root.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    gui = FileConverter(root)
    root.mainloop()
