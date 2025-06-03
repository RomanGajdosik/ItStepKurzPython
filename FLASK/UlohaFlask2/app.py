from flask import Flask ,request ,jsonify,send_from_directory
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

upFolder = 'cloud_storage'

@app.route('/')
def index():
    return send_from_directory(upFolder, 'index2.html')
    

@app.route('/upload',methods =["POST"])
def upload_file():
    if 'file' not in request.files:
        return  jsonify({"Message":"Add file in key field "}), 400
    file = request.files['file']
    if file.filename == "":
        return jsonify({"Mssg":"No selected file"}), 400
    filename = secure_filename(file.filename)
    file.save(os.path.join(upFolder,filename))
    return jsonify({'Message':"Upload successful","filename":filename})

@app.route('/files',methods=['GET'])
def show_all_files():
    files = os.listdir(upFolder)
    return jsonify(files), 200
@app.route('/files/<fileName>',methods=['GET'])
def download_file(fileName):
    if not fileName:
        return jsonify({'ErrorMsg':'FileName is required'}), 404
    fileName = secure_filename(fileName)
    filePath = os.path.join(upFolder,fileName)
    if not os.path.exists(filePath):
        return jsonify({'ErrorMsg':'FilePath not found'}), 404
    return send_from_directory(upFolder,fileName,as_attachment=True)

if __name__ == '__main__':
    app.run()