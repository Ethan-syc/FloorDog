import requests
from bs4 import BeautifulSoup
import re


def get_comb_url(product_url):
    s = requests.session()
    p = requests.get(product_url)
    soup = BeautifulSoup(p.content, "html.parser")
    other = soup.find_all("div", class_ = 'tab-pane span16 tab-content vspace2')
    comb = other[2].find_all("a")
    url = re.findall(r"href=\".*?\"", str(comb))
    print(url)


if __name__ == '__main__':
    product_url = 'https://www.ssense.com/en-us/men/product/opening-ceremony/black-elliptical-souvenir-shirt/3390929'
    get_comb_url(product_url)