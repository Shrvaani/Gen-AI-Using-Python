# handlers.py

import os
import requests
from PIL import Image
from io import BytesIO
import re
import time
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
MODEL_ID = os.getenv("HF_MODEL_ID", "black-forest-labs/FLUX.1-dev")

# Folder for saving generated images
FOLDER_PATH = "media"
os.makedirs(FOLDER_PATH, exist_ok=True)


def _safe_filename(prompt: str) -> str:
    """Generate a safe filename based on the prompt."""
    safe = re.sub(r'[^A-Za-z0-9_\-\.]', '_', prompt)[:60]
    timestamp = int(time.time())
    return f"image_{safe}_{timestamp}.png"


def generate_image(prompt: str = "a white siamese cat"):
    """Generate an image using Hugging Face Inference API."""
    if not HF_TOKEN:
        raise ValueError("HF_TOKEN not found. Please set it in your .env file.")

    url = f"https://router.huggingface.co/hf-inference/models/{MODEL_ID}"
    headers = {"Authorization": f"Bearer {HF_TOKEN}"}
    payload = {"inputs": prompt, "options": {"wait_for_model": True}}

    response = requests.post(url, headers=headers, json=payload, stream=True)

    if response.status_code != 200:
        raise RuntimeError(
            f"Failed to generate image ({response.status_code}): {response.text}"
        )

    if "image" not in response.headers.get("content-type", ""):
        raise RuntimeError(f"Unexpected response: {response.text}")

    # Save image to disk
    image = Image.open(BytesIO(response.content))
    filename = _safe_filename(prompt)
    filepath = os.path.join(FOLDER_PATH, filename)
    image.save(filepath, format="PNG")
    return filepath


def get_files():
    """Return all images in the media folder."""
    files = []
    for fname in sorted(os.listdir(FOLDER_PATH), reverse=True):
        if fname.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
            files.append(
                {"file_path": os.path.join(FOLDER_PATH, fname), "title": fname}
            )
    return files
