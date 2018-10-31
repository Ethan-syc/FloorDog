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

root = 'https://www.ssense.com'

catagory_max = 1000

def scrap(args):
	csv_path = os.path.join(args.csv_dir, "clothes.csv")
	with open(csv_path, 'w', newline='') as csvfile:
		writer = csv.writer(csvfile, delimiter=',')

		index = 0
		catagory_index = 0
		
		for cat in men_category:
			catagory_index += 1
			product_index = 0
			print("men catagory: {}/{}".format(catagory_index, len(men_category)))

			for i in range(1, 100):

				cat_url = root + '/en-us/' + 'men/' + cat
				if i != 1:
					cat_url += "?page={}".format(i)

				try:
					product_urls = scrapping_tools.get_product_url(cat_url)
				except:
					print("end of catagory: page{}".format(i+1))
					break

				for product_url in product_urls:
					product_index += 1
					index += 1

					if(product_index > 1000):
						break
					if(product_index%10 == 0):
						print("men/{}: page{}, {}/{}".format(cat, i, product_index, len(product_urls)*i))

					product_url = root + product_url

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
						product_description=['null','null']

					temp.append(index)
					temp.append(product_url)
					temp.append(product_description[0])
					temp.append('men')
					temp.append(cat)
					temp.append(img_url)
					temp.append(product_description[1])
					writer.writerow(temp)

				if(product_index > 1000):
						break

		catagory_index = 0

		for cat in women_category:

			catagory_index += 1
			product_index = 0
			print("women catagory: {}/{}".format(catagory_index, len(women_category)))

			for i in range(1, 100):

				cat_url = root + '/en-us/' + 'women/' + cat

				if i != 1:
					cat_url += "?page={}".format(i)

				try:
					product_urls = scrapping_tools.get_product_url(cat_url)
				except:
					print("end of catagory: page{}".format(i+1))
					break

				for product_url in product_urls:
					product_index += 1
					index += 1

					if(product_index > 1000):
						break
					if(product_index%10 == 0):
						print("women/{}: page{}, {}/{}".format(cat, i, product_index, len(product_urls)*i))

					product_url = root + product_url
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
						product_description=['null','null']

					temp.append(index)
					temp.append(product_description[0])
					temp.append('women')
					temp.append(cat)
					temp.append(img_url)
					temp.append(product_description[1])
					writer.writerow(temp)

				if(product_index > 1000):
						break


def arg():
	parser = argparse.ArgumentParser(description='save data directory')
	parser.add_argument('--csv_dir', dest = 'csv_dir', type=str,
                    default='/Users/evnw/Documents/GitHub/FloorDog/project316')
	args = parser.parse_args()
	return args


if __name__ == '__main__':
	args = arg()
	clothes = scrap(args)














