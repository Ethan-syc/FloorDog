import requests
from bs4 import BeautifulSoup
import re
from scrapping_tools import scrapping_tools
import argparse
import csv

men_category = ('jackets-coats', 'jeans', 'pants',
				'shirts', 'shorts', 'suits-blazers',
				'sweaters')
women_category = ('dresses', 'jackets-coats', 'jeans', 'jumpsuits',
				'pants', 'shorts', 'skirts', 'sweaters', 'tops')

root = 'https://www.ssense.com'

def scrap(args):
	csv_path = args.csv_dir + '/' + "clothes.csv"
	with open(csv_path, 'w', newline='') as csvfile:
		writer = csv.writer(csvfile, delimiter=',')

		index = 0
		for cat in men_category:
			cat_url = root + '/en-us/' + 'men/' + cat
			product_urls = scrapping_tools.get_product_url(cat_url)
			for product_url in product_urls:
				product_url = root + product_url
				index += 1
				temp = []
				img_url = scrapping_tools.get_img_url(product_url)
				product_description = scrapping_tools.get_product_description(product_url)
				temp.append(index)
				temp.append(product_description[0])
				temp.append('men')
				temp.append(cat)
				temp.append(img_url)
				temp.append(product_description[1])
				print(product_url)
				writer.writerow(temp)

		for cat in women_category:
			cat_url = root + '/en-us/' + 'women/' + cat
			product_urls = scrapping_tools.get_product_url(cat_url)
			for product_url in product_urls:
				product_url = root + product_url
				index += 1
				temp = []
				img_url = scrapping_tools.get_img_url(product_url)
				product_description = scrapping_tools.get_product_description(product_url)
				temp.append(index)
				temp.append(product_description[0])
				temp.append('women')
				temp.append(cat)
				temp.append(img_url)
				temp.append(product_description[1])
				print(product_url)
				writer.writerow(temp)


def arg():
	parser = argparse.ArgumentParser(description='save data directory')
	parser.add_argument('--csv_dir', dest = 'csv_dir', type=str,
                    default='/Users/evnw/Documents/GitHub/FloorDog/project316')
	args = parser.parse_args()
	return args


if __name__ == '__main__':
	args = arg()
	clothes = scrap(args)














