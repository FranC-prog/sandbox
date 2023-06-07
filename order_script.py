import os
import shutil

# Set the directory path to the folder containing the files
directory = "/Users/franc/OneDrive/Documentos"

# Loop through each file in the directory
for filename in os.listdir(directory):
    # Get the first 4 characters of the file name
    prefix = filename[:4]

    # Create a directory with the prefix name if it doesn't exist
    if not os.path.exists(os.path.join(directory, prefix)):
        os.mkdir(os.path.join(directory, prefix))

    # Get the full path of the source file
    src_path = os.path.join(directory, filename)

    # Get the full path of the destination directory
    dest_path = os.path.join(directory, prefix)

    # Check if the source and destination paths are the same
    if os.path.abspath(src_path) != os.path.abspath(dest_path):
        # Move the file to the directory with the matching prefix
        shutil.move(src_path, os.path.join(dest_path, filename))
