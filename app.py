from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf
import keras
from PIL import Image
import io

# Initialize Flask app
app = Flask(__name__)

# Load trained model
model = keras.models.load_model("HDR_model.h5")

# Define a route for digit prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get image from request
        file = request.files['file']
        image = Image.open(file).convert('L')  # Convert to grayscale
        image = image.resize((28, 28))  # Resize to 28x28
        image = np.array(image) / 255.0  # Normalize
        image = image.reshape(1, 28, 28)  # Reshape for model input

        # Predict
        prediction = model.predict(image)
        predicted_digit = np.argmax(prediction)

        return jsonify({'digit': int(predicted_digit)})
    except Exception as e:
        return jsonify({'error': str(e)})

# Run Flask app
if __name__ == '__main__':
    app.run(debug=True)

