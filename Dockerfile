# Use an official Python runtime as a parent image
FROM python:alpine3.20

# Set the working directory inside the container
WORKDIR /

RUN apk update && \
    apk add --no-cache ffmpeg

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_ENV=development

# Make port 5001 available to the world outside this container
EXPOSE 5001

VOLUME ["/app/Downloaded Music"]

# Run app.py when the container launches
CMD ["python", "main.py"]
