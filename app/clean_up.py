import json
import shutil
from app.setup import directories, logging

def clean_completed_files():
    try:
        with directories['download_progress'].open('r') as f:
            data = json.load(f)

        filtered_data = [entry for entry in data if entry.get("downloaded") == False and entry.get("tagged") == False]

        if filtered_data:
            with directories['download_progress'].open('w') as f:
                json.dump(filtered_data, f, indent=4)
            logging.info(f"{directories['download_progress'].name} contains {len(filtered_data)} entries that were not completed")
        else:
            shutil.rmtree(directories['temp_folder'])
            shutil.rmtree(directories['download_list_folder'])

    except Exception as e:
        logging.error(f"An error occurred while processing the temp file: {e}")
