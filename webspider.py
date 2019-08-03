from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
import re
import random


base_url = "https://baike.baidu.com/item/"
key = ["测试"]
url = base_url + key[-1]
print(url)
html = requests.get(url).text
soup = BeautifulSoup(html, features='lxml')
print(soup.find('h1').get_text(), '    url: ', key[-1])
