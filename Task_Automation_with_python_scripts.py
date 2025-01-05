'''3)Task Automation with Python Scripts
Identify a repetitive task in your workflow and create
Python scripts to automate it. This could include tasks
like file organization, data cleaning, or system
maintenance.
'''

import os
import shutil

source_folder = "C:/path/to/your/folder"

categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv"],
    "Music": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".rar", ".tar"],
}

for category in categories:
    category_path = os.path.join(source_folder, category)
    if not os.path.exists(category_path):
        os.makedirs(category_path)

def organize_files():
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)

        if os.path.isfile(file_path):

            file_extension = os.path.splitext(filename)[1].lower()


            for category, extensions in categories.items():
                if file_extension in extensions:
                    destination = os.path.join(source_folder, category, filename)
                    shutil.move(file_path, destination)
                    print(f"Moved: {filename} -> {category}")
                    break

organize_files()

print("File organization completed.")

