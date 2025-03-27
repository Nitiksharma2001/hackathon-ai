import base64, json, requests
import numpy as np
import io, os
from PIL import Image

# Databricks Model Serving Endpoint URL
DATABRICKS_MODEL_URL = os.getenv('DATABRICKS_MODEL_URL')
# Databricks Access Token (Replace with your actual token)
DATABRICKS_ACCESS_TOKEN = os.getenv('DATABRICKS_ACCESS_TOKEN')

def preprocess_image(contents):
    """ Convert uploaded image to a format compatible with the model """
    content_type, content_string = contents.split(',')
    
    decoded = base64.b64decode(content_string)
    
    # Open the image using PIL and convert to RGB
    image = Image.open(io.BytesIO(decoded)).convert("RGB")  

    # Resize to match model's expected input size (256x256)
    image = image.resize((224, 224))

    # Convert to NumPy array and normalize to [0,1]
    img_array = np.array(image) / 255.0  

    # Ensure correct shape: (1, 256, 256, 3)
    img_array = np.expand_dims(img_array, axis=0)

    return img_array.tolist()

def is_image_AI(contents):
    """
    Send the processed image to the Databricks Model Serving API for prediction.
    """
    image_data = preprocess_image(contents)

    headers = {
        "Authorization": f"Bearer {DATABRICKS_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "inputs": image_data
    }

    response = requests.post(DATABRICKS_MODEL_URL, headers=headers, data=json.dumps(payload))
    if response.status_code == 200:
        prediction = response.json()  # Parse response JSON
        return prediction['predictions'][0][0] <= 0.5
    else:
        return {"error": "Failed to get prediction", "details": response.text}