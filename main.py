from flask import Flask, send_from_directory, request, redirect, url_for, render_template
from app.setup import directories
from app.download_music import download_song
from pathlib import Path

app = Flask(__name__)

# Define the path where the files are located
UPLOAD_FOLDER = Path('app/Download List')
DOWNLOAD_FOLDER = Path('app/setup/docs')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER

# Limit the maximum allowed payload to 1MB
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024  # 1MB

@app.route('/')
def index():
    # Render the HTML template instead of returning raw HTML
    return render_template('index.html')

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
    
    # Ensure the file is a CSV
    if not file.filename.endswith('.csv'):
        return 'Invalid file type. Please upload a CSV file.', 400
    
    if file:
        # Use pathlib to create the file path
        filepath = app.config['UPLOAD_FOLDER'] / 'download-list.csv'
        file.save(str(filepath))  # Convert the Path object to a string for saving the file
        download_song()
        # Redirect to main page after successful upload
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
