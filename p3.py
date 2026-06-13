import os
import shutil

source = "source_folder"
destination = "destination_folder"

if not os.path.exists(destination):
    os.makedirs(destination)

for file in os.listdir(source):
    src_path = os.path.join(source, file)
    dest_path = os.path.join(destination, file)

    if os.path.isfile(src_path):
        shutil.move(src_path, dest_path)

print("All files moved successfully!")