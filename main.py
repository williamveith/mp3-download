from flask import (
    Flask,
    send_from_directory,
    request,
    redirect,
    url_for,
    render_template,
)
from app.setup import directories
from app.download_music import download_song, rewrite_metadata
from pathlib import Path
import csv

app = Flask(__name__)

UPLOAD_FOLDER = Path("app/Download List")
DOWNLOAD_FOLDER = Path("app/setup/docs")
METADATA_FOLDER = Path("app/Updated Metadata")
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["DOWNLOAD_FOLDER"] = DOWNLOAD_FOLDER
app.config["METADATA_FOLDER"] = METADATA_FOLDER


@app.route("/favicon.ico")
def favicon():
    return send_from_directory("static/images", "favicon.png", mimetype="image/x-icon")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/download-template")
def download_template():
    return send_from_directory(
        app.config["DOWNLOAD_FOLDER"], "Template Download List.csv", as_attachment=True
    )


@app.route("/upload-list", methods=["POST"])
def upload_list():
    if "file" not in request.files:
        return "No file part", 400
    file = request.files["file"]
    if file.filename == "":
        return "No selected file", 400

    if not file.filename.endswith(".csv"):
        return "Invalid file type. Please upload a CSV file.", 400

    if file:
        filepath = app.config["UPLOAD_FOLDER"] / "download-list.csv"
        file.save(str(filepath))
        download_song()
        return redirect(url_for("index"))
    
@app.route("/manual-add", methods=["GET", "POST"])
def manual_add():
    if request.method == 'POST':
        data = request.get_json()

        # Write to CSV
        csv_file_path = app.config['UPLOAD_FOLDER'] / "manual-add.csv"
        with open(csv_file_path, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            for row in data:
                writer.writerow(row)
                
        download_song()

        return redirect(url_for("index"))

    columns = ["url", "title", "author"]
    return render_template("manual-add.html", columns=columns)


@app.route("/update-metadata", methods=["POST"])
def update_metadata():
    file = request.files["file"]
    title = request.form.get("title")
    author = request.form.get("author")

    # Save the uploaded file
    filepath = app.config["METADATA_FOLDER"] / file.filename
    file.save(filepath)

    # Process the metadata with your custom function
    rewrite_metadata(filepath, title, author)

    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
