from flask import Flask, send_from_directory, request, redirect, url_for, render_template, Response
from app.setup import directories
from app.download_music import download_song
from pathlib import Path

app = Flask(__name__)

UPLOAD_FOLDER = Path('app/Download List')
DOWNLOAD_FOLDER = Path('app/setup/docs')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER

app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024  # 1MB

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download-template')
def download_template():
    return send_from_directory(app.config['DOWNLOAD_FOLDER'], 'Template Download List.csv', as_attachment=True)

@app.route('/upload-list', methods=['POST'])
def upload_list():
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    
    if not file.filename.endswith('.csv'):
        return 'Invalid file type. Please upload a CSV file.', 400
    
    if file:
        filepath = app.config['UPLOAD_FOLDER'] / 'download-list.csv'
        file.save(str(filepath))
        download_song()
        return redirect(url_for('index'))
    
@app.route('/log')
def display_log():
    def generate():
        with directories["log_file"].open('r') as log_file:  # Use `open()` method to read the file
            while True:
                line = log_file.readline()
                if not line:
                    break
                yield line.replace("\n", "<br>\n")  # Convert newlines to HTML line breaks

    return Response(generate(), mimetype='text/html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
