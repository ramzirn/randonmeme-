from bs4 import BeautifulSoup
from requests import request
import requests


def rgif():
    url = "https://www.generatormix.com/random-gif-generator?safe="

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    gif_element = soup.find('div', class_='thumbnail-col-1')

    link = soup.find('img', class_='lazy thumbnail')

    src_content = link['data-src']

    return src_content


message = rgif ()
print(message )