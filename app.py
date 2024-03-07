import base64
import io
from PIL import Image
import cv2
from flask import Flask, request, jsonify, send_from_directory, render_template
from werkzeug.utils import secure_filename
from flask_cors import CORS
from threading import Thread
import os
import run

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')


app.config['UPLOAD_FOLDER'] = 'C:/Users/malit/Documents/DXDY/Fonterra Web App/static/Uploads'
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB limit, for example

def save_image(image, imageName):
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], imageName)
    image.save(filepath)
    print(f"\nImage {imageName} Saved Successfully.")

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
    directory = r'static/Resources/Planograms/JSONs'
    files = [f for f in os.listdir(directory) if f.endswith('.json')]
    return jsonify(files)

@app.route('/compare2', methods=['POST'])
def compare_images2():
    return jsonify ("Hello World!")

@app.route('/compare', methods=['POST'])
def compare_images():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400
    
    image = request.files['image']
    imageName = request.form.get('imageName')
    planogramType = request.form.get('planogramType')
    
    if image.filename == '':
        return jsonify({'error': 'No selected file'})
    if image:
        # filename = secure_filename(imageName)
        # filepath = os.path.join(app.config['UPLOAD_FOLDER'], imageName)
        # image.save(filepath)
        thread = Thread(target=save_image, args=(image, imageName))
        thread.start()

        model_output = run.gold(imageName, planogramType)

        return model_output, 200
    
    else:
        return jsonify({'error': 'An error occurred'}), 500
    
@app.route('/get-json', methods=['GET'])
def get_json():
    directory = "./"  # Update this path to where your JSON file is stored
    filename = "model_output.json"  # Update this to your JSON file's name
    return send_from_directory(directory, filename, as_attachment=True)

@app.route('/update_status', methods=['POST'])
def update_status():
    data = request.get_json()
    print(data)
    return jsonify(data)
    
@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)