# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 11:16:00 2020

@author: Ryan Gamilo
"""

import requests
import re
from bs4 import BeautifulSoup

r = requests.get('https://en.wikipedia.org/wiki/Lists_of_foods')
soup = BeautifulSoup(r.content, 'html.parser')

body = soup.find(class_ = 'mw-parser-output')
liLists = body.findAll('li')
foodLists = []
for liList in liLists:
    if liList.find('a') is not None:
        if re.search('^/wiki', liList.find('a')['href']) is not None:
            if re.search('[Cc]ategory', liList.find('a')['href']) is not None or re.search(':', liList.find('a')['href']) is None:
                foodLists.append(liList.find('a'))

for fList in foodLists:
    r = requests.get('https://en.wikipedia.org/wiki/' + fList['href'])
    soup = BeautifulSoup(r.content, 'html.parser')
    if re.search('[Cc]ategory', fList['href']) is not None:
        if soup.find_all(class_='CategoryTreeBullet') is not None:
            #categories = soup.find_all(class_='CategoryTreeBullet')
            pass
    elif re.search('#', fList['href']) is not None:
        pass
    else:
        pass
            
            
        
        
    


