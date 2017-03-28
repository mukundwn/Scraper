import requests
from bs4 import BeautifulSoup as soup
from lxml import html
url = 'https://www.timeanddate.com/weather/'
r = requests.get(url)
s = soup(r.content,"lxml")
read_loc = raw_input("Enter the place you'd want the weather at: ")
sec_url = url+'india/'+read_loc
r1=requests.get(sec_url)
s1=soup(r1.content,"lxml")
temperature=s1.findAll("p")
for i in temperature[0:9]:
	print i.text
