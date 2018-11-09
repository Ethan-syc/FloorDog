

import urllib.request
import requests
import lxml
import re
from urllib.parse import urlparse
from lxml.html import fromstring
from html import unescape
from collections import Counter
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import xml.etree.ElementTree as ET
from lxml import etree


def getText(url):

    try:
        response = requests.get(url, headers=headers)
        return response.text

    except:
        return ""

        # return results from Google search, given a search term & number of results

        def fetch_results(search_term, number_results, language_code):
            assert isinstance(search_term, str), 'Search term must be a string'
            assert isinstance(number_results, int), 'Number of results must be an integer'
            escaped_search_term = search_term.replace(' ', '+')

            google_url = 'https://www.google.com/search?q={}&num={}&hl={}'.format(escaped_search_term,
                                                                                  number_results, language_code)


            response = requests.get(google_url, USER_AGENT)
            response.raise_for_status()

            return response.text


def scrape_results(html):
    soup = BeautifulSoup(html, 'html.parser')

    results = []
    rank = 1

    result_block = soup.find_all('div', attrs={'class': 'g'})
    for result in result_block:

        link = result.find('a', href=True)
        title = result.find('h3', attrs={'class': 'r'})
        description = result.find('span', attrs={'class': 'st'})

        if link and title:
            link = link['href']
            title = title.get_text()
            # print(title)
            if description:
                description = description.get_text()
                # print(description)
            if link != "#":
                new_link = link[7:].split("&")[0]
                results.append([rank, title, description, new_link])
                rank += 1

    df = pd.DataFrame(results)
    df.columns = ['Rank', 'title', 'description', 'url']

    return df
