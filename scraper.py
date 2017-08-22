# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 19:21:32 2017

@author: NKallfa
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

alldata = []
for url2 in tlinks[0:10]:

    url = "https://www.beeradvocate.com/" + url2
#url = "https://www.beeradvocate.com/beer/profile/33521/"

    data = requests.get(url)
    
    page = BeautifulSoup(data.text)
    
    brewstats = page.find_all('div', attrs = {"id": "item_stats"})
    
    table_body=page.find('tbody')
    rows = table_body.find_all('tr')
    BreweryName = page.find("title").text.strip().split("|")[0]
    BreweryCity = page.find("title").text.strip().split("|")[1]
    beerlist = []
    
    for row in rows:
        cols=row.find_all('td')
        cols=[x.text.strip() for x in cols]
        beerlist.append(cols)
        
    df = pd.DataFrame(beerlist)
    df.drop([5,6],axis = 1,inplace = True)
    df.rename(columns = {0: "Beer", 1: "Type", 2: "ABV", 3:"NRating", 4:"AvgRating"}, inplace = True)
    df = pd.concat([df,pd.DataFrame([page.find("title").text.strip().split("|")[0]]*len(df), columns = ["Brewery"]), pd.DataFrame([page.find("title").text.strip().split("|")[1]]*len(df), columns = ["City"])], axis = 1)
    alldata.append(df)
