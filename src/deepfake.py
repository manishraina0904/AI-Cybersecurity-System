import cv2
import numpy as np

def detect_deepfake(image_path):
    image = cv2.imread(image_path)
    
    if image is None:
        return "Invalid Image"

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Simple variance check (blur detection)
    variance = cv2.Laplacian(gray, cv2.CV_64F).var()

    if variance < 50:
        return "Possibly Fake (Low detail / blurred)"
    else:
        return "Likely Real"