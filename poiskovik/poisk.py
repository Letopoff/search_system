import re
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = str(input("Введите сайт\n"))
slovo = str(input("Введите запрос\n"))
page = urlopen(url)
html = page.read().decode("Utf-8")
soup = BeautifulSoup(html, "lxml")
print(soup.find_all(string=re.compile(slovo)))