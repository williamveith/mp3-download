# Dockerized YouTube MP3 Downloader

Downloads YouTube videos as MP3 files based on a CSV list. Sets the title and artist metadata for the song.

For docker on Linux Ubuntu, this must be run after OS restarts for docker to work

```sh
sudo sysctl -w kernel.apparmor_restrict_unprivileged_userns=0
```

## Run from Image

```sh
curl -O https://raw.githubusercontent.com/williamveith/mp3-download/refs/heads/main/docker-compose.yml
docker-compose up --build -d
```

## Build Locally & Run

```sh
git clone git@github.com:williamveith/mp3-download.git
cd mp3-download
docker-compose up --build -d
```

## Pull to Develop

```sh
git clone git@github.com:williamveith/mp3-download.git
cd mp3-download
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
deactivate
cd ..
code mp3-download
```

## Generating Deployment Key

```sh
ssh-keygen -t ed25519 -C "williamveith@gmail.com" -f ~/.ssh/id_ed25519_github_mp3-download
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519_github_mp3-download
pbcopy < ~/.ssh/id_ed25519_github_mp3-download.pub
```
