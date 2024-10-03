from flask import Flask, send_from_directory, request
from app.setup import directories
from app.download_music import download_song
import os

app = Flask(__name__)

# Define the path where the files are located
UPLOAD_FOLDER = 'app/Download List'
DOWNLOAD_FOLDER = 'app/setup/docs'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER

@app.route('/')
def index():
    return '''
    <html>
        <body>
            <h1>File Operations</h1>
            <form action="/download-template" method="GET">
                <button type="submit">Download Template</button>
            </form>
            <br><br>
            <form action="/upload-list" method="POST" enctype="multipart/form-data">
                <input type="file" name="file">
                <button type="submit">Upload List</button>
            </form>
        </body>
    </html>
    '''

@app.route('/download-template')
def download_template():
    # Serve the CSV file from the setup/docs directory
    return send_from_directory(app.config['DOWNLOAD_FOLDER'], 'Template Download List.csv', as_attachment=True)

@app.route('/upload-list', methods=['POST'])
def upload_list():
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], 'download-list.csv')
        file.save(filepath)
        download_song()
        return f'File successfully uploaded to {filepath}'

if __name__ == '__main__':
    app.run(debug=True)
