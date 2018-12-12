import cv2
import numpy as np
from matplotlib import pyplot as plt
import os, time, webcolors, csv
from sklearn.cluster import KMeans
import xml.etree.ElementTree as ET
#import requests

kmeans = KMeans(10)

csv_dir = "/Users/evnw/Documents/GitHub/FloorDog/project316"
img_path = os.path.join(csv_dir, 'temp2.jpg')

class Color:
	
	def __init__(self, num, BGR):
		self.BGR = BGR
		self.num = num
		self.dist = np.sqrt(BGR[0]**2 + BGR[1]**2 + BGR[2]**2)
		self.Blue = BGR[0]
		self.Green = BGR[1]
		self.Red = BGR[2]

	def calc_dist(self, Color):
		dist = np.sqrt((int(self.Blue)-int(Color.Blue))**2 + (int(self.Green)-int(Color.Green))**2 + (int(self.Red)-int(Color.Red))**2)
		return dist

def color_recognition(im):

	# RGB2BGR
	im = im[...,::-1]
	im_s = cv2.resize(im, (15, 15))

	background = find_background(im_s)

	#print(background)

	# KMeans
	im_arr = im_s.reshape((im_s.shape[0] * im_s.shape[1], 3))
	kmeans.fit(im_arr)
	colors = kmeans.cluster_centers_.astype(np.uint8)								 #BGR
	labels = kmeans.labels_

	# Create color class
	color_array = []
	for i in range(10):
		color_temp = Color(len(np.where(labels==i)[0]), colors[i])
		color_array.append(color_temp)

	thresh = 50
	# find number of significant colors
	color_res, color_num = color_filter(color_array, thresh)
	while color_num < 2:
		print('refind')
		thresh -= 5
		color_res, color_num = color_filter(color_array, thresh)
		if thresh < 35:
			break

	kmeans_res = KMeans(color_num)
	kmeans_res.fit(im_arr)
	colors_final = kmeans_res.cluster_centers_.astype(np.uint8)

	if color_num == 1:
		return colors_final

	#plt.imshow(im);plt.show()
	#plt.imshow([colors_final]);plt.show()

	min_dist = 999999
	closest_BGR_index = None

	for i in range(len(colors_final)):
		color_BGR = colors_final[i]
		dist = np.sqrt((int(color_BGR[0] - int(background[0])))**2 + (int(color_BGR[1] - int(background[1])))**2 + (int(color_BGR[2] - int(background[2])))**2)
		if dist < min_dist:
			min_dist = dist
			closest_BGR_index = i

	colors_final_noback = np.delete(colors_final, closest_BGR_index, 0)

	if len(colors_final_noback) == 0:
		return colors_final


	#plt.imshow([colors_final]);plt.show()

	#print(colors_final)

	return colors_final_noback

def color_filter(color_array, min_dist_thresh):

	distant_color_num = 0
	res = []
	current = Color(500, [0,0,0])

	while len(color_array) > 0:

		closest_color = None
		min_dist = 9999999

		for color in color_array:
			dist = current.calc_dist(color)
			#dist = current.calc_dist(color)
			if (dist < min_dist):
				min_dist = dist
				closest_color = color

		if min_dist >= min_dist_thresh:
			distant_color_num += 1
		if current.num >= 500 and min_dist < min_dist_thresh:
			distant_color_num += 1


		res.append(closest_color)
		current = closest_color
		color_array.remove(closest_color)

	return res, max(distant_color_num - 1, 1)



def find_background(im):
	edge_BGRs = im[0,:]+im[:,0]

	kmeans_background = KMeans(2)
	kmeans_background.fit(edge_BGRs)
	labels = kmeans_background.labels_
	if len(np.where(labels == 0)[0]) > len(np.where(labels == 1)[0]):
		index = 0
	else:
		index = 1

	return kmeans_background.cluster_centers_[index]


def create_xml(colors, url):
	root = ET.Element("Outfit")
	link = ET.SubElement(root, 'link')
	dom_colors = ET.SubElement(root, 'dom_colors')
	ET.SubElement(link, "url").text = "{}".format(url)
	for color_BGR in colors:
		color = ET.SubElement(dom_colors, "color")
		ET.SubElement(color, "blue").text = "{}".format(color_BGR[0])
		ET.SubElement(color, "green").text = "{}".format(color_BGR[1])
		ET.SubElement(color, "red").text = "{}".format(color_BGR[2])
	tree = ET.ElementTree(root)

	xml_path = os.path.join(res_dir, 'test.xml')
	tree.write(xml_path)

def color_attr(gender):
	csv_path = os.path.join(csv_dir, gender+'.csv')
	csv_file = open(csv_path, 'r')
	csv_color_path = os.path.join(csv_dir, gender+'_color.csv')
	csv_color_file = open(csv_color_path, 'w')
	writer = csv.writer(csv_color_file, delimiter = ',')
	reader = csv.reader(csv_file, delimiter = ',')
	for row in reader:
		index = int(row[0])
		print(index)
		img_url = row[5]
		response = requests.get(img_url)
		image = response.content
		f = open(img_path,'wb')
		f.write(image)
		f.close()
		im = cv2.imread(img_path)
		colors = color_recognition(im)
		while len(colors) == 0:
			colors = color_recognition(im)
			print(colors)
		temp = []
		temp.append(index)
		for color in colors:
			rgb = (color[2], color[1], color[0])
			hex = webcolors.rgb_to_hex(rgb)
			temp.append(hex)
		colors = temp
		writer.writerow(temp)
		os.remove(img_path)


if __name__ == '__main__':
	#color_attr('men')
	color_attr('women')
'''
	url = img_path											  # need change
	im = cv2.imread(img_path)

	tm = time.time() #---------------------------------------------------------

	dominant_colors = color_rec(im)
	create_xml(dominant_colors, url)

	print(time.time() - tm) #--------------------------------------------------'''

	