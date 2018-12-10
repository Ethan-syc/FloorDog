import cv2
import numpy as np
from matplotlib import pyplot as plt
import os, time, csv
import requests, random
import shutil

csv_dir = '/home/zw119/floordog/scrapping_res/'
train_dir = '/home/zw119/floordog/dataset_resnet/train'
test_dir = '/home/zw119/floordog/dataset_resnet/test'
if not os.path.exists('/home/zw119/floordog/dataset_resnet'):
	os.mkdir('/home/zw119/floordog/dataset_resnet')
if not os.path.exists('/home/zw119/floordog/dataset_resnet/train'):
	os.mkdir('/home/zw119/floordog/dataset_resnet/train')
if not os.path.exists('/home/zw119/floordog/dataset_resnet/test'):
	os.mkdir('/home/zw119/floordog/dataset_resnet/test')

categories = {'men': ('jackets-coats', 'jeans', 'pants',
				'shirts', 'shorts', 'suits-blazers',
				'sweaters'), 
			'women': ('dresses', 'jackets-coats', 'jeans', 'jumpsuits',
				'pants', 'shorts', 'skirts', 'sweaters', 'tops')}

for gender in ('men', 'women'):
	if not os.path.exists(os.path.join(test_dir, gender)):
		os.mkdir(os.path.join(test_dir, gender))
	for category in categories[gender]:
			dir_temp = os.path.join(os.path.join(test_dir, gender), category)
			if not os.path.exists(dir_temp):
				os.mkdir(dir_temp)

def create_dataset(gender):
	csv_path = csv_dir + gender + '.csv'
	data_dir = os.path.join(train_dir, gender)

	if not os.path.exists(data_dir):
		os.mkdir(data_dir)
	for category in categories[gender]:
		dir_temp = os.path.join(data_dir, category)
		if not os.path.exists(dir_temp):
			os.mkdir(dir_temp)

	csv_file = open(csv_path, 'r')
	reader = csv.reader(csv_file, delimiter = ',')
	count = 0

	for row in reader:
		index = row[0]
		img_url = row[5]
		category = row[4]
		print('1:', gender, index)

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

def create_testset():
	for gender in ('men', "women"):
		for category in categories[gender]:
			img_train_dir = os.path.join(train_dir, gender)
			if not os.path.exists(img_train_dir):
				os.mkdir(img_train_dir)
			img_train_dir = os.path.join(img_train_dir, category)
			if not os.path.exists(img_train_dir):
				os.mkdir(img_train_dir)
			img_test_dir = os.path.join(test_dir, gender)
			if not os.path.exists(img_train_dir):
				os.mkdir(img_test_dir)
			img_test_dir = os.path.join(img_test_dir, category)
			if not os.path.exists(img_train_dir):
				os.mkdir(img_test_dir)

			imgs = os.listdir(img_train_dir)
			num = len(imgs)
			random.shuffle(imgs)

			for i in range(int(num/10)):
				print('1:', gender, category,"{}/{}".format(i, num))
				img_old_path = os.path.join(img_train_dir, imgs[i])
				img_new_path = os.path.join(img_test_dir, imgs[i])
				shutil.copy2(img_old_path, img_new_path)
				os.remove(img_old_path)

def copy_back():
	for gender in ('men', "women"):
		for category in categories[gender]:
			img_train_dir = os.path.join(train_dir, gender)
			if not os.path.exists(img_train_dir):
				os.mkdir(img_train_dir)
			img_train_dir = os.path.join(img_train_dir, category)
			if not os.path.exists(img_train_dir):
				os.mkdir(img_train_dir)
			img_test_dir = os.path.join(test_dir, gender)
			if not os.path.exists(img_train_dir):
				os.mkdir(img_test_dir)
			img_test_dir = os.path.join(img_test_dir, category)
			if not os.path.exists(img_train_dir):
				os.mkdir(img_test_dir)

			imgs = os.listdir(img_test_dir)
			num = len(imgs)

			for i in range(int(num)):
				print('1:', gender, category,"{}/{}".format(i, num))
				img_old_path = os.path.join(img_test_dir, imgs[i])
				img_new_path = os.path.join(img_train_dir, imgs[i])
				shutil.copy2(img_old_path, img_new_path)
				os.remove(img_old_path)

if __name__ == '__main__':
	#create_dataset('men')
	#create_dataset('women')
	create_testset()
	#copy_back()