import os
import shutil

desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')

# Define dictionary for mapping file types to destination directories
destination_directories = {
    '.png': 'Pictures',
    '.jpg': 'Pictures',
    '.jpeg': 'Pictures',
    '.pdf': 'Documents',
    '.doc': 'Documents',
    '.docx': 'Documents',
    '.mp4': 'Videos',
    '.mp3': 'Music',
    '.gif': 'Pictures',
    '.bmp': 'Pictures',
    '.tiff': 'Pictures',
    '.txt': 'TextFiles',
    '.exe': 'Apps',
    '.lnk': 'Apps',
    '.csv': 'Excel Files',
    '.ods': 'Excel Files',
    '.ppt': 'PowerPoint',
    '.pptx': 'PowerPoint',
}

# Create destination directories if they don't exist
for directory in destination_directories.values():
    directory_path = os.path.join(desktop_path, directory)
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)


# Sorting all my files into folders with appropriate names based on their extention if theres duplicate just add 2 to its name
def sort_files():
    for file in os.listdir(desktop_path):
        file_extension = os.path.splitext(file)[1].lower()
        if file_extension in destination_directories:
            destination_directory = destination_directories[file_extension]
            destination_path = os.path.join(desktop_path, destination_directory)
            source_file_path = os.path.join(desktop_path, file)
            destination_file_path = os.path.join(destination_path, file)
            if os.path.exists(destination_file_path):
                new_file_path = os.path.join(destination_path, os.path.splitext(file)[0] + "2" + file_extension)
                try:
                    os.rename(source_file_path, new_file_path)  # Rename duplicate file
                    print(f"Renamed duplicate {file} to {os.path.basename(new_file_path)} in {destination_directory}")
                    shutil.move(new_file_path, destination_path)
                except Exception as e:
                    print(f"Failed to rename duplicate {file}: {e}")
            else:
                shutil.move(source_file_path, destination_path)
                print(f"Moved {file} to {destination_directory}")
        else:
            print(f"No destination directory found for {file}")


# Deleting all my zip files
def delete_compressed_files():
    for file in os.listdir(desktop_path):
        if file.endswith(('.rar', '.zip')):
            file_path = os.path.join(desktop_path, file)
            try:
                os.remove(file_path)
                print(f"Deleted {file}")
            except Exception as e:
                print(f"Failed to delete {file}: {e}")


delete_compressed_files()

sort_files()
