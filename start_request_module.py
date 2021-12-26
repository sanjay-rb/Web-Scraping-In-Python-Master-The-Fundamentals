"""
Created on Sun Dec 26 10:59:34 2021

@author: Sanjay
"""
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
