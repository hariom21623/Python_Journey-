# Best Practice

import os
import shutil

source = input("Enter folder path: ")

file_types = {
    "Images": ["jpg", "jpeg", "png", "gif"],
    "Documents": ["pdf", "docx", "txt"],
    "Videos": ["mp4", "mkv"],
    "Audio": ["mp3", "wav"],
    "Code": ["py", "js", "html", "css"]
}

def get_unique_name(folder, filename):
    name, ext = os.path.splitext(filename)
    counter = 1
    new_name = filename

    while os.path.exists(os.path.join(folder, new_name)):
        new_name = f"{name}_{counter}{ext}"
        counter += 1

    return new_name

for file in os.listdir(source):
    path = os.path.join(source, file)

    if os.path.isfile(path):
        ext = file.split(".")[-1].lower()
        moved = False

        for folder, extensions in file_types.items():
            if ext in extensions:
                folder_path = os.path.join(source, folder)
                os.makedirs(folder_path, exist_ok=True)

                new_name = get_unique_name(folder_path, file)
                shutil.move(path, os.path.join(folder_path, new_name))

                moved = True
                break

        if not moved:
            other_path = os.path.join(source, "Others")
            os.makedirs(other_path, exist_ok=True)

            new_name = get_unique_name(other_path, file)
            shutil.move(path, os.path.join(other_path, new_name))

print("✅ Files organized successfully!")