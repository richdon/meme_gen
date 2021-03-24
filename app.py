import random
import os
import requests
from flask import Flask, render_template, request

# @TODO Import your Ingestor and MemeEngine fromn
from MemeEngine import MemeEngine
from QuoteEngine import Ingestor

app = Flask(__name__, template_folder='./templates')

meme = MemeEngine('./tmp/url_imgs')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    
    for file in quote_files:
        quotes.extend(Ingestor.parse(file))
    
    images_path = "./_data/photos/"

    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]
    
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
   
    img = request.form['image_url']
    body = request.form['body']
    author = request.form['author']

    r = requests.get(img)
    tmp_img = './tmp/url_imgs/tmp_img.jpg'
    with open(tmp_img, 'wb') as f:
       f.write(r.content)

    tmp_txt = './tmp/quotes/tmp_txt.txt'
    with open(tmp_txt, 'w') as f:
        f.write(f'{body} - {author}')

   
    quote = Ingestor.parse(tmp_txt)[0]
    body = quote.body
    author = quote.author

    path = meme.make_meme(tmp_img, body, author)

    os.remove(tmp_img)
    os.remove(tmp_txt)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
