import re
import os
from bs4 import BeautifulSoup

fips = open('test.html','r',encoding='utf-8')
soup=BeautifulSoup(fips, 'lxml')

#забирает только строки с цифрами и более 5 знаков
strings = soup.find_all(string=re.compile('^[0-9]\d{5,20}'))
pn_list = []
for txt in strings:
    pn_list.append(" ".join(txt.split()))
#print(pn_list)
    