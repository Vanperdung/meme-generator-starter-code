import os
import random
from ingestor import Ingestor, QuoteModel
from engine import MemeEngine
import argparse

def get_images_path(folder):
    """
    Get all subdirectories in the given folder that contain .jpg image files.
    """
    jpg_files = []
    
    for root, dirs, files in os.walk(folder):
        jpg_files.extend([os.path.join(root, f) for f in files if f.lower().endswith('.jpg')])
    
    return jpg_files


def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given an path and a quote """
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path[0]

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a meme by adding a quote to an image")
    parser.add_argument('--path', type=str, required=True, help="Directory containing image files")
    parser.add_argument('--body', type=str, required=True, help="Quote body to add to the image")
    parser.add_argument('--author', type=str, required=True, help="Author of the quote")
    args = parser.parse_args()
    
    if args.path:
        img_path = get_images_path(args.path)
        if not img_path:
            raise Exception(f"No .jpg files found in the directory: {args.path}")
    else:
        img_path = None
        
    print(generate_meme(img_path, args.body, args.author))
