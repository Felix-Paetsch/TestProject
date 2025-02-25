from tkinter import filedialog

while True:
    folder_path = filedialog.askdirectory()
    print("Selected folder:", folder_path)
