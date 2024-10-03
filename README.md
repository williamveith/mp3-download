# Dockerized YouTube MP3 Downloader

Downloads YouTube videos as MP3 files based on a CSV list. Sets the title and artist metadata for the song.

For docker on Linux Ubuntu, this must be run after OS restarts for docker to work

```sh
sudo sysctl -w kernel.apparmor_restrict_unprivileged_userns=0
```

## Quick Setup

```sh
git clone https://github.com/williamveith/mp3-download.git
cd mp3-download
git checkout 4f4dfd7
docker-compose up --build -d
```

## Explanation

### Clone Project from specific commit

```sh
git clone https://github.com/williamveith/mp3-download.git
cd mp3-download
git checkout 4f4dfd7
```

### Build Image and Start Container

```sh
docker-compose up --build -d
```
