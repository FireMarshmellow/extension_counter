import os
import time
import shutil

# Set the directory path where the folders should be created
directory_path = ""
# directory_path = "C:/Users/tomas/Desktop/test"

# Set the extensions of the files to look for
extensions = [".jpg", ".mp4", ".procreate"]

# Create the folders with names starting from 0000 to 9999
for i in range(1, 10000):
    folder_name = "{:04d}".format(i)

    completed_directory_path = os.path.join(directory_path, "completed")

    folder_path = os.path.join(directory_path, folder_name)

    # Check if the folder already exists
    if not os.path.exists(os.path.join(directory_path, "completed", folder_name)):
        # Create the folder if it does not exist
        os.makedirs(os.path.join(directory_path, folder_name))

    # Wait until there is one file with each of the desired extensions in the folder
    while True:
        # Get the list of files in the folder
        try:
            files = os.listdir(os.path.join(directory_path, folder_name))
        except:
            files = os.listdir(os.path.join(directory_path, "completed", folder_name))

        time.sleep(0.5)
        # Initialize a dictionary to count the number of files with each extension
        counts = {ext: 0 for ext in extensions}

        # Count the number of files with each extension
        for file in files:
            for ext in extensions:
                if file.endswith(ext):
                    counts[ext] += 1
        print(folder_name, counts)
        # If there is at least one file with each extension, break out of the loop
        if all(counts.values()):
            break

    if not os.path.exists(os.path.join(completed_directory_path, folder_name)):
        shutil.move(folder_path, completed_directory_path)
