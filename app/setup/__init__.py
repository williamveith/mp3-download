from pathlib import Path
import shutil

# Get the parent directory of the current file
current_file_path = Path(__file__).resolve()
module_directory = current_file_path.parent
root_directory = module_directory.parent

# Define paths to the relevant folders
DOCS_FOLDER = module_directory / "docs"
DOWNLOAD_LIST_FOLDER = root_directory / "Download List"
OUTPUT_FOLDER = root_directory / "Downloaded Music"
TEMP_FOLDER = root_directory / "temp"

# Define paths to the relevant files
COMPILED_DOWNLOAD_LIST_FILE = DOWNLOAD_LIST_FOLDER / "Download List.json"
DOWNLOAD_PROGRESS_FILE = TEMP_FOLDER / "Download Progress.json"

# Create necessary directories if they do not exist
DOWNLOAD_LIST_FOLDER.mkdir(parents=True, exist_ok=True)
OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)
TEMP_FOLDER.mkdir(parents=True, exist_ok=True)

# Define directories as a dictionary that can be imported
directories = {
    "root_folder": root_directory,
    "download_list_folder": DOWNLOAD_LIST_FOLDER,
    "output_folder": OUTPUT_FOLDER,
    "compiled_download_list": COMPILED_DOWNLOAD_LIST_FILE,
    "temp_folder": TEMP_FOLDER,
    "download_progress": DOWNLOAD_PROGRESS_FILE
}