



import os
from bs4 import BeautifulSoup
from flask import Flask, render_template
import requests


def rgif():
    url = "https://www.generatormix.com/random-gif-generator?safe="

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    gif_element = soup.find('div', class_='thumbnail-col-1')

    link = soup.find('img', class_='lazy thumbnail')

    src_content = link['data-src']

    return src_content

app = Flask(__name__)

@app.route('/')
def display_random_gif():
    gif_url = rgif()  # Appelez votre fonction rgif() pour obtenir le lien du GIF aléatoire
    return render_template('index.html', gif_url=gif_url)

if __name__ == '__main__':
    app.run(debug=True)
