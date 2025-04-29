import os
import shutil

# download data from https://www.robots.ox.ac.uk/~vgg/data/pets/ and call the folder images

# Directory containing all images
source_dir = 'images'

# Target directory where organized subfolders will be created
target_dir = 'organized_images'

# Create target directory if it doesn't exist
if not os.path.exists(target_dir):
    os.makedirs(target_dir)

# Loop over all files in the source directory
for filename in os.listdir(source_dir):
    if filename.lower().endswith('.jpg'):
        # Extract the breed name from the filename (assuming format 'BreedName_#.jpg')
        breed = filename.split('_')[0]
        
        # Create a subfolder for the breed if it doesn't exist
        breed_folder = os.path.join(target_dir, breed)
        if not os.path.exists(breed_folder):
            os.makedirs(breed_folder)
        
        # Define source and destination file paths
        src_path = os.path.join(source_dir, filename)
        dst_path = os.path.join(breed_folder, filename)
        
        # Move the image to the corresponding breed folder
        shutil.move(src_path, dst_path)
        print(f"Moved {filename} to {breed_folder}")

print("Images have been organized into subfolders.")
