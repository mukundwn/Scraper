from lxml import html 
import requests
import os
from bs4 import BeautifulSoup as soup

base_url = "https://genius.com/search?q="
inp=raw_input("Enter the name of the song: \n")
sec_url=base_url+inp
r1=requests.get(sec_url)
s=soup(r1.content,"lxml")

titles = s.findAll("span", {"class":"song_title"})
artists = s.findAll("span", {"class":"artist_name"})
for i in range(len(titles)):
    print i+1,")" + titles[i].text + " by "  +artists[i].text

links = s.findAll("a", {"class":" song_link"})
    
songinfo = {}

for i in range(len(titles)):
    songinfo[i] = {"Titles":titles[i].text,"Artists":artists[i].text,"url":links[i]["href"]}

choice=int(raw_input("Enter your choice from the above list: \n"))

print "\n" * 10
print "\t\tLyrics:\n"

R = requests.get(songinfo[choice -1]["url"])
s1 = soup(R.content,"lxml")
lyric = s1.findAll("a",{"classification":"accepted"})
for l in lyric:
    print l.text 





