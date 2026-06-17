import os
import shutil

# Folder path
path = r"C:\Users\xyz/"

# Read all items in folder
file_name = os.listdir(path)

# File type mapping
file_type = {
    ".csv": "csv files",
    ".png": "image files",
    ".jpg": "image files",
    ".jpeg": "image files",
    ".txt": "text files"
}

# Create folders
for folder in set(file_type.values()):
    if not os.path.exists(path + folder):
        os.makedirs(path + folder)

# Create others folder
if not os.path.exists(path + "others"):
    os.makedirs(path + "others")

# Counters
file_moved = 0
file_count = {}

# Loop through all items
for file in file_name:

    source = path + file

    # Skip folders (only files to be moved)
    if not os.path.isfile(source):
        continue

    file_extension = os.path.splitext(file)[1].lower()

    # Known file types
    if file_extension in file_type:
        destination_folder = file_type[file_extension]

    # Unknown file types
    else:
        destination_folder = "others"

    destination = path + destination_folder + "/" + file

    # Move file if it doesn't already exist
    if not os.path.exists(destination):

        shutil.move(source, destination)

        file_moved += 1

        if destination_folder not in file_count:
            file_count[destination_folder] = 0

        file_count[destination_folder] += 1

# Print results
print(f"\nFiles sorted: {file_moved}")

print("\nSummary:")

for folder, count in file_count.items():
    print(f"{folder}: {count}")
print(file_count)
