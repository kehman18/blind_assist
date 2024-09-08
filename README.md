# Professional Camera Web App for the Visually Impaired

## Description

This is a **web-based camera application** designed specifically for visually impaired or blind individuals. The application allows users to interact with their device’s camera by using simple gestures such as **single-tap** and **double-tap**:
- **Single-tap**: Captures an image from the device camera.
- **Double-tap**: Switches between the front and rear cameras.

Once an image is captured, the application provides a **description** of the captured image using **text-to-speech (TTS)** and displays the description on the screen. After reading out the description, the user is automatically returned to the camera view to capture more images if desired.

## Features

- **Single-Tap Image Capture**: Users can capture an image by simply tapping the screen once.
- **Double-Tap Camera Switch**: Double-tapping switches between the front and rear cameras (user-facing and environment-facing).
- **Image Description**: The app uses a server-based API to generate an image description, which is spoken out loud to the user and displayed on the screen.
- **Text-to-Speech (TTS)**: The app speaks out the description of the captured image for the user.
- **Responsive and Accessible UI**: The app is designed to be responsive, fully accessible, and centered on the screen for ease of use.

## Technologies Used

### Frontend
- **HTML5**: Markup for the web interface.
- **CSS3**: Styling and layout for responsiveness and accessibility.
- **JavaScript**: Handling user gestures (single-tap, double-tap), camera operations, and TTS functionalities.

### Backend
- **Flask (Python)**: A lightweight backend framework for handling image uploads and generating image descriptions.
- **Transformers (Hugging Face)**: The app uses the **BLIP Image Captioning Model** to generate image descriptions based on the captured image.
- **PIL (Python Imaging Library)**: Used to process images before sending them to the image captioning model.

## How It Works

1. **Camera Initialization**: The camera starts with the environment-facing camera by default. The user can switch to the user-facing camera with a double-tap gesture.
2. **Single Tap**: When the user taps the screen once, the app captures an image and displays it in a popup.
3. **Image Description**: The captured image is sent to a Flask server where an image captioning model generates a description. The description is returned to the frontend, displayed on the screen, and spoken out loud using the TTS engine.
4. **Return to Camera**: Once the description is read aloud, the popup closes, and the user is returned to the camera interface for further interaction.

## Project Setup and Installation

### Prerequisites

- Python 3.x
- Node.js (for serving static assets)
- Flask and required Python packages
- Browser supporting WebRTC API (Google Chrome, Mozilla Firefox, etc.)

### Backend Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/kehman18/professional-camera-app.git
    cd professional-camera-app
    ```

2. Install Python dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Start the Flask server:
    ```bash
    python app.py or flask --app main run --debug --port 5000 (you can choose to change the port if need be)
    ```

### Frontend Setup

1. Open `index.html` in your preferred browser, or host it on a web server.

2. Ensure your device has access to the camera and microphone, and grant permissions when prompted.

## Usage

- **Single Tap**: To capture an image, simply tap anywhere on the screen once. The image will be captured and the description will be read aloud.
- **Double Tap**: To switch cameras (front/rear), double-tap anywhere on the screen.
- **Automatic Return**: After the description is read aloud, the app automatically returns to the camera view, allowing you to capture another image.

## Customization

### Customizing Text-to-Speech (TTS)
The TTS engine is currently set to use the `en-US` locale. You can modify the language and other TTS parameters by adjusting the `speakDescription` function in the `index.html` file.

### Customizing Camera Modes
You can modify the initial camera mode (default: `environment`) or add additional camera-related features in the `startCamera` function.

## Known Issues and Limitations

- **Browser Compatibility**: The app relies on the WebRTC API for accessing device cameras. It may not work in older browsers or in some mobile browsers.
- **Image Processing Speed**: The speed of generating image descriptions depends on server performance and internet connectivity.
- **Offline Mode**: The app requires an internet connection to generate image descriptions.

## Future Enhancements

- **Improved Accessibility**: Implement voice commands for easier navigation.
- **Offline Mode**: Allow capturing images and providing basic descriptions without internet access.
- **Language Support**: Add multi-language support for text-to-speech and image descriptions.

## Contributing

Contributions to improve this project are welcome. To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix:
    ```bash
    git checkout -b feature-branch-name
    ```
3. Commit your changes and push the branch to your fork:
    ```bash
    git commit -m "Description of changes"
    git push origin feature-branch-name
    ```
4. Submit a pull request describing your changes.

## Contact

For any questions or suggestions, feel free to reach out:
- Email: [youremail@example.com](mailto:kehindeadekola96@gmail.com)
- GitHub: [yourusername](https://github.com/kehman18)
