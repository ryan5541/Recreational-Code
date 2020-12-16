# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 16:43:02 2018

@author: Ryan Gamilo
"""
import requests
import re
from bs4 import BeautifulSoup

r = requests.get('https://ielanguages.com/romlang.html')
soup = BeautifulSoup(r.content, 'html.parser')

vocab_links = []
vocab_lists = soup.find('ol')
for li in vocab_lists.find_all('li'):
    vocab_links.append(li.find('a')['href'])

row_list = []
col_list = []

for href in vocab_links:
    r = requests.get('https://ielanguages.com/'+href)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find(class_=re.compile('table table-striped table-bordered table-hover'))
    rows = table.find_all('tr')[1:]
    for tr in rows:
        cols = tr.find_all('td')
        col_list = []
        for td in cols:
            for br in td.find_all('br'):
                br.extract()
            for em in td.find_all('em'):
                em.extract()
            if td.find('strong') is None:
                data_text = td.text
            else:
                data_text = td.find('strong').text
            col_list.append(re.sub('[\t\r\n\v\f]|\\xa0',"", data_text))
        print(col_list)
        row_list.append(col_list)

fullStr = ""
for row in row_list:
    if "" not in row:
        rowStr = "|".join(row)
        fullStr = fullStr + rowStr +"\n"
    
f = open('vocab', 'w', encoding='utf-8')
f.write(fullStr)
f.close()
