# Smart File Organizer

A Python automation project that organizes files into folders based on file type.

## Features

- Automatically creates folders
- Sorts files by extension
- Handles unknown file types
- Ignores folders during processing
- Displays sorting summary

## Technologies Used

- Python
- os
- shutil

## Example

sales.csv -> csv files

image.png -> image files

report.pdf -> others


## Project Workflow

1. Read all items from the selected folder
2. Ignore folders and process only files
3. Identify the file extension
4. Match the extension to a destination folder
5. Create folders if they do not exist
6. Handle duplicate file names automatically
7. Move files to their destination folders
8. Display a summary of files sorted
