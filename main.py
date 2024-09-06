from flask import Flask, request, jsonify, send_from_directory
from transformers import AutoModelForCausalLM, AutoTokenizer
from PIL import Image
import io
import os

app = Flask(__name__)

# Load the model and tokenizer
model_id = "vikhyatk/moondream2"
revision = "2024-08-26"
model = AutoModelForCausalLM.from_pretrained(
    model_id, trust_remote_code=True, revision=revision
)
tokenizer = AutoTokenizer.from_pretrained(model_id, revision=revision)

@app.route('/upload', methods=['POST'])
def upload_image():
    print(request)
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        # Open the image
        image = Image.open(io.BytesIO(file.read()))
        print(image)
        # Encode and process the image
        enc_image = model.encode_image(image)
        print("am here")
        description = model.answer_question(enc_image, "Describe this image.", tokenizer)
        print("am here")
        return jsonify({'description': description}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
