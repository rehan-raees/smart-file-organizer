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

1. Read all items from folder
2. Ignore folders
3. Identify file extension
4. Match extension to destination folder
5. Move file
6. Display summary
