# Dockerized YouTube MP3 Downloader

Downloads YouTube videos as MP3 files based on a CSV list. Sets the title and artist metadata for the song

## Quick Setup

```sh
git clone https://github.com/williamveith/mp3-download.git
cd mp3-download
git checkout d91596b
docker-compose up --build -d
```

## Explanation

### Clone Project

```sh
git clone https://github.com/williamveith/mp3-download.git
cd mp3-download
```

### Build Image and Start Container

```sh
docker-compose up --build -d
```
