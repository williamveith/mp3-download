# YouTube MP3 Downloader

Downloads YouTube videos as MP3 files based on a CSV list. Sets the title and artist metadata for the song

## Quick Setup

```sh
git clone https://github.com/williamveith/mp3-download.git
cd mp3-download
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app/setup/__init__.py
open app/Download\ List/Template\ Download\ List.csv
```

### Update CSV with url, title, and author for each song. Save As using a new file name

```sh
python app/main.py
```

## Explanation

### Clone Project

```sh
git clone https://github.com/williamveith/mp3-download.git
cd mp3-download
```

### Set up project

```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app/setup/__init__.py
```

### Update Download List

At the url, title, and author for each desired download here [Download Template List](./app/Download%20List/Template%20Download%20List.csv)

Save As with a new file name

### Run Project

```sh
python app/main.py
```
