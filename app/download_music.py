import json
import yt_dlp
from mutagen.easyid3 import EasyID3
from app.setup import directories
from app.get_download_list import compile_download_list
from app.clean_up import clean_completed_files

def set_mp3_metadata(entry):
    try:
        audio = EasyID3(entry["downloaded"])
        audio['title'] = entry["title"]
        audio['artist'] = entry["author"]
        audio.save()
        return True
    except Exception as e:
        print(f"Error setting metadata for {entry['downloaded']}: {e}")
        return False

def download_audio(entry):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': str(directories["output_folder"] / f"{entry['title']}.%(ext)s"),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(entry['url'], download=True)
        file_path = directories["output_folder"] / f"{entry['title']}.mp3"
        return file_path

def process_json_file(json_file):
    try:
        with json_file.open('r') as f:
            data = json.load(f)

        for entry in data:
            if not entry.get("downloaded"):
                print(f"Downloading {entry['title']} by {entry['author']}")
                try:
                    file_path = download_audio(entry)
                    entry['downloaded'] = str(file_path)
                    print(f"Successfully downloaded to {file_path}")

                    with directories["download_progress"].open('w') as f:
                        json.dump(data, f, indent=4)

                    if set_mp3_metadata(entry):
                        entry['tagged'] = True
                        print(f"Successfully set title and artist for {entry['downloaded']}")

                        with directories["download_progress"].open('w') as f:
                            json.dump(data, f, indent=4)
                    else:
                        print(f"Error setting metadata for {entry['downloaded']}")

                except Exception as e:
                    print(f"Failed to download {entry['title']}: {e}")
            else:
                print(f"Already downloaded: {entry['downloaded']}")

    except Exception as e:
        print(f"An error occurred while processing the JSON file: {e}")

def download_song():
    download_list = compile_download_list()
    process_json_file(download_list)
    clean_completed_files()

