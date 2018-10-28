import requests
from bs4 import BeautifulSoup
import re
from. import get_img_url
from. import get_product_description
from. import get_product_url
import argparse

men_category = ('jackets-coats', 'jeans', 'pants',
				'shirts', 'shorts', 'suits-blazers',
				'sweaters')
women_category = ('dresses', 'jackets-coats', 'jeans', 'jumpsuits',
				'pants', 'shorts', 'skirts', 'sweaters', 'tops')

root = 'https://www.ssense.com/en-us/'

def scrap():
	clothes = []
	index = 0
	for cat in men_category:
		cat_url = root + 'men/' + cat
		product_urls = get_product_url(cat_url)
		for product_url in product_urls:
			index += 1
			temp = []
			img_url = get_img_url(product_url)
			product_description = get_product_description(product_url)
			temp.append(index)
			temp.append(product_description[0])
			temp.append('men')
			temp.append(cat)
			temp.append(img_url)
			temp.append(product_description[1])
			clothes.append(temp)

	for cat in women_category:
		cat_url = root + 'women/' + cat
		product_urls = get_product_url(cat_url)
		for product_url in product_urls:
			index += 1
			temp = []
			img_url = get_img_url(product_url)
			product_description = get_product_description(product_url)
			temp.append(index)
			temp.append(product_description[0])
			temp.append('women')
			temp.append(cat)
			temp.append(img_url)
			temp.append(product_description[1])
			clothes.append(temp)

	return clothes

def arg():
	parser = argparse.ArgumentParser(description='save data directory')
	parser.add_argument('--csv_dir', dest = csv_dir, type=str,
                    default='/Users/evnw/Documents/GitHub/FloorDog/project316')

def save_csv(args, clothes):
	csv_path = args.csv_dir + '/' + "clothes.csv"
	with open(csv_path, 'w', newline='') as csvfile:
		writer = csv.writer(csvfile, delimiter=',')
		for cloth in clothes:
			writer.write(cloth)


if __name__ == '__main__':
	args = arg()
	clothes = scrap()














