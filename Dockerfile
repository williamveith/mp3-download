# Use an official Python runtime as a parent image
FROM python:alpine3.20

LABEL maintainer="software@williamveith.com"
LABEL description="Downloads YouTube videos as MP3 files based on a CSV list. Sets the title and artist metadata for the song"
LABEL version="1.0"
LABEL build_date="2024-10-03"
LABEL vcs-url="https://github.com/williamveith/mp3-download"
LABEL vcs-ref="49fc9669752a3b98857f853cc0b71623d8bff5d2"
LABEL org.opencontainers.image.title="mp3-download"
LABEL org.opencontainers.image.authors="software@williamveith.com"
LABEL org.opencontainers.image.documentation="https://github.com/williamveith/mp3-download/blob/main/README.md"
LABEL org.opencontainers.image.source="https://github.com/williamveith/mp3-download"
LABEL org.opencontainers.image.licenses="MIT"
LABEL org.opencontainers.image.version="1.0"
LABEL org.opencontainers.image.revision="49fc9669752a3b98857f853cc0b71623d8bff5d2"


# Set the working directory inside the container
WORKDIR /

RUN apk update && \
    apk add --no-cache ffmpeg

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "main.py"]
