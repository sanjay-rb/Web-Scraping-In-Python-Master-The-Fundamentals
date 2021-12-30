'''
Created on 27 December 2021 12:23:34

@author: Sanjay R B
'''

import requests
from bs4 import BeautifulSoup
from pprint import pprint

wikiUrl = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

responce = requests.get(wikiUrl)
html = responce.text

soup = BeautifulSoup(html, features='html.parser')

symbols = []
tbody = soup.find_all('tbody')
first_table_tr = tbody[0].contents

for i in range(2, len(first_table_tr)):
    if i % 2 == 0:
        symbols.append(first_table_tr[i].td.text.strip('\n'))

pprint(symbols)
print("There are", str(len(symbols)), "companies in this wiki table")