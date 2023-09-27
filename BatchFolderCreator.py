import os
import tkinter as tk
from tkinter import filedialog

def create_folders(names, directory):
    existing_folders = []
    created_folders = []

    for name in names:
        name = name.strip()  # Remove leading/trailing spaces and line breaks
        folder_path = os.path.join(directory, name)
        if os.path.exists(folder_path):
            existing_folders.append(name)
            print(f"Folder already exists: {folder_path}")
        else:
            os.mkdir(folder_path)
            created_folders.append(name)
            print(f"Created folder: {folder_path}")

            # Create 'Exports' and 'Assets' subfolders
            exports_path = os.path.join(folder_path, 'Exports')
            assets_path = os.path.join(folder_path, 'Assets')

            os.mkdir(exports_path)
            os.mkdir(assets_path)
            print(f"Created subfolder: {exports_path}")
            print(f"Created subfolder: {assets_path}")

    # Display appropriate message to the user
    if existing_folders:
        existing_message = "Folders already exist:\n" + '\n'.join(existing_folders)
        message_label.config(text=existing_message, cursor="xterm")
    else:
        message_label.config(text="", cursor="")

    if created_folders:
        created_message = "Created folders:\n" + '\n'.join(created_folders)
        message_label2.config(text=created_message, cursor="xterm")
    else:
        message_label2.config(text="", cursor="")

def browse_directory():
    directory = filedialog.askdirectory()
    directory_entry.delete(0, tk.END)
    directory_entry.insert(0, directory)

def add_names():
    names = name_entry.get("1.0", "end-1c").splitlines()  # Retrieve all content from Text widget
    names = [name.strip('"') for name in names]  # Remove double quotes
    names_str = ', '.join(names)  # Join with commas
    directory = directory_entry.get()
    create_folders(names, directory)
    name_entry.delete("1.0", tk.END)  # Clear the Text widget
    name_entry.insert(tk.END, names_str)  # Insert the modified names back into the Text widget

# Create the main window
root = tk.Tk()
root.title("Folder Creator")

# Label and Entry for directory selection
directory_label = tk.Label(root, text="Select Directory:")
directory_label.pack()
directory_entry = tk.Entry(root, width=50)
directory_entry.pack()
browse_button = tk.Button(root, text="Browse", command=browse_directory)
browse_button.pack()

# Textbox for adding names with line breaks
name_label = tk.Label(root, text="Add Names (one per line):")
name_label.pack()
name_entry = tk.Text(root, width=50, height=10)
name_entry.pack()

# Button to create folders
create_button = tk.Button(root, text="Create Folders", command=add_names)
create_button.pack()

# Labels to display the messages
message_label = tk.Label(root, text="", cursor="xterm")
message_label.pack()
message_label2 = tk.Label(root, text="", cursor="xterm")
message_label2.pack()

# Start the GUI main loop
root.mainloop()
