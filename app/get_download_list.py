import csv
import json
from app.setup import directories, logging

# Define default values for title and author
DEFAULT_TITLE = "untitled"
DEFAULT_AUTHOR = "unknown"

# Define reusable keys
KEY_URL = "url"
KEY_TITLE = "title"
KEY_AUTHOR = "author"
KEY_DOWNLOADED = "downloaded"
KEY_TAGGED = "tagged"

def generate_object(url, title=None, author=None):
    return {
        KEY_URL: url.strip(),
        KEY_TITLE: title.strip() if title else DEFAULT_TITLE,
        KEY_AUTHOR: author.strip() if author else DEFAULT_AUTHOR,
        KEY_DOWNLOADED: False,
        KEY_TAGGED: False
    }

def get_value_from_headers(row, headers, key, default=None):
    return row[headers.index(key)] if key in headers and headers.index(key) < len(row) else default

def get_value_from_row(row, index, default=None):
    return row[index] if len(row) > index else default

def extract_data_from_csv(file_path, file_type):
    extracted_data = []
    
    try:
        with file_path.open('r') as f:
            reader = csv.reader(f)
            
            if file_type == "csv-header":
                headers = next(reader)
                for row in reader:
                    if len(row) > 0 and row[0].startswith("http"):
                        url = get_value_from_headers(row, headers, KEY_URL)
                        title = get_value_from_headers(row, headers, KEY_TITLE)
                        author = get_value_from_headers(row, headers, KEY_AUTHOR)
                        extracted_data.append(generate_object(url, title, author))
            else:
                for row in reader:
                    if len(row) > 0 and row[0].startswith("http"):
                        url = get_value_from_row(row, 0)
                        title = get_value_from_row(row, 1)
                        author = get_value_from_row(row, 2)
                        extracted_data.append(generate_object(url, title, author))
    except Exception as e:
        logging.error(f"Error reading CSV file {file_path}: {e}")
    
    return extracted_data


def extract_data_from_json(file_path):
    extracted_data = []
    
    try:
        with file_path.open('r') as f:
            data = json.load(f)
            for entry in data:
                if isinstance(entry, dict) and entry.get(KEY_URL, "").strip():
                    url = entry.get(KEY_URL, "")
                    title = entry.get(KEY_TITLE, None)
                    author = entry.get(KEY_AUTHOR, None)
                    extracted_data.append(generate_object(url, title, author))
    except Exception as e:
        logging.error(f"Error reading JSON file {file_path}: {e}")
    
    return extracted_data


def get_data_from_files(folder_path):
    if not folder_path.exists():
        logging.info(f"The specified folder '{folder_path.name}' does not exist.")
        return []

    combined_data = []
    
    for file_path in folder_path.rglob('*'):
        try:
            if file_path.suffix == '.csv':
                with file_path.open('r') as f:
                    reader = csv.reader(f)
                    first_row = next(reader)

                    if KEY_URL in first_row:
                        file_type = "csv-header"
                    else:
                        file_type = "csv-noheader"

                    combined_data.extend(extract_data_from_csv(file_path, file_type))

            elif file_path.suffix == '.json':
                combined_data.extend(extract_data_from_json(file_path))
                
        except Exception as e:
            logging.error(f"Error processing file {file_path}: {e}")
    
    return combined_data


def filter_unique_and_valid_urls(data):
    seen_urls = set()
    unique_data = []

    for entry in data:
        url = entry[KEY_URL]
        if url and url.strip() and url not in seen_urls:
            seen_urls.add(url)
            unique_data.append(entry)
    
    return unique_data

def delete_json_and_csv_files_except(folder_path, exclude_file):
    for file_path in folder_path.glob('*.json'):
        if file_path.name != exclude_file.name:
            try:
                file_path.unlink()
            except Exception as e:
                logging.error(f"Error deleting file {file_path}: {e}")
    
    for file_path in folder_path.glob('*.csv'):
        try:
            file_path.unlink()
        except Exception as e:
            logging.error(f"Error deleting file {file_path}: {e}")

def save_data_to_json(data):
    try:
        with directories['compiled_download_list'].open('w') as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        logging.error(f"Error saving data to {directories['compiled_download_list']}: {e}")
    return directories['compiled_download_list']


def compile_download_list():
    combined_data = get_data_from_files(directories['download_list_folder'])
    unique_combined_data = filter_unique_and_valid_urls(combined_data)
    if unique_combined_data:
        download_list_file = save_data_to_json(unique_combined_data)
        delete_json_and_csv_files_except(directories['download_list_folder'], download_list_file)
        return download_list_file
    else:
        logging.info("No valid data found.")
        return None

if __name__ == "__main__":
    compile_download_list()