import requests
from bs4 import BeautifulSoup
import re

class scrapping_tools:

	def get_product_description(product_url):
		s = requests.session()
		p = requests.get(product_url)
		soup = BeautifulSoup(p.content, "html.parser")
		html_str = str(soup.prettify())
		title_str = re.findall(r"content=.*twitter\:title", html_str)[0]
		des_str = re.findall(r"content=.*twitter\:description", html_str)[0]
		title = re.sub(r"content=\"", "", title_str)
		title = re.sub(r"\".*", "", title)
		title = re.sub(r".* - ", "", title)
		des = re.sub(r"content=\"", "", des_str)
		des = re.sub(r"\".*", "", des)
		return title, des

	def get_img_url(product_url):
		s = requests.session()
		p = requests.get(product_url)
		soup = BeautifulSoup(p.content, "html.parser")
		picture = soup.find_all("picture")
		pattern1 = re.compile(r"\<img.*?product-detail lazyload.*?\>")
		res1 = re.findall(pattern1, str(picture))
		res_url = []
		for node in res1:
			pattern_jpg = re.compile(r"http.*\.jpg")
			temp = re.findall(pattern_jpg, node)
			res_url.append(temp[0])
		return res_url[0]

	def get_product_url(category_url: str) -> list:
		p = requests.get(category_url)
		soup = BeautifulSoup(p.content, "html.parser")
		urls = soup.find_all("a")
		res_url = []
		for url in urls:
			href = url.get("href")
			if re.search(r"product", href):
				res_url.append(href)
		return res_url