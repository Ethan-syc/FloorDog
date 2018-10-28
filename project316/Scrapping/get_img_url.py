import requests
from bs4 import BeautifulSoup
import re

def get_img_url(product_url)
	s = requests.session()
	p = requests.get(product_url)
	soup = BeautifulSoup(p.content, 'html.parser')
	picture = soup.find_all("picture")
	pattern1 = re.compile(r"\<img.*?product-detail lazyload.*?\>")
	res1 = re.findall(pattern1,str(picture))
	res_url = []
	for node in res1:
		pattern_jpg = re.compile(r"http.*\.jpg")
		temp = re.findall(pattern_jpg, node)
		res_url.append(temp[0])

	return res_url[0]

	#pattern2 = re.compile(r"http.*?(?:jpg|png)")
	#res = re.findall(pattern, str(picture))
	#print(picture)

	#children = body.find()
	#print(children)