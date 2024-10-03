# Dockerized YouTube MP3 Downloader

Downloads YouTube videos as MP3 files based on a CSV list. Sets the title and artist metadata for the song.

For docker on Linux Ubuntu, this must be run after OS restarts for docker to work

```sh
sudo sysctl -w kernel.apparmor_restrict_unprivileged_userns=0
```

## Build to Run
```sh
git clone https://github.com/williamveith/mp3-download.git
cd mp3-download
git checkout 4f4dfd7
docker-compose up --build -d
```

## Pull to Develop
```sh
git clone https://github.com/williamveith/mp3-download.git
cd mp3-download
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
deactivate
cd ..
code mp3-download
```
