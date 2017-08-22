# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 21:05:10 2017

@author: NKallfa
"""

import requests
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import pandas as pd
import re

url = "https://www.beeradvocate.com/place/city/19/"

page = requests.get(url)

soup = BeautifulSoup(page.text)

soup2 = soup.find_all("li")
links = []

for link in soup.find_all('a', href=True):
    links.append(link['href'])
    
links = pd.DataFrame(links)   
linkRegex = re.compile(r"(/beer/profile/)(\d){1,6}(/)$")

tlinks = []
index = []

def RegSearch(x):
    linkRegex = re.compile(r"(/beer/profile/)(\d){1,6}(/)$")
    x  = str(x)
    test = linkRegex.search(x)
    if test is not None:
        return(test.group())
    else:
        return("False")
    
for i in range(0,235,1):
    if RegSearch(links[0][i]) is not "False":
        tlinks.append(links[0][i])
        index.append(i)
    else:
        tlinks = tlinks

#links.apply(lambda x: tlinks.append(linkRegex.search(x)) if RegSearch(x) is not "False" else print(), axis = 1)