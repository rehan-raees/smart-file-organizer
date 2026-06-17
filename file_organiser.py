import os
import shutil

# Folder path
path = r"C:\Your\Folder\Path\\"

# Get all items in folder
file_name = os.listdir(path)

# File type mapping
file_type = {
    ".csv": "csv files",
    ".png": "image files",
    ".jpg": "image files",
    ".jpeg": "image files",
    ".txt": "text files"
}

# Create destination folders
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

    # Full path of current item
    source = path + file

    # Skip folders
    if not os.path.isfile(source):
        continue

    # Get extension
    file_extension = os.path.splitext(file)[1].lower()

    # Decide destination folder
    if file_extension in file_type:
        destination_folder = file_type[file_extension]
    else:
        destination_folder = "others"

    # Build destination path
    destination = path + destination_folder + "/" + file

    # Handle duplicate file names
    if os.path.exists(destination):

        file_name_only, file_extension = os.path.splitext(file)

        counter = 1

        while os.path.exists(destination):

            new_file_name = (
                f"{file_name_only}_{counter}{file_extension}"
            )

            destination = (
                path + destination_folder + "/" + new_file_name
            )

            counter += 1

    # Move file
    shutil.move(source, destination)

    # Update counters
    file_moved += 1

    if destination_folder not in file_count:
        file_count[destination_folder] = 0

    file_count[destination_folder] += 1

# Print results
print(f"\nFiles sorted: {file_moved}")

print("\nSummary:")

for folder, count in file_count.items():
    print(f"{folder}: {count}")
