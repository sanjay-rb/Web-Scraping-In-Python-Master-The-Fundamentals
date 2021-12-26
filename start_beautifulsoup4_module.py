"""
Created on Sun Dec 26 10:59:34 2021

@author: Sanjay
"""
import requests
from bs4 import BeautifulSoup

url = 'https://finance.yahoo.com/quote/AAPL?p=AAPL'
responce = requests.get(url)

print("Responce :", responce)
print("Status code :", responce.status_code)
html = responce.text

tag = 'Previous Close'
soup = BeautifulSoup(html, features="html.parser")

find_by_tag = soup.find_all('tr')
for row in find_by_tag:
    if tag in row.text:
        value = row.text.split(tag)[-1]
        print(tag, "tag value :", value)
        break

find_by_class = soup.find_all('td', class_="C($primaryColor) W(51%)")
for row in find_by_class:
    print("find_by_class", row)

find_by_attribute = soup.find_all('td',attrs={"data-test":"PREV_CLOSE-value"})
for row in find_by_attribute:
    print("find_by_attribute", row)