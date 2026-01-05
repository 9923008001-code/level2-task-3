import os
import shutil

# Path to Downloads folder
path = os.path.expanduser("~/Downloads")

# File type folders
folders = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".avi", ".mkv"],
    "CSV Files": [".csv"]
}

# Create folders if not exists
for folder in folders:
    folder_path = os.path.join(path, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Organize files
for file in os.listdir(path):
    file_path = os.path.join(path, file)

    if os.path.isfile(file_path):
        moved = False
        for folder, extensions in folders.items():
            if file.lower().endswith(tuple(extensions)):
                shutil.move(file_path, os.path.join(path, folder, file))
                moved = True
                break

        if not moved:
            other_folder = os.path.join(path, "Others")
            if not os.path.exists(other_folder):
                os.makedirs(other_folder)
            shutil.move(file_path, os.path.join(other_folder, file))

print("✅ Files organized successfully!")
