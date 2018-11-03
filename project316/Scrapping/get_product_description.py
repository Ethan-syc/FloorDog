import requests
from bs4 import BeautifulSoup
import re


def get_product_des(product_url):
    s = requests.session()
    p = requests.get(product_url)
    soup = BeautifulSoup(p.content, "html.parser")
    html_str = str(soup.prettify())
    title_str = re.findall(r"content=.*twitter\:title", html_str)[0]
    des_str = re.findall(r"content=.*twitter\:description", html_str)[0]
    mat_str = re.findall(r"composition\"\:\".*?\"", html_str)[0]
    title = re.sub(r"content=\"", "", title_str)
    title = re.sub(r"\".*", "", title)
    title = re.sub(r".* - ", "", title)
    des = re.sub(r"content=\"", "", des_str)
    des = re.sub(r"\".*", "", des)
    mat = re.sub(r"composition\"\:\"", "", mat_str)
    mat = re.sub(r"\"", "", mat)
    return title, des, mat
