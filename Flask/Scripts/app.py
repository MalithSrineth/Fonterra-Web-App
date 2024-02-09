from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from flask_cors import CORS
import os
import run

app = Flask(__name__)
CORS(app)

app.config['UPLOAD_FOLDER'] = 'C:/Users/malit/Documents/DXDY/Fonterra Web App/Flask/Uploads'
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB limit, for example

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'})
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    if file:
        filename = secure_filename(file.filename)
        print(filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        # You can now use the filepath or any other operations
        return jsonify({'message': 'File uploaded successfully', 'filepath': filepath})
    
@app.route('/get-json-files', methods=['GET'])
def get_json_files():
    directory = r'../../Resources/Planograms/JSONs'
    files = [f for f in os.listdir(directory) if f.endswith('.json')]
    return jsonify(files)

@app.route('/compare', methods=['POST', 'GET'])
def compare_images():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400
    
    image = request.files['image']
    imageName = request.form.get('imageName')
    planogramType = request.form.get('planogramType')
    
    if image.filename == '':
        return jsonify({'error': 'No selected file'})
    if image:
        filename = secure_filename(imageName)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        image.save(filepath)

        model_output = run.gold(filename, planogramType)
        # print(model_output)
        return jsonify(model_output), 200
    
    else:
        return jsonify({'error': 'An error occurred'}), 500
    
@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)