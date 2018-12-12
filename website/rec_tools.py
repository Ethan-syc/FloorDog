from website.fas_resnet_pred import men_pred, women_pred
from website.color_recognition_tool import color_recognition
from website.recommend import recommendation_similar
import cv2, os
import webcolors

txt_path = 'website/id_lists/result.txt'
im_root = 'website/uploaded_files'
im_path = os.path.join(im_root, os.listdir(im_root)[0])


def rec_rec(gender):
	if gender == 'men':
		cat = men_pred(im_path)
	else:
		cat = women_pred(im_path)
	im = cv2.imread(im_path)
	colors = color_recognition(im)
	temp = []
	for color in colors:
		rgb = (color[2], color[1], color[0])
		hex = webcolors.rgb_to_hex(rgb)
		temp.append(hex)
	while len(temp) < 3:
		temp.append(temp[0])

	hex_colors = temp
	if len(temp) > 3:
		hex_colors = hex_colors[0:3]
	indexes = recommendation_similar(gender, cat, hex_colors[0], hex_colors[1], hex_colors[2])
	index_str = ''
	i = 0
	for index in indexes:
		if i == 0:
			index_str += str(index)
			i += 1
		else:
			index_str += ','
			index_str += str(index)

	'''
	print(index_str)
	f = open(txt_path)
	print(type(index_str))
	f.write(index_str)
	f.close()
	'''
	print(indexes)
	return indexes
