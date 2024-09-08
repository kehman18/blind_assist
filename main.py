from flask import Flask, request, jsonify, send_from_directory
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import io

app = Flask(__name__)

# Load the BLIP model and processor for image captioning
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        # Open and preprocess the image
        image = Image.open(io.BytesIO(file.read())).convert("RGB")
        inputs = processor(images=image, return_tensors="pt")

        # Generate description
        outputs = model.generate(**inputs)
        description = processor.decode(outputs[0], skip_special_tokens=True)

        return jsonify({'description': description}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
