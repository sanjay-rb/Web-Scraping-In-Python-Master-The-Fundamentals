'''
Created on 27 December 2021 10:16:10

@author: Sanjay R B
'''
import requests

url = 'https://finance.yahoo.com/quote/AAPL?p=AAPL'
responce = requests.get(url)

print("Responce :", responce)
print("Status code :", responce.status_code)
html = responce.text

# This logic may change when source {html} is changed from website!
tag = 'Previous Close'
tag_index = html.index(tag)
content = html[tag_index:].split('</td>')
value = content[1].split('>')[-1]
print(tag, "tag value :", value)
