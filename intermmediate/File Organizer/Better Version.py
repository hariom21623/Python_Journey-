# Real Categories : 

import os
import shutil

source = r"c:\Users\Hariom\Downloads"

file_types = {
    "Images": ["jpg", "jpeg", "png", "gif"],
    "Documents": ["pdf", "docx", "txt"],
    "Videos": ["mp4", "mkv"],
    "Audio": ["mp3", "wav"],
    "Code": ["py", "js", "html", "css"]
}

for file in os.listdir(source):
    path = os.path.join(source, file)

    if os.path.isfile(path):
        ext = file.split(".")[-1].lower()

        moved = False

        for folder, extensions in file_types.items():
            if ext in extensions:
                folder_path = os.path.join(source, folder)

                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                shutil.move(path, os.path.join(folder_path, file))
                moved = True
                break

        if not moved:
            other_path = os.path.join(source, "Others")
            if not os.path.exists(other_path):
                os.makedirs(other_path)

            shutil.move(path, os.path.join(other_path, file))

print("Organized into categories!")