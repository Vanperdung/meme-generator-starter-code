import random
import os
import requests
from flask import Flask, render_template, abort, request
from ingestor import Ingestor
from engine import MemeEngine
import tempfile

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']
    quotes = []
    
    for quote_file in quote_files:
        try:
            parsed_quotes = Ingestor.parse(quote_file)
            quotes.extend(parsed_quotes) 
        except ValueError as error:
            print(f"Error parsing {quote_file}: {error}")
    
    images_path = "./_data/photos/dog/"
    imgs = []

    for filename in os.listdir(images_path):
        file_path = os.path.join(images_path, filename)
        imgs.append(file_path)

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    # @TODO:
    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    # 3. Remove the temporary saved image.

    image_url = request.form['image_url']
    body = request.form['body']
    author = request.form['author']
    
    try:
        response = requests.get(image_url)
        response.raise_for_status()
        
        temp_img = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
        temp_img.write(response.content)
        temp_img.close()
        
        meme = MemeEngine('./static')
        path = meme.make_meme(temp_img.name, body, author)
        
        os.remove(temp_img.name)
    except requests.exceptions.RequestException as e:
        print(f"Error downloading image: {e}")
        return "Error downloading image", 400
    except Exception as e:
        print(f"Error creating meme: {e}")
        return "Error creating meme", 500

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
