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
root = 'https://www.ssense.com'

category_max = 1000

def scrap(args):
	scrap_by_gender(args, 'men')
	scrap_by_gender(args, 'women')


def arg():
	parser = argparse.ArgumentParser(description='save data directory')
	parser.add_argument('--csv_dir', dest = 'csv_dir', type=str,
                    default='/Users/evnw/Documents/GitHub/FloorDog/project316')
	args = parser.parse_args()
	return args

def scrap_by_gender(args, gender):
	csv_path = os.path.join(args.csv_dir, gender+"_clothes_comb.csv")
	with open(csv_path, 'w', newline='') as csvfile:
		writer = csv.writer(csvfile, delimiter=',')

		index = 0
		category_index = 0
		
		for cat in category[gender]:
			category_index += 1
			product_index = 0
			print(gender+" category: {}/{}".format(category_index, len(men_category)))

			for i in range(1, 100):

				cat_url = root + '/en-us/' + gender + '/' + cat
				if i != 1:
					cat_url += "?page={}".format(i)

				try:
					product_urls = scrapping_tools.get_product_url(cat_url)
				except:
					print("end of category: page{}".format(i+1))
					break

				for product_url in product_urls:
					print(product_url)
					product_index += 1
					index += 1

					if(product_index > 1000):
						break
					if(product_index%10 == 0):
						print(gender + "/{}: page{}, {}/{}".format(cat, i, product_index, len(product_urls)*i))

					product_url = root + product_url

					print("get_product_url")

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

					try:
						specific_cat = get_specific_category(product_url)
						category_dict[gender][cat].add(specific_cat)

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

					if(product_index > 1000):
						break
				if(product_index > 1000):
						break


def get_specific_category(product_url):
	cat = re.findall(r"-.*?/[0-9]", product_url)[0]
	cat = re.sub(r"-.*-", '', cat)
	cat = re.sub(r"/[0-9]", '', cat)
	return cat


def save_cat_dict(args):
	dict_path = os.path.join(args.csv_dir, 'cat_dict.csv')
	with open(dict_path, 'w', newline = '') as csvfile:
		writer = csv.writer(csvfile, delimiter=',')
		for gender in ('men', 'women'):
			for cat in category_dict[gender].keys():
				for specific_cat in category_dict[gender][cat]:
					temp = []
					temp.append(gender)
					temp.append(cat)
					temp.append(specific_cat)
					writer.writerow(temp)

if __name__ == '__main__':
	args = arg()
	clothes = scrap(args)
	save_cat_dict(args)














