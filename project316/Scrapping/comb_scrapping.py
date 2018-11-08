import requests
from bs4 import BeautifulSoup
import re
from scrapping_tools import scrapping_tools
import argparse
import csv, os

def arg():
	parser = argparse.ArgumentParser(description='save data directory')
	parser.add_argument('--csv_dir', dest = 'csv_dir', type=str,
                    default='/Users/evnw/Documents/GitHub/FloorDog/project316')
	args = parser.parse_args()
	return args

def initialize(args, gender):
	csv_path = os.path.join(args.csv_dir, gender+"_clothes_comb.csv")
	product_url_dict = {}
	product_url_set = set([])
	comb_url_set = set([])
	max_index = 0
	with open(csv_path, 'r', newline='') as csvfile:
		reader = csv.reader(csvfile, delimiter = ',')
		for row in reader:
			index = row[0]
			product_url = row[1]
			comb_urls = row[8:]
			product_url_dict[product_url] = index
			product_url_set.add(product_url)
			for url in comb_urls:
				comb_url_set.add(url)
			if index>max_index:
				max_index = index
	return product_url_set, product_url_dict, comb_url_set, max_index

def comb_scrapping(args, gender)
	url_set, url_dict, comb_set, max_index = initialize(args, gender)
	with open(csv_path, 'a', newline = '') as csvfile:
		writer = csv.reader(csvfile, delimiter = ',')
		index = max_index
		for url in comb_url_set:
			if not url in url_set:
				index += 1
				scrap(url, writer, index)
				
def scrap(url, writer, index):
	temp = []

	try:
		img_url = scrapping_tools.get_img_url(product_url)
	except:
		print("cannot find image url: index-{}, product_url: {}".format(index, product_url))
		img_url = 'null'
	print('get_img_url')

	try:
		product_description = scrapping_tools.get_product_description(product_url)
	except:
		print("cannot find description: index-{}, product_url: {}".format(index, product_url))
		product_description=['null','null','null']
	print('get_product_description')

	try:
		comb_url = scrapping_tools.get_comb_url(product_url)
	except:
		print("cannot find combinition url: index-{}, product_url: {}".format(index, product_url))
		comb_url = []
		print('get comb url')

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
	print("appending")

	writer.writerow(temp)
	print('write')

if __name__ == '__main__':
	args = arg()
	comb_scrapping(args, 'men')
	comb_scrapping(args, 'women')