# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 21:14:13 2019

@author: derek.mulhausen
"""

import urllib
from bs4 import BeautifulSoup

r=urllib.request.urlopen('https://www.census.gov/programs-surveys/popest.html')
soup=BeautifulSoup(r,"lxml")

AllLinks=[]

for link in soup.find_all('a'):
    tempStr=link.get('href')
    if(isinstance(tempStr,str)):
        if(tempStr.find('http')==0):
            AllLinks.append(tempStr)
        elif((tempStr.find('/')==0)&(len(tempStr)>1)):
            AllLinks.append('https://www.census.gov'+tempStr)

#remove duplicates
i=0
while i<len(AllLinks):
    j=i+1
    while j<len(AllLinks):
        if(AllLinks[i]==AllLinks[j]):
            AllLinks.pop(j)
        else:
            j=j+1
    i=i+1
f=open('CensusLinks.csv','w+')
for link in AllLinks:
    f.write(link + '\n')
f.close()
