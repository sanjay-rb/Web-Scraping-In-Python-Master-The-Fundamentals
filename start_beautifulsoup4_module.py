'''
Created on 27 December 2021 10:15:07

@author: Sanjay R B
'''
import requests
from bs4 import BeautifulSoup

from pprint import pprint

url = 'https://finance.yahoo.com/quote/AAPL?p=AAPL'
responce = requests.get(url)
html = responce.text

soup = BeautifulSoup(html, features="html.parser")

tag = 'Previous Close'
find_by_tag = soup.find_all('tr')
for row in find_by_tag:
    if tag in row.text:
        value = row.text.split(tag)[-1]
        print(tag, "tag value :", value)
        '''
        Previous Close tag value : 175.64
        '''
        break

find_by_class = soup.find_all('td', class_="C($primaryColor) W(51%)")
list_of_tag_have_class = []
for row in find_by_class:
    if row != None:
        list_of_tag_have_class.append(row.text)
pprint(list_of_tag_have_class)
'''
['Previous Close',
 'Open',
 'Bid',
 'Ask',
 "Day's Range",   
 '52 Week Range',
 'Volume',
 'Avg. Volume',
 'Market Cap',
 'Beta (5Y Monthly)',
 'PE Ratio (TTM)',
 'EPS (TTM)',
 'Earnings Date',
 'Forward Dividend & Yield',
 'Ex-Dividend Date',
 '1y Target Est']
 '''

find_by_attribute = soup.find_all(
    'td', attrs={"data-test": "PREV_CLOSE-value"})
list_of_tag_have_attribute = []
for row in find_by_attribute:
    if row != None:
        list_of_tag_have_attribute.append(row.text)
pprint(list_of_tag_have_attribute)
'''
['175.64']
'''

# To find all values from the table till 1y Target Est
tagVal = {}
find_by_tag = soup.find_all('tr')
for row in find_by_tag:
    tag = row.find('td', class_="C($primaryColor) W(51%)")
    val = row.find('td', class_="Ta(end) Fw(600) Lh(14px)")
    if tag != None and val != None:
        tagVal[tag.text] = val.text
pprint(tagVal)
'''
{'1y Target Est': '174.93',
 '52 Week Range': '116.21 - 182.13',
 'Ask': '176.40 x 1000',
 'Avg. Volume': '90,843,769',
 'Beta (5Y Monthly)': '1.20',
 'Bid': '176.27 x 800',
 "Day's Range": '175.28 - 176.85',
 'EPS (TTM)': '5.61',
 'Earnings Date': 'Jan 25, 2022 - Jan 31, 2022',
 'Ex-Dividend Date': 'Nov 05, 2021',
 'Forward Dividend & Yield': '0.88 (0.50%)',
 'Market Cap': '2.892T',
 'Open': '175.85',
 'PE Ratio (TTM)': '31.42',
 'Previous Close': '175.64',
 'Volume': '68,356,867'}
'''
