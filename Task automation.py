import os
import shutil

def organize_files(directory):

    if not os.path.exists(directory):
        print("Directory does not exist. Please provide a valid path.")
        return


    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
        "Videos": [".mp4", ".mkv", ".avi", ".mov"],
        "Music": [".mp3", ".wav", ".aac"],
        "Archives": [".zip", ".rar", ".tar.gz"],
        "Others": []  # Everything else goes here
    }


    for folder in file_types.keys():
        folder_path = os.path.join(directory, folder)
        os.makedirs(folder_path, exist_ok=True)


    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)


        if os.path.isdir(file_path):
            continue


        moved = False
        for folder, extensions in file_types.items():
            if any(file.lower().endswith(ext) for ext in extensions):
                shutil.move(file_path, os.path.join(directory, folder, file))
                print(f"Moved: {file} --> {folder}")
                moved = True
                break


        if not moved:
            shutil.move(file_path, os.path.join(directory, "Others", file))
            print(f"Moved: {file} --> Others")

if __name__ == "__main__":

    target_directory = input("Enter the path of the directory to organize: ").strip()
    organize_files(target_directory)