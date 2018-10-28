import requests
from bs4 import BeautifulSoup
import re
import get_img_url
import get_product_description
import get_product_url

men_category = ('men/jackets-coats', 'men/jeans', 'men/pants',
				'men/shirts', 'men/shorts', 'men/suits-blazers',
				'men/sweaters')
women_category = ('women/dresses', 'women/jackets-coats', 'women/jeans', 'women/jumpsuits',
				'women/pants', 'women/shorts', 'women/skirts', 'women/sweaters', 'women/tops')

root = 'https://www.ssense.com/en-us/'

def scrap():
	clothes = []
	index = 0
	for cat in men_category:
		cat_url = root+cat
		product_urls = get_product_url(cat_url)
		for product_url in product_urls:
			index += 1
			temp = []
			img_url = get_img_url(product_url)
			product_description = get_product_description(product_url)
			temp.append(index)
			temp.append(product_description[0])
			temp.append('men')
			temp.append(img_url)
			temp.append(product_description[1])
			clothes.append(temp)

	for cat in women_category:
		cat_url = root+cat
		product_urls = get_product_url(cat_url)
		for product_url in product_urls:
			index += 1
			temp = []
			img_url = get_img_url(product_url)
			product_description = get_product_description(product_url)
			temp.append(index)
			temp.append(product_description[0])
			temp.append('women')
			temp.append(img_url)
			temp.append(product_description[1])
			clothes.append(temp)



if __name__ == '__main__':
	scrap()