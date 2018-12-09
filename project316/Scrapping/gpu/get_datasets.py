import cv2
import numpy as np
from matplotlib import pyplot as plt
import os, time, csv
import requests

csv_dir = '/floordog/scrapping_res/'
res_dir = '/floordog/dataset_resnet/'

categories = {'men': ('jackets-coats', 'jeans', 'pants',
				'shirts', 'shorts', 'suits-blazers',
				'sweaters'), 
			'women': ('dresses', 'jackets-coats', 'jeans', 'jumpsuits',
				'pants', 'shorts', 'skirts', 'sweaters', 'tops')}

def create_dataset(gender):
	csv_path = csv_dir + gender + '.csv'
	data_dir = os.path.join(res_dir, 'gender')

	if not os.path.exists(data_dir):
		os.mkdir(data_dir)
	for category in categories[gender]:
		dir_temp = os.path.join(data_dir, category)
		if not os.path.exists(dir_temp):
			os.mkdir(dir_temp)

	csv_file = open(csv_path, 'r')
	reader = csv.reader(csv_file, delimieter = ',')
	count = 0

	for row in reader:
		index = row[0]
		img_url = row[5]
		category = row[4]

		if category not in categories[gender]:
			continue

		count += 1

		img_dir = os.path.join(data_dir, category)
		img_path = os.path.join(img_dir, '{}.jpg'.format(index))
		response = requests.get(img_url)
		image = response.content
		f = open(img_path,'wb')
		f.write(image)
		f.close()

if __name__ == '__main__':
	create_dataset('men')
	create_dataset('women')