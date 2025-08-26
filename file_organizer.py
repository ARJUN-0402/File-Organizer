import os
import shutil

def organize_files(directory):
    """
    Organize files in the given directory by their extension.
    
    Args:
        directory (str): Path to the directory to organize
    """
    # Check if directory exists
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return
    
    # Check if directory is actually a directory
    if not os.path.isdir(directory):
        print(f"Error: '{directory}' is not a directory.")
        return
    
    # Get all items in the directory
    items = os.listdir(directory)
    
    # Counter for moved files
    moved_files = 0
    
    # Process each item in the directory
    for item in items:
        item_path = os.path.join(directory, item)
        
        # Skip directories, only process files
        if os.path.isfile(item_path):
            # Get file extension (without the dot)
            _, extension = os.path.splitext(item)
            extension = extension[1:].lower()  # Remove the dot and convert to lowercase
            
            # If file has no extension, put it in "no_extension" folder
            if not extension:
                extension = "no_extension"
            
            # Create folder for this extension if it doesn't exist
            extension_folder = os.path.join(directory, extension)
            if not os.path.exists(extension_folder):
                os.makedirs(extension_folder)
                print(f"Created folder: {extension}")
            
            # Move file to its extension folder
            destination = os.path.join(extension_folder, item)
            
            # Check if file already exists in destination
            if os.path.exists(destination):
                print(f"File {item} already exists in {extension} folder. Skipping.")
                continue
            
            # Move the file
            shutil.move(item_path, destination)
            print(f"Moved: {item} -> {extension}/")
            moved_files += 1
    
    print(f"\nOrganization complete! {moved_files} files organized.")

def main():
    """
    Main function to run the file organizer.
    """
    print("File Organizer")
    print("=" * 20)
    
    # Get directory from user
    directory = input("Enter the path to the directory you want to organize: ").strip()
    
    # Organize files
    organize_files(directory)

if __name__ == "__main__":
    main()