import requests
from bs4 import BeautifulSoup as soup
from lxml import html

read_news=raw_input("Do you wanna read the news? y/n: ")
if read_news == 'y':
	url = 'https://www.inshorts.com/en/read'
r = requests.get(url)
s= soup(r.content,"lxml")
news=s.findAll("div",{"itemprop":"articleBody"})
j=1
for i in news:
    print "NEWS",j,i.text
    print '\n'
    j=j+1

