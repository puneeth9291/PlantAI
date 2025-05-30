import torch
import torch.nn as nn
from torchvision import models
from torchvision.models import ResNet34_Weights
import torchvision.transforms as transforms
from PIL import Image
import torch.nn.functional as F
import io
import os
import requests  # Add this import for downloading the model

class Plant_Disease_Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.network = models.resnet34(weights=ResNet34_Weights.DEFAULT)
        num_ftrs = self.network.fc.in_features
        self.network.fc = nn.Linear(num_ftrs, 38)

    def forward(self, xb):
        return self.network(xb)

transform = transforms.Compose([
    transforms.Resize(size=128),
    transforms.ToTensor()
])

num_classes = [
    'Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
    'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 'Cherry_(including_sour)___healthy',
    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 'Corn_(maize)___Common_rust_',
    'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 'Grape___Black_rot',
    'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Grape___healthy',
    'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot', 'Peach___healthy',
    'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 'Potato___Early_blight',
    'Potato___Late_blight', 'Potato___healthy', 'Raspberry___healthy', 'Soybean___healthy',
    'Squash___Powdery_mildew', 'Strawberry___Leaf_scorch', 'Strawberry___healthy',
    'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold',
    'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite',
    'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus',
    'Tomato___healthy'
]

model = Plant_Disease_Model()

# Define the path where the model file should be stored
model_dir = os.path.join(os.path.dirname(__file__), '..', 'Models')
model_path = os.path.join(model_dir, 'plantDisease-resnet34.pth')

# URL to download the model file
model_url = "https://github.com/puneeth9291/PlantAI/releases/download/v1.0.0/plantDisease-resnet34.pth"

# Download the model file if it doesn't exist
if not os.path.exists(model_path):
    print(f"Downloading model file from {model_url}...")
    os.makedirs(model_dir, exist_ok=True)
    response = requests.get(model_url)
    if response.status_code == 200:
        with open(model_path, 'wb') as f:
            f.write(response.content)
        print("Model file downloaded successfully.")
    else:
        raise Exception(f"Failed to download model file from {model_url}. Status code: {response.status_code}")

# Load model
model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
model.eval()

def predict_image(img: bytes) -> str:
    # Convert bytes to PIL Image and apply transformations
    img_pil = Image.open(io.BytesIO(img))
    tensor = transform(img_pil).unsqueeze(0)

    # Make prediction
    yb = model(tensor)
    probs = F.softmax(yb, dim=1)
    confidence, preds = torch.max(probs, dim=1)

    # Set a stricter confidence threshold (increased from 0.3 to 0.5)
    if confidence.item() < 0.5:
        return "Error: Unable to identify the image. Please upload a clear image of a leaf."

    return num_classes[preds.item()]