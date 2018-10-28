import requests
from bs4 import BeautifulSoup
import re


def get_product_url(category_url: str) -> list:
    p = requests.get(category_url)
    soup = BeautifulSoup(p.content, "html.parser")
    urls = soup.find_all("a")
    res_url = []
    for url in urls:
        href = url.get("href")
        if re.search(r"product", href):
            res_url.append(href)
    return res_url

