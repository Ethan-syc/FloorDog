import requests
from bs4 import BeautifulSoup
import re
from scrapping_tools import scrapping_tools


if __name__ == '__main__':

    product_url="https://www.ssense.com/en-us/women/product/maison-margiela/red-knit-turtleneck-dress/3042348"
    temp = []
    try:
        img_url = scrapping_tools.get_img_url(product_url)
        print(img_url)
    except:
        print("cannot find image url: index-{}, product_url: {}".format(index, product_url))
    try:
        product_description = scrapping_tools.get_product_description(product_url)
        print(product_description)
    except:
        print("cannot find description: index-{}, product_url: {}".format(index, product_url))
        product_description=['null','null','null']

    temp.append(product_url)
    temp.append(product_description[0])
    temp.append('men')
    temp.append(img_url)
    temp.append(product_description[1])
    temp.append(product_description[2])
    print(temp)