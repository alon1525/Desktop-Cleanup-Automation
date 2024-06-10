# File Organizer

This Python script helps organize files on your desktop by sorting them into appropriate directories based on their file extensions. Additionally, it handles duplicates by renaming them with a "2" appended to their filenames.

## Features
- Moves files to specific directories based on their extensions.
- Renames duplicate files by appending "2" to their filenames.
- Deletes compressed files (e.g., .zip, .rar) from the desktop.

## Usage
1. Place the script file in a directory of your choice.
2. Run the script.
3. Files on your desktop will be organized into designated folders.

## How it Works
1. The script defines a dictionary mapping file extensions to destination directories.
2. It creates destination directories if they don't exist already.
3. Files on the desktop are iterated over.
4. For each file:
   - If it matches a known file extension, it's moved to the appropriate directory.
   - If a file with the same name already exists in the destination directory, the script renames the duplicate file by appending "2" to its filename before the extension.
   - Compressed files are deleted from the desktop.

## File Extensions and Corresponding Destination Directories
- Pictures: .png, .jpg, .jpeg, .gif, .bmp, .tiff
- Documents: .pdf, .doc, .docx
- Videos: .mp4
- Music: .mp3
- TextFiles: .txt
- Apps: .exe, .lnk (shortcut)
- Excel Files: .csv, .ods
- PowerPoint: .ppt, .pptx
