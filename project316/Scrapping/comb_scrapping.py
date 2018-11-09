import requests
from bs4 import BeautifulSoup
import re
from scrapping_tools import scrapping_tools
import argparse
import csv, os

men_category = ('jackets-coats', 'jeans', 'pants',
				'shirts', 'shorts', 'suits-blazers',
				'sweaters')
women_category = ('dresses', 'jackets-coats', 'jeans', 'jumpsuits',
				'pants', 'shorts', 'skirts', 'sweaters', 'tops')

men_cat_dict = {'jackets-coats': set([]), 'jeans': set([]), 'pants': set([]), 'shirts': set([]), 'shorts': set([]), 'suits-blazers': set([]), 'sweaters': set([])}
women_cat_dict = {'dresses': set([]), 'jackets-coats': set([]), 'jeans': set([]), 'jumpsuits': set([]), 'pants': set([]), 'shorts': set([]), 'skirts': set([]), 'sweaters': set([]), 'tops': set([])}

category = {'men': men_category, 'women': women_category}
category_dict = {'men': men_cat_dict, 'women': women_cat_dict}

def arg():
	parser = argparse.ArgumentParser(description='save data directory')
	parser.add_argument('--csv_dir', dest = 'csv_dir', type=str,
                    default='/Users/evnw/Documents/GitHub/FloorDog/project316')
	parser.add_argument('--category_dict_path', dest = 'cat_dict_path', type = str,
					default = '/Users/evnw/Documents/GitHub/FloorDog/project316/cat_dict.csv')
	args = parser.parse_args()
	return args



def initialize(args, gender):
	csv_path = os.path.join(args.csv_dir, gender+'_clothes_comb.csv')
	product_url_dict = {}
	product_url_set = set([])
	comb_url_set = set([])
	max_index = 0

	with open(csv_path, 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter = ',')
		for row in reader:
			index = int(row[0])
			product_url = row[1]
			comb_urls = row[8:]
			product_url_dict[product_url] = index
			product_url_set.add(product_url)
			for url in comb_urls:
				comb_url_set.add(url)
			if index>max_index:
				max_index = index
	return product_url_set, product_url_dict, comb_url_set, max_index



def comb_scrapping(args, gender):
	csv_path = os.path.join(args.csv_dir, gender+'_clothes_comb copy.csv')
	product_url_set, product_url_dict, comb_url_set, max_index = initialize(args, gender)
	index = max_index
	url_queue = []
	for url in comb_url_set:
		url_queue.append(url)

	with open(csv_path, 'a', newline = '') as csvfile:
		writer = csv.writer(csvfile, delimiter = ',')
		while(len(url_queue) > 0):
			product_url = url_queue.pop()
			product_url = re.findall(r"\".*\"", product_url)[0]
			product_url = product_url[1:-1]
			product_url = 'http://www.ssense.com' + product_url

			if product_url in product_url_set:
				continue

			product_url_set.add(product_url)

			cat = re.findall(r"-.*?/[0-9]", product_url)[0]
			cat = re.sub(r"-.*-", '', cat)
			cat = re.sub(r"/[0-9]", '', cat)

			unconsidered_cat = True
			for key in category_dict[gender].keys():
				if cat in category_dict[gender][key]:
					unconsidered_cat = False

			if unconsidered_cat:
				continue

			index = index + 1
			temp = []
			
			try:
				img_url = scrapping_tools.get_img_url(product_url)
			except:
				print("cannot find image url: index-{}, product_url: {}".format(index, product_url))
				img_url = 'null'

			try:
				product_description = scrapping_tools.get_product_description(product_url)
			except:
				print("cannot find description: index-{}, product_url: {}".format(index, product_url))
				product_description=['null','null','null']

			try:
				comb_url = scrapping_tools.get_comb_url(product_url)
			except:
				print("cannot find combinition url: index-{}, product_url: {}".format(index, product_url))
				comb_url = []
			
			temp.append(index)
			temp.append(product_url)
			temp.append(product_description[0])
			temp.append(gender)
			temp.append(cat)
			temp.append(img_url)
			temp.append(product_description[1])
			temp.append(product_description[2])
			for comb in comb_url:
				temp.append(comb)
				if not comb in product_url_set:
					url_queue.append(comb)

			print(index, len(url_queue))
			writer.writerow(temp)



def get_category_dict(cat_dict_path):
	with open(cat_dict_path, 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter = ',')
		for row in reader:
			gender = row[0]
			cat = row[1]
			category_dict[gender][cat].add(row[2])


if __name__ == '__main__':
	args = arg()
	get_category_dict(args.cat_dict_path)
	comb_scrapping(args, 'men')
	comb_scrapping(args, 'women')