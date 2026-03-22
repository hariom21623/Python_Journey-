''' 
Core Logic: This code organizes files in a specified source folder by moving them into 
subfolders based on their file extensions. It checks each file in the source folder, 
determines its extension, creates a corresponding subfolder if it doesn't exist, and 
then moves the file into that subfolder.
'''

import os
import shutil

source_folder = r"c:\Users\Hariom\Downloads"

for file in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file)

    if os.path.isfile(file_path):
        ext = file.split(".")[-1]

        folder_path = os.path.join(source_folder, ext)

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        shutil.move(file_path, os.path.join(folder_path, file))

print("Files organized successfully!")