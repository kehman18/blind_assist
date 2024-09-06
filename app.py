from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import os
import torch
from torchvision import transforms
from PIL import Image
from gtts import gTTS
from transformers import VisionEncoderDecoderModel, ViTFeatureExtractor, AutoTokenizer
import io
import base64

# Initialize Flask app
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Load the pre-trained image captioning model (e.g., from a library like Hugging Face)
# This is an example of how you might load a transformer-based model for captioning
 
model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
feature_extractor = ViTFeatureExtractor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")

# Preprocessing pipeline for the images
def preprocess_image(image_path):
    image = Image.open(image_path)
    pixel_values = feature_extractor(images=image, return_tensors="pt").pixel_values
    return pixel_values

# Generate caption
def generate_caption(image_path):
    pixel_values = preprocess_image(image_path)
    output_ids = model.generate(pixel_values)
    caption = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    return caption

# Convert text to speech
def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    fp = io.BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    return base64.b64encode(fp.read()).decode('ascii')

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Capture and process image
@app.route('/capture', methods=['POST'])
def capture():
    data_url = request.json['image']
    header, encoded = data_url.split(",", 1)
    data = base64.b64decode(encoded)
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], 'captured_image.png')
    with open(image_path, "wb") as f:
        f.write(data)
    
    # Generate the caption
    caption = generate_caption(image_path)
    
    # Convert the caption to speech
    speech = text_to_speech(caption)
    
    return jsonify({'caption': caption, 'speech': speech})

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
