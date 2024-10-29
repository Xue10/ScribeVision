from pdf2image import convert_from_path
from PIL import Image
import numpy as np
import io
import base64

def convert_pdf_to_images(pdf_path):
    """Convert PDF to list of images."""
    return convert_from_path(pdf_path)

def trim_whitespace(image):
    """Remove excess whitespace from image."""
    # Convert to numpy array
    img_array = np.array(image)
    # Get non-empty pixels
    coords = np.argwhere(img_array.sum(axis=2) < 255 * 3)
    y_min, x_min = coords.min(axis=0)
    y_max, x_max = coords.max(axis=0)
    # Crop image
    return image.crop((x_min, y_min, x_max, y_max))

def encode_image(image):
    """Convert PIL image to base64 string."""
    buffer = io.BytesIO()
    image.save(buffer, format="JPEG")
    return base64.b64encode(buffer.getvalue()).decode('utf-8') 