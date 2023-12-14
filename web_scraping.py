import bs4
import requests

url = 'https://books.toscrape.com/catalogue/page-{}.html'

for n in range(1,15):
    print(url.format(n))