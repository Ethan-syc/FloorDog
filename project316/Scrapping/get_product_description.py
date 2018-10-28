import requests
from bs4 import BeautifulSoup
import re

def get_product_des(product_url):
	s = requests.session()
	p = requests.get(product_url)
	soup = BeautifulSoup(p.content, 'html.parser')
	html_str = str(soup.prettify())
	title_str = re.findall(r"content=.*twitter\:title", html_str)[0]
	des_str = re.findall(r"content=.*twitter\:description", html_str)[0]
	title = re.sub(r"content=\"", '', title_str)
	title = re.sub(r"\".*", '', title)
	title = re.sub(r".* - ", '', title)
	des = re.sub(r"content=\"", '', des_str)
	des = re.sub(r"\".*", '', des)

	return title, des
	'''
	des = soup.find_all("div", class_ = "product-item-container row-fluid")[0]
	container = des.find_all("div", class_ = "product-description-container")[0]
	content = container.find_all("div", class_ = "content")[0]
	content_div = content.find_all("div")[0]
	print(content_div.find_all())
	'''
	'''
	pattern1 = re.compile(r"\<img.*?product-detail lazyload.*?\>")
	res1 = re.findall(pattern1,str(picture))
	res_url = []
	for node in res1:
		pattern_jpg = re.compile(r"http.*\.jpg")
		temp = re.findall(pattern_jpg, node)
		res_url.append(temp[0])

	return res_url[0]
	'''

if __name__ == '__main__':
	product_url = 'https://www.ssense.com/en-us/men/product/undercover/black-astronaut-hoodie/3089828'
	get_product_des(product_url)