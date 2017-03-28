import requests
from bs4 import BeautifulSoup as soup
from lxml import html

read_headlines=raw_input("Do you wanna read the headlines? y/n: ")
if read_headlines == 'y':
	url = 'https://www.inshorts.com/en/read'
r = requests.get(url)
s= soup(r.content,"lxml")
headlines=s.findAll("span",{"itemprop":"headline"})
j=1
for i in headlines:
    print j,i.text
    j+=1

