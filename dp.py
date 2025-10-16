from flask import Flask, request
import dropbox


app = Flask(__name__)


dbx = dropbox.Dropbox("")




@app.route("/", methods=["GET"])
def index():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Upload to Dropbox</title>
    </head>
    <body>
        <h2>Upload Image to Dropbox</h2>
        <form method="POST" enctype="multipart/form-data" action="/upload">
            <input type="file" name="file" required>
            <button type="submit">Upload</button>
        </form>
    </body>
    </html>
    '''




@app.route("/upload", methods=["POST"])
def upload():
    file = request.files.get("file")
    if not file:
        return "No file uploaded", 400
    
    path = "/" + file.filename
    dbx.files_upload(file.read(), path, mode=dropbox.files.WriteMode.overwrite)
    link = dbx.files_get_temporary_link(path).link


    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Upload Result</title>
    </head>
    <body>
        <h2>Uploaded Successfully ✅</h2>
        <p><b>File:</b> {file.filename}</p>
        <img src="{link}" style="max-width:300px;" />
        <p><a href="{link}" target="_blank">Open Image</a></p>
        <a href="/">⬅ Upload Another</a>
    </body>
    </html>
    '''




if __name__ == "__main__":
    app.run(debug=True)
