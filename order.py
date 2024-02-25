



# -----------------------------------------------------------------------------------
# Daniel T. K. W.
# GitHub: https://github.com/danieltkw
# Contact Email: danielkopolo95@gmail.com
# -----------------------------------------------------------------------------------

# ---- Imports ----
from pathlib import Path
import time
import shutil
import logging
import subprocess
import platform
# -----------------

# -----------------------------------------------------------------------------------
# Initialize logging
# -----------------------------------------------------------------------------------
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# -----------------------------------------------------------------------------------
# Variables for the source and destination folders
# -----------------------------------------------------------------------------------
# Assuming the script is located in the 'folder_org' directory.
script_directory = Path(__file__).parent
source_folder = script_directory / "folders/v1/caixa-phd"
destination_folder = script_directory / "destination/folder"

# -----------------------------------------------------------------------------------
# Function Definitions
# -----------------------------------------------------------------------------------

def clear_terminal():
    """Clears the terminal screen."""
    if platform.system() == "Windows":
        subprocess.run("cls", shell=True)
    else:
        subprocess.run("clear", shell=True)

def get_folder_size(folder_path):
    """Calculates the total size of files in a given folder."""
    total_size = sum(f.stat().st_size for f in folder_path.glob('**/*') if f.is_file())
    return total_size

def sanitize_name(name):
    """Sanitizes the file or directory name."""
    return name.lower().replace(" ", "_")

def copy_and_rename(src, dest):
    """Recursively copies and renames files and folders maintaining the structure."""
    if not dest.exists():
        dest.mkdir(parents=True, exist_ok=True)

    for item in src.iterdir():
        dest_item_path = dest / sanitize_name(item.name)
        if item.is_dir():
            logging.info(f"Processing directory: {item}")
            copy_and_rename(item, dest_item_path)  # Recursive call for subdirectories
        elif item.is_file():
            logging.info(f"Processing file: {item}")
            try:
                shutil.copy2(item, dest_item_path)
                logging.info(f"Copied and renamed: {item} -> {dest_item_path}")
            except Exception as e:
                logging.error(f"Error copying {item}: {e}")

def organize_folder():
    """Main function to organize the folder."""
    clear_terminal()
    logging.info(f"Starting the organization process.")
    start_time = time.time()

    if source_folder.exists():
        copy_and_rename(source_folder, destination_folder)
    else:
        logging.error(f"Source folder does not exist: {source_folder}")

    end_time = time.time()
    logging.info(f"Folder organization completed in {end_time - start_time:.2f} seconds.")

# -----------------------------------------------------------------------------------
# Main Execution
# -----------------------------------------------------------------------------------
if __name__ == "__main__":
    organize_folder()

# --- Code End ---






