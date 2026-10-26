import os

def check_directory_size(directory_path):
    total_size = 0
    image_total_size = 0
    
    # Tuple containing valid image extensions
    image_extensions = ('.jpg', '.jpeg', '.png', '.gif')

    print(f"Scanning directory: {directory_path}")
    print("-" * 50)
    
    try:
        # Loop through all items (files and folders) in the directory
        for filename in os.listdir(directory_path):
            # Create absolute path for the item
            file_path = os.path.join(directory_path, filename)
            
            # Check if the current item is a file (ignore sub-folders)
            if os.path.isfile(file_path):
                # Get file size in bytes
                file_size = os.path.getsize(file_path)
                total_size += file_size
                
                # Check if the filename ends with any image extension
                if filename.lower().endswith(image_extensions):
                    image_total_size += file_size
                    print(f"[Image] {filename:<20} | Size: {file_size} bytes")
                else:
                    print(f"[File]  {filename:<20} | Size: {file_size} bytes")

        print("-" * 50)
        print(f"Total size of ALL files: {total_size:,} bytes")
        print(f"Total size of IMAGE files: {image_total_size:,} bytes")
        
    except FileNotFoundError:
        print(f"Error: Directory '{directory_path}' not found.")
    except PermissionError:
        print(f"Error: Permission denied to access '{directory_path}'.")

# Get the exact directory where this python file is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# Execute the function using the current directory
check_directory_size(current_dir)