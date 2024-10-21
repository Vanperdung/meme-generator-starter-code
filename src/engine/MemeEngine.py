"""Meme Engine is used to generate memes."""
from PIL import Image, ImageDraw, ImageFont
import os


def load_image(path):
    """Open the image path."""
    try:
        img = Image.open(path)
        return img
    except IOError:
        raise Exception(f"Cannot open image {path}")

def resize_image(img: Image, width=500):
    """Resize the image."""
    aspect_ratio = img.height / img.width
    new_height = int(width * aspect_ratio)
    resized_img = img.resize((width, new_height), Image.LANCZOS)
    return resized_img

def add_text(img: Image, text: str, author: str, font_path=None, font_size=20):
    """Add quote to the image."""
    draw = ImageDraw.Draw(img)
    try:
        if font_path:
            font = ImageFont.truetype(font_path, size=font_size)
        else:
            font = ImageFont.truetype("./_data/font/DejaVuSans-Bold.ttf", size=font_size)
    except IOError:
        raise Exception(f"Cannot load font at {font_path or './_data/font/DejaVuSans-Bold.ttf'}")
    
    text_to_be_added = f'{text}\n- {author}'
    draw.text((10, 30), text_to_be_added, font=font, fill="white")
    return img

def save_image(img: Image, output_dir: str, filename="meme.jpg"):
    """Save the meme to output directory."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    path = os.path.join(output_dir, filename)
    img.save(path)
    return path

class MemeEngine:
    """The Meme Engine Module is responsible for manipulating and drawing text onto images."""
    
    def __init__(self, output_dir: str):
        """Initialize the MemeEngine object."""
        self.output_dir = output_dir

    def make_meme(self, path, text, author, width=500) -> str:
        """Generate a meme."""
        try:
            img = load_image(path)
            img = resize_image(img, width)
            img = add_text(img, text, author)
            output_path = save_image(img, self.output_dir)
            return output_path
        except Exception as error:
            raise Exception(f"Error when creating meme: {error}")
