from rembg import remove
from PIL import Image
import io

def remove_background(input_path, output_path):
    with open(input_path, "rb") as i:
        input_bytes = i.read()
        output_bytes = remove(input_bytes)
    output_image = Image.open(io.BytesIO(output_bytes)).convert("RGBA")
    output_image.save(output_path, format="PNG")
